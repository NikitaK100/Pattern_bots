from aiogram import executor



async def on_startup(dp):
    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)


if __name__ == '__main__':
    from handlers import dp
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
