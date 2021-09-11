from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.utils import executor
from asyncio import sleep

TOKEN = "1889170052:AAGXusk_9GQSq03VVOTs1-Z43DCfu76kRhk"

bot = Bot(token=TOKEN, parse_mode="html")
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    keys = ReplyKeyboardMarkup(resize_keyboard=True)
    key1 = KeyboardButton(text="Понеділок")
    key2 = KeyboardButton(text="Вівторок")
    key3 = KeyboardButton(text="Середа")
    key4 = KeyboardButton(text="Четверг")
    key5 = KeyboardButton(text="П'ятниця")
    keys.add(key1, key2)
    keys.add(key3, key4)
    keys. add(key5)
    await bot.send_message(message.chat.id, "💥Розклад уроків:",reply_markup=keys)
    
@dp.message_handler()
async def rsur(message: types.Message):
    if message.text=="Понеділок":
        await bot.send_message(message.chat.id, """1. Трудове🏗️
2. Трудове🏗️
3. Укр. Мова🚀
4. Фізика⚙️
5. Алгебра🔢
6. Біологія💩
7. Зарубіжна🌏""")
    elif message.text=="Вівторок":
        await bot.send_message(message.chat.id, """1. Анг. Мова🔡
2. Хімія💩
3. Укр. Літ⭐
4. Вс. Історія🌎
5. Геометрія🔢
6. Фізра🏃‍♂️
7. Інформатика💻""")
    elif message.text=="Середа":
        await bot.send_message(message.chat.id, """1. Географія🗺️
2. Укр. Мова⭐
3. Фізика⚙️
4. Англ. Мова🔡
5. Алгебра🔢
6. Біологія💩
7. Фізра🏃‍♂️""")
    elif message.text=="Четверг":
        await bot.send_message(message.chat.id, """1. Історія
2. Геометрія🔢
3. Інфа/Креслення💻
4. Хімія💩
5. Фізра🏃‍♂️
6. Географія🗺️""")
    elif message.text=="П'ятниця":
        await bot.send_message(message.chat.id, "Розклад")

@dp.message_handler(commands=['dm',"удалить"], commands_prefix="!")
async def delete_message(message: types.Message):
    await message.delete.message(message.chat.id, message.reply_to_message.from_user.id)
    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
