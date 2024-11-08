import telebot
from main_bot import main
TOKEN = "5936779941:AAHeKFFMa6hhjXEkNQ_5hT5pUJPWwPqdUcY"

bot = telebot.TeleBot(token=TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! Use a command with a team name to get information about that team. For example, type /Everton to get information about Everton.")

@bot.message_handler(commands=['.*'])
def run_main_with_regex_command(message):
    print(message)
    command = message.text.split()[0][1:]
    try:
        main_output = main(command)
        bot.reply_to(message, main_output)
    except telebot.apihelper.ApiTelegramException as e:
        if 'message text is empty' in str(e):
            bot.reply_to(message, "Sorry, I cannot do it for this game.")
        else:
            raise e

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    text = main(message.text[1:])
    bot.reply_to(message, text)

bot.infinity_polling()