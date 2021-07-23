import telebot
import datetime
# from telebot import types
bot = telebot.TeleBot("1640805626:AAF9_CSGSagtrHWQmdxUgtzt4oTrafEsQn4")

@bot.message_handler(commands=['start'])
def mes(message):
    i = 0
    while i <= 10:
        # bot.send_message(chat_id='@dfddfffdfddddfddddd',text="Testing "+str(i))
        bot.send_message(chat_id="@dfddfffdfddddfddddd",text="Current date and time: "+ str(datetime.datetime.now()))
        i=i+1

@bot.message_handler(commands=['promos'])
def promote(message):
    id = message.text.split()
    bot.promote_chat_member(message.chat.id,id[1],can_change_info=True,can_delete_messages=True,can_invite_users=True,can_restrict_members=True,can_pin_messages=True,can_promote_members=True)

@bot.message_handler(commands=['my_id'])
def send_id(message):
    bot.send_message(message.chat.id,"Your id: "+str(message.from_user.id))
bot.polling()