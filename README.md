# GPT Telegram Bot
Script for a Telegram bot that uses [OpenAI API](https://beta.openai.com/overview) similar to ChatGPT. It has all its capabilities plus the fact that by using the API directly, there is no waiting time prior to using this bot. The current downside to this project is that the script has to be running for the bot to work. _Anyone willing to contribute to this project in anyway, particularly by making it work forever, please visit the [Contribution](#contribution) section._

## Features
- [ ] Use OpenAI API through Telegram
- [ ] Get text replies by default
- [ ] Get code responses by starting your messages with `>>>`
- [ ] Get code related answers by using the word `code` in your meessage
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

### 3. Create an OpenAI account
If you do not already have an account, create one at [OpenAI website](https://beta.openai.com/signup).

### 4. Gather your keys
Once you have your Telegram and OpenAI accounts, gather the keys.

**OpenAI API key:**
1. Log-in in [OpenAI keys](https://beta.openai.com/account/api-keys)
2. Create a new secret key and copy it to the clipboard. This is your **OPENAI_API_KEY**. It should look like this: `xx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`
3. Paste it in your .env file in the field **OPENAI_API_KEY**
4. Set!
_Be aware that you will be using your own OpenAI credit so charges might be applied._

**Telegram Bot key:**
1. Open Telegram in any of your devices
2. Open a chat with [@BotFather](https://web.telegram.org/k/#@BotFather). It is your go-to for all things bot, from creation to settings
3. Type `/newbot` to begin. The BotFather will ask you to pick a bot name (which must be universally unique) and a username, it then generates an authentication token for your new bot. This token is your **BOT_API_KEY**. It should look like this: `0123456789:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`
4. Paste it in your .env file in the field **BOT_API_KEY**
5. Done!

**Telegram user key:**
1. Head back to Telegram and open a chat with [@userinfobot](https://web.telegram.org/k/#@userinfobot)
2. Type `/start` to begin. It will reply with your info.
3. Copy the ID, that should look like this: `0123456789`
4. Paste it in your .env file in the field **USER_KEY**
5. Nice! This way only you can talk with the bot.
_Notice that if you would like the bot to reply to many people you should modify the code to stop rejecting other peoples' messages._

Make sure your .env file has the three KEYs obtained during this step. Save the file. It might dissapear but it is still there.

### 5. Decide which engine suits you
The script is intended to be used for natural and code responses, if either the message starts with `>>>` or contains `code` or `python` keywords. If you are willing to use other engine rather than the ones included, just change it by the one that suits you. Not sure on which engine suits you? Check the official website to see what each model offers [here](https://beta.openai.com/docs/models/overview).

### 6. Run the script
Now you can use the bot as long as the script is running. Just type Hello! and make sure it responds.

## Contribution
> Notice that this section is not precise, as I am not a senior developer and I neither have in depth knowledge on the Telegram API nor python packages that might be usefull to make the bot better, but I believe that some changes are needed to reach the full potential of this script.

I encourage anyone with knowledge on the topic to help me in any way considered appropiate. If any bug, failure or error is detected, feel free to communicate or try to solve it. Here is a list of features I believe that should be worked on in order to improve the repository, but suggestions are as well accepted:
- Make the script run forever
- Enable through chat command to modify the engine used for the response

## Credits
- Creator [@juan-miii](https://github.com/juan-miii) (GitHub), [@juanmiiix](https://twitter.com/juanmiiix) on Twitter
- Contributor [@han3on](https://github.com/han3on) (GitHub)
- Based on [@browneye1826](https://gist.github.com/browneye1826)'s Gists on a [_Telegram bot to communicate with Codex by OpenAI_](https://gist.github.com/browneye1826/4890211188170a43087dfc586afc962b#file-codex_bot-py)
