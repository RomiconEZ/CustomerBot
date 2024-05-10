from aiogram import Router, types
from aiogram.filters import Command
from aiogram.utils.i18n import gettext as _

from bot.core.config import settings

router = Router(name="info")


@router.message(Command(commands=["info", "about"]))
async def info_handler(message: types.Message) -> None:
    """Information about bot."""
    await message.answer(
        _(
            f"Я ваш личный ассистент-бот {settings.COMPANY_NAME}. Я доступен 24/7 и готов ответить на все ваши "
            "вопросы о наших турах, услугах и акциях."
        )
    )
