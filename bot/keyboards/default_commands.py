from __future__ import annotations

from typing import TYPE_CHECKING

from aiogram.types import BotCommand, BotCommandScopeDefault

if TYPE_CHECKING:
    from aiogram import Bot

users_commands: dict[str, dict[str, str]] = {
    "en": {
        "info": "info about bot",
        "supports": "support contacts",
        "new_chat": "create new chat",
        "review": "give feedback",
    },
    "uk": {
        "info": "info about bot",
        "supports": "support contacts",
        "new_chat": "create new chat",
        "review": "give feedback",
    },
    "ru": {
        "info": "информация о боте",
        "supports": "вызов оператора",
        "new_chat": "создать новый чат",
        "review": "оставить отзыв",
    },
}

admins_commands: dict[str, dict[str, str]] = {
    **users_commands,
    "en": {
        "ping": "Check bot ping",
        "stats": "Show bot stats",
    },
    "uk": {
        "ping": "Check bot ping",
        "stats": "Show bot stats",
    },
    "ru": {
        "ping": "Check bot ping",
        "stats": "Show bot stats",
    },
}


async def set_default_commands(bot: Bot) -> None:
    await remove_default_commands(bot)

    for language_code in users_commands:
        await bot.set_my_commands(
            [
                BotCommand(command=command, description=description)
                for command, description in users_commands[language_code].items()
            ],
            scope=BotCommandScopeDefault(),
        )

        """ Commands for admins
        for admin_id in await admin_ids():
            await bot.set_my_commands(
                [
                    BotCommand(command=command, description=description)
                    for command, description in admins_commands[language_code].items()
                ],
                scope=BotCommandScopeChat(chat_id=admin_id),
            )
        """


async def remove_default_commands(bot: Bot) -> None:
    await bot.delete_my_commands(scope=BotCommandScopeDefault())
