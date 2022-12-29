# GPT Telegram Bot
Script for a Telegram bot that uses [OpenAI API](https://beta.openai.com/overview) similar to ChatGPT. It has all its capabilities plus the fact that by using the API directly, there is no waiting time prior to using this bot. The current downside to this project is that the script has to be running for the bot to work. _Anyone willing to contribute to this project in anyway, particularly by making it work forever, please visit the [Contibution](#contribution) section._

## Features
- [ ] Chat with GTP using Telegram
- [ ] Choose between different OpenAI engines
- [ ] Make your bot private for personal use

## How to install

### 1. Install Python

Get Python installed in the most recent version together with the following packages:

```
pip install openai
pip install pyTelegramBotAPI
pip install python-dotenv
```

### 2. Install Telegram

If you do not already have Telegram in any device or web browser, create an account as it is needed.

### 3. Gather your keys

Once you have your

Fill-in your .env file with the KEYs obtained during this step.

## Contribution
> Notice that this section is not precise, as I am not completely sure on how to run the script forever, but I only know that it should be done.

The bot can now only work if the script is running, but for an ideal implementation, the bot should work on demand at any time given. I encourage anyone with knowledge on the topic to help me, by using pull requests or in any way considered appropiate. If any bug, failure or error is detected, feel free to comunicate or try to solve it.

## Credits
- Creator [@juan-miii](https://github.com/juan-miii)
- Based on [@browneye1826](https://gist.github.com/browneye1826)'s Gists on a [_Telegram bot to communicate with Codex by OpenAI_](https://gist.github.com/browneye1826/4890211188170a43087dfc586afc962b#file-codex_bot-py)