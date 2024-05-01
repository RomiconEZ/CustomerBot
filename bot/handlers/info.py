from aiogram import Router, types
from aiogram.filters import Command
from aiogram.utils.i18n import gettext as _

router = Router(name="info")


@router.message(Command(commands=["info", "about"]))
async def info_handler(message: types.Message) -> None:
    """Information about bot."""
    await message.answer(
        _(
            "Я ваш личный ассистент-бот KareliaTour. Я доступен 24/7 и готов ответить на все ваши "
            "вопросы о наших турах, услугах и акциях."
        )
    )
