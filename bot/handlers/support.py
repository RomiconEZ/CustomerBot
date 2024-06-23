import aiohttp
from aiogram import Router, types
from aiogram.filters import Command
from aiogram.utils.i18n import gettext as _
from aiohttp import ClientConnectorError
from loguru import logger

from bot.core.config import settings
from bot.core.loader import redis_client
from bot.handlers.message import get_user_message_history_key

router = Router(name="support")
support_error_text = (f"В данный момент тур-агенты {settings.COMPANY_NAME} не могут ответить по вашему обращению, "
                      f"пожалуйста, обратитесь позже")


@router.message(Command(commands=["supports", "support", "оператор", "помощь"]))
async def support_handler(message: types.Message) -> None:
    """None"""
    # Получаем Telegram ID пользователя
    user_id = message.from_user.id

    # Получаем никнейм пользователя в Telegram
    username = message.from_user.username

    try:
        # Получаем историю из Redis
        key = get_user_message_history_key(user_id)
        history = await redis_client.lrange(key, 0, -1)  # Use `await` here
        history = [eval(item) for item in history]

        # Подготовка данных для отправки
        data = {
            "customer": {
                "id": user_id,
                "name": None,
                "surname": None,
                "patronymic": None,
                "username_telegram": username,
                "email": None,
            },
            "context": history,
        }

        # Отправка POST-запроса
        async with aiohttp.ClientSession() as session:
            async with session.post(
                    settings.PREFIX_GEN_BACKEND_URL + "waiting_customer",
                    json=data,
                    headers={"Content-Type": "application/json", "accept": "application/json"},
            ) as response:
                if response.status == 201:
                    await message.answer(
                        _(
                            f"С вами свяжется тур-агента {settings.COMPANY_NAME}, "
                            "пожалуйста ожидайте обратной связи, по вашему обращению."
                        )
                    )
                elif response.status == 409:
                    await message.answer(
                        _(
                            "Пожалуйста, ожидайте, когда с вами свяжется "
                            f"тур-агент {settings.COMPANY_NAME}."
                        )
                    )
                else:
                    await message.answer(
                        _(support_error_text)
                    )
    except ClientConnectorError:
        logger.error("The connection to the backend server could not be established.")
        await message.answer(_(support_error_text))
    except Exception as e:
        logger.error(f"An error has occurred: \n {e}")
        await message.answer(_(support_error_text))
