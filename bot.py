from aiogram import Bot, Dispatcher
from aiogram.utils import executor

TOKEN = '7375215343:AAGI-R0d5I_UfGFBf_Wi_X41aEYPqnQcxA4'  # O'z bot tokeningizni bu yerga qo'shing
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_handler(message):
    await message.answer("Salom! Instagram yoki TikTok linkini yuboring.")

@dp.message_handler()
async def download_media(message):
    url = message.text
    await message.answer("Yuklanmoqda, iltimos kuting...")
    ydl_opts = {'format': 'best'}
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        await message.answer("Media muvaffaqiyatli yuklandi!")
    except Exception as e:
        await message.answer(f"Xatolik: {str(e)}")

if __name__ == '__main__':
    executor.start_polling(dp)
