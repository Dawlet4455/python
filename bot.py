from aiogram import types,executor,Bot,Dispatcher
from req import send_answer

api = '7099426374:AAGIssHou9TGoJCZ7hUAoF0PcrHE6T-Xn_I'
bot = Bot(api)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_hi(message:types.Message):
    await message.answer('Biz ge siz qalegen sorawlardi jibering')


@dp.message_handler()
async def save(message:types.Message):
    answer = await send_answer(message.text)
    await message.answer(answer)

if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True)