import logging
from os import environ as env
from dotenv import load_dotenv

import telebot
import openai


logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

load_dotenv()
bot = telebot.TeleBot(env["BOT_API_KEY"])
openai.api_key = env["OPENAI_API_KEY"]
user_id = int(env["USER_KEY"])

@bot.message_handler(func=lambda message: True)
def get_codex(message):
  if int(message.chat.id) != user_id:
    bot.send_message("This is an only user bot. Please, to get it for your own go to //INCLUDE GITHUB")
  else:
    response = openai.Completion.create(
     #engine = "text-davinci-003",
      engine = "text-davinci-001",
     #engine = "text-curie-001",
     #engine = "text-babbage-001",
     #engine = "text-ada-001",
     #engine = "code-davinci-002",
     #engine = "code-cushman-001",
      prompt = '"""\n{}\n"""'.format(message.text),
      temperature = 0,
      max_tokens = 1200,
      top_p = 1,
      frequency_penalty = 0,
      presence_penalty = 0,
      stop = ['"""'])

    bot.send_message(message.chat.id, f'```\n{response["choices"][0]["text"]}\n```', parse_mode="Markdown")

bot.infinity_polling()