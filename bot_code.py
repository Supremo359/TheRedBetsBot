import telebot
import requests

API_KEY = 'YOUR_BOT_API_KEY'
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the Football Predictions Bot! Use /prognoza for today's predictions.")

@bot.message_handler(commands=['prognoza'])
def send_predictions(message):
    # Тук добавяш логиката, която извлича прогнозите от машината или API
    predictions = "Today's predictions:\nBarcelona vs Real Sociedad: 1 & Over 2.5\nFenerbahce vs Besiktas: GG & Over 2.5"
    bot.reply_to(message, predictions)

bot.polling()
