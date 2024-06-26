import aiohttp
from aiogram import Router, types
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.utils.i18n import gettext as _
from aiohttp import ClientConnectorError
from loguru import logger

from bot.core.config import settings
from bot.handlers.functions import cancel_if_command

router = Router(name="review")
give_feedback_error_text = "Извините, в данный момент невозможно оставить отзыв."

class Form(StatesGroup):
    review = State()


@router.message(Command(commands=["review", "отзыв"]))
async def start_review(message: types.Message, state: FSMContext) -> None:
    """Запросить у пользователя отзыв"""
    await message.answer(_("Пожалуйста, напишите ваш отзыв о нашем сервисе."))
    await state.set_state(Form.review)


@router.message(Form.review)
async def receive_review(message: types.Message, state: FSMContext) -> None:
    """Получить и обработать отзыв от пользователя"""
    if await cancel_if_command(message, state):
        await message.answer(_("Добавление отзыва прервано."))
        return

    review = message.text  # Текст отзыва от пользователя

    # Получаем Telegram ID пользователя
    user_id = message.from_user.id

    # Получаем никнейм пользователя в Telegram
    username = message.from_user.username

    data = {"text": review, "created_by_customer_id": user_id}

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                    settings.PREFIX_GEN_BACKEND_URL
                    + f"review?customer_telegram_username={username}",
                    json=data,
                    headers={"Content-Type": "application/json", "accept": "application/json"},
            ) as response:
                if response.status == 201:
                    await message.answer(_("Спасибо за ваш отзыв!"))
                else:
                    await message.answer(
                        _(give_feedback_error_text)
                    )
    except ClientConnectorError:
        logger.error("The connection to the backend server could not be established.")
        await message.answer(_(give_feedback_error_text))
    except Exception as e:
        logger.error(f"An error has occurred: \n {e}")
        await message.answer(_(give_feedback_error_text))

    await state.clear()
