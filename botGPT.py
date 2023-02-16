# Telegram Bot to communicate with OpenAI API
# forked from juan-miii, modified by han3on

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
def get_response(message):
  if int(message.chat.id) != user_id:
    bot.send_message("This boti not for public but private use only.")
  else:
    response = ""
    if message.text.startswith(">>>"):
      # Use Codex API for code completion
      response = openai.Completion.create(
        engine="code-davinci-002",
        prompt=f'```\n{message.text[3:]}\n```',
        temperature=0,
        max_tokens=8000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\n", ">>>"],
      )
    else:
      # Use GPT API for text completion
      response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f'"""\n{message.text}\n"""',
        temperature=0,
        max_tokens=4000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=['"""'],
      )

    bot.send_message(message.chat.id, f'{response["choices"][0]["text"]}', parse_mode="None")

bot.infinity_polling()
