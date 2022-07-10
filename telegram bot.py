
from aiogram import Bot,Dispatcher,executor,types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup



bot = Bot(token="5310357509:AAGg0zuRAofatxRDpfCYec5rqa4XMTpjLuU")
dp = Dispatcher(bot)


button1 = InlineKeyboardButton(text = 'Volunteer', callback_data = 'v')
button2 = InlineKeyboardButton(text = 'Beneficiary', callback_data = 'b')
button3 = InlineKeyboardButton(text = 'Help/info',callback_data = 'h')
keyboard_inline = InlineKeyboardMarkup().add(button1,button2,button3)

button4 = InlineKeyboardButton(text = 'Disabled', callback_data = 'd')
button5 = InlineKeyboardButton(text = 'Elderly', callback_data = 'e')
button6 = InlineKeyboardButton(text = 'Children', callback_data = 'c')
# button7 = InlineKeyboardButton(text = 'Others', callback_data = 'o')
inline_keyboard_2 = InlineKeyboardMarkup().add(button4,button5,button6)

button8= InlineKeyboardButton(text = 'Persons with disabilities', callback_data = 'disabled')
button9 = InlineKeyboardButton(text = 'Assisting the elderly', callback_data = 'elderly')
button10= InlineKeyboardButton(text = 'Helping / caring for children', callback_data = 'children')
inline_keyboard_3 = InlineKeyboardMarkup().add(button8,button9,button10)

@dp.message_handler(commands=['hello'])
async def hello_(message:types.Message):
    await message.reply(f"Hello, welcome to enigma bot");



@dp.message_handler(commands = ['start'])
async def start_(message: types.Message):
    await message.reply('Choose a category you belong to: ', reply_markup=keyboard_inline)




@dp.callback_query_handler(text = ['v','b','h'])
async def response(call: types.CallbackQuery):
    if call.data == 'v':
        await call.message.reply('Choose a group to help: ', reply_markup=inline_keyboard_2);

    elif call.data == 'b':
        await call.message.answer('What kind of help do you need? ',reply_markup = inline_keyboard_3);



#list of NGOs that volunteers can help based on the category they chose
@dp.callback_query_handler(text = ['d','e','c'])
async def volunteer(call: types.CallbackQuery):
    if call.data == 'd':
        await call.message.reply("List of NGOs for disabled persons :\n\n 1:  'https://www.dpa.org.sg/how-you-can-help/be-a-volunteer/'\n\n2: 'https://www.minds.org.sg/volunteer/' ");


    elif call.data == 'e':
        await call.message.answer(f" List of NGOs for elderly:{'https://thesmartlocal.com/read/volunteering-old-folks/'}");

    elif call.data == 'c':
        await call.message.reply('List of NGOs for children: \n\n 1: https://www.wishingwell.org.sg/volunteer/\n\n 2:https://www.msf.gov.sg/Fostering/Pages/Volunteer-with-Us.aspx \n\n 3.https://www.kidstart.sg/for-volunteers/');




#beneficiaries can be matched up to an organisation which suits their needs
@dp.callback_query_handler(text = ['disabled','elderly','children'])
async def beneficiary(call:types.CallbackQuery):
    if call.data == 'disabled':
        await call.message.reply("Connecting you to an organisation for the disabled...... \n\n https://www.dpa.org.sg/contact-us/")

    elif call.data =='elderly':
        await call.message.reply("Connecting you to an organisation for the elderly...... \n\n https://cef.org.sg/")

    elif call.data =='children':
        await call.message.reply("Connecting you to an organisation for the children...... \n\nhttps://www.touch.org.sg")
executor.start_polling(dp)



