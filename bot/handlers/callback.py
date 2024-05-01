from aiogram import F, Router, types

from bot.handlers.info import info_handler

router = Router(name="callback")


@router.callback_query(F.data.startswith("info"))
async def callback_query_handler(query: types.CallbackQuery):
    await info_handler(query.message)
