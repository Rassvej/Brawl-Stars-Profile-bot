import telebot
import brawlstats

# Specify the token of your Telegram bot
telegram_token = '6996247665:AAHnZAfS3Qq44PwNyU7CH6EbACenbhSksxY'
# Specify the Brawl Stars API token (available on the website https://developer.brawlstars.com )
brawlstars_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjAxYTlmNmFhLTc4OWUtNDQ0My1iZDkzLWRiNjNhMGUwMTUxMiIsImlhdCI6MTcxNTE4MzgwNCwic3ViIjoiZGV2ZWxvcGVyLzljOGE2MDVjLWY2NGYtNTg1My1lNjQ0LTU4ZDFmNjQwOGJkZCIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiOTQuMjM3LjgzLjEzOSJdLCJ0eXBlIjoiY2xpZW50In1dfQ.Vawuy0F7N90tEgvPuqUymrjThAOVN0pi_vhHL-SHfw6Nj0IMttH32v1Tvxd9ZwPPlgROZkIG4WkMDMoxR1E0yg'

# Creating a client object Brawl Stars
client = brawlstats.Client(brawlstats_token)
# Creating a bot object
bot = telebot.TeleBot(telegram_token)

# Command handler /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Для просмотра статистики профилей в Brawl Stars используйте внутриигровой #ТЭГ игрока.")

# Text message handler
@bot.message_handler(func=lambda message: True)
def handle_message(message):
# We receive the text of the message from the user
    text = message.text.strip()
# Check if the text of the message is a player tag
    if text.startswith("#"):
# Extract the player tag
        player_tag = text[1:]
        try:
            # We get the player's profile data by his tag
            player = client.get_player(player_tag)
            # We form a reply message with the player's profile data
            response = f"Никнейм: {player.name }\Тэг: #{player.tag}\Трофеи: {player.trophies}\Рекорд трофеев: {player.highest_trophies}\Уровень: {player.exp_level}"
# Sending a reply message to the user
            bot.reply_to(message, response)
        except brawlstats.NotFoundError:
            # In case of an error, we send an error message
            bot.reply_to(message, "Такого тэга не сущевствует, перепроверьте.")
except Exception as e:
            # In case of other errors, we send an error message
            bot.reply_to(message, f"ОШИБКА: {str(e)}")
else:
# If the message does not contain a player tag, we send a hint
        bot.reply_to(message, "Для просмотра статистики игрока. Введите тэг начиная с #.")

# Launching the bot
bot.polling()
