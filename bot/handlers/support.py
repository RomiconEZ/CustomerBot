import aiohttp
from aiogram import Router, types
from aiogram.filters import Command
from aiogram.utils.i18n import gettext as _
from icecream import ic

from bot.core.config import settings
from bot.core.loader import redis_client

router = Router(name="support")


@router.message(Command(commands=["supports", "support", "оператор", "помощь"]))
async def support_handler(message: types.Message) -> None:
    """None"""
    # Получаем Telegram ID пользователя
    user_id = message.from_user.id

    # Получаем никнейм пользователя в Telegram
    username = message.from_user.username

    # Получаем историю из Redis
    chat_id = message.chat.id
    key = f"chat_{chat_id}_user_{user_id}_history"
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
            ic(response)
            if response.status == 201:
                await message.answer(
                    _(
                        "С вами свяжется тур-агента KareliaTour, "
                        "пожалуйста ожидайте обратной связи, по вашему обращению."
                    )
                )
            elif response.status == 409:
                await message.answer(
                    _(
                        "Пожалуйста, ожидайте, когда с вами свяжется "
                        "тур-агент KareliaTour."
                    )
                )
            else:
                await message.answer(
                    _(
                        "В данный момент тур-агенты KareliaTour не могут "
                        "ответить по вашему обращению, пожалуйста, обратитесь позже"
                    )
                )
