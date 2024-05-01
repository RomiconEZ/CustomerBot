from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.utils.i18n import gettext as _

from bot.keyboards.inline.menu import main_keyboard
from bot.services.analytics import analytics

router = Router(name="start")


@router.message(CommandStart())
async def start_handler(message: types.Message) -> None:
    """Welcome message."""
    await message.answer(
        _(
            "Согласие на обработку персональных данных "
            "[эл.ссылка](https://drive.google.com/file/d/1XvQ70zT57PHz5ixdajFjo95KRNa6Eqbf/view?usp=sharing). "
            "Спасибо, что выбрали нашу Турфирму! Я ваш личный ассистент и с удовольствием помогу вам "
            "выбрать и приобрести тур."
        ),
        reply_markup=main_keyboard(),
        parse_mode="Markdown",
    )
