import telebot
from subprocess import check_output

# Ваш токен бота Telegram
bot_token = '6420347331:AAGUAJmjWu19KgLa8lfhofOVQmuEUDWaEm4'

# Айді користувача, якому дозволено керувати systemd
allowed_user_id = 6316376597

# Ім'я служби, якою ви хочете керувати
service_name = 'acbot'

# Ініціалізація бота
bot = telebot.TeleBot(bot_token)

# Обробник команди /status
@bot.message_handler(commands=['status'])
def get_status(message):
    if message.from_user.id == allowed_user_id:
        status = check_output(['systemctl', 'status', service_name]).decode('utf-8')
        bot.reply_to(message, status)
    else:
        bot.reply_to(message, "Ви не маєте дозволу використовувати цю команду.")

# Обробник команди /restart
@bot.message_handler(commands=['restart'])
def restart_service(message):
    if message.from_user.id == allowed_user_id:
        result = check_output(['sudo', 'systemctl', 'restart', service_name]).decode('utf-8')
        bot.reply_to(message, f"Службу {service_name} успішно перезавантажено.")
    else:
        bot.reply_to(message, "Ви не маєте дозволу використовувати цю команду.")

# Обробник команди /logs
@bot.message_handler(commands=['logs'])
def get_logs(message):
    if message.from_user.id == allowed_user_id:
        logs = check_output(['sudo', 'journalctl', '-u', service_name, '--no-pager']).decode('utf-8')
        with open(f'{service_name}_logs.txt', 'w') as file:
            file.write(logs)
        with open(f'{service_name}_logs.txt', 'rb') as file:
            bot.send_document(message.chat.id, file)
    else:
        bot.reply_to(message, "Ви не маєте дозволу використовувати цю команду.")

# Запуск бота
bot.polling()
