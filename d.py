import os
import requests
import snapsave_downloader
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor
import asyncio

API_TOKEN = 'token'  # Замените на ваш токен

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

# Словарь для хранения состояния каждого пользователя
user_state = {}

async def download_video(url):
    try:
        # Отправляем GET-запрос для скачивания видео
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            video_content = response.content
            return video_content
        else:
            print("Не удалось скачать видео. HTTP статус:", response.status_code)
            return None
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Отправьте мне ссылку на видео с Facebook, и я отправлю вам видео напрямую!")

@dp.message_handler(lambda message: message.text.startswith("http"))
async def handle_video_url(message: types.Message):
    user_id = message.from_user.id
    
    # Проверяем, есть ли в состоянии пользователя флаг, который запрещает отправку новых ссылок
    if user_id in user_state and user_state[user_id] == "processing":
        await message.reply("Пожалуйста, подождите, пока я загружу первое видео.")
        return

    # Устанавливаем состояние пользователя как "обработка"
    user_state[user_id] = "processing"

    facebook_video_url = message.text
    await message.reply("Обрабатываю вашу ссылку...")

    print(f"Обработка ссылки на видео: {facebook_video_url}")
    download_url = snapsave_downloader.SnapSave(facebook_video_url)

    if download_url:
        print(f"Ссылка для скачивания: {download_url}")

        # Загружаем содержимое видео
        video_content = await download_video(download_url)
        
        if video_content:
            # Отправляем видео пользователю
            await bot.send_video(
                chat_id=message.chat.id,
                video=video_content,
                caption="Вот ваше видео!",
                parse_mode=ParseMode.MARKDOWN
            )
        else:
            await message.reply("Не удалось скачать видео.")
    else:
        await message.reply("Не удалось получить ссылку для скачивания. Проверьте ссылку и попробуйте снова позже.")

    # Завершаем обработку и сбрасываем состояние пользователя
    user_state[user_id] = "idle"

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

