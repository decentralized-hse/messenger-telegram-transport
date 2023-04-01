# Messenger: Telegram transport

### Send and recieve messages with the usage of Telegram

#### Demo

CLI usage [demonstration](https://drive.google.com/file/d/1BOZ0Q28qOZJBzg_2m6cXyV22lATXVssZ/view?usp=sharing): sending and receiving messages. (The example's bot token has been revoked)

#### Usage: CLI with Python Script

1. Create bot using `@BotFather` and get its token
2. Create public dead drop channel and add the bot as an admin
3. Send a message using the `transport.py` script (No requirements needed!)

Example:
```
python .\transport.py send -t 0123456789:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX -n testchannelname -f Sender -c "This is the coolest test message!!!"
```

4. Read the message using the `transport.py` script

Example:
```
python .\transport.py read -n testchannelname
```

#### Usage: Kotlin library

You can integrate Kotlin classes `Message.kt` and `TelegramClient.kt` for the usage inside Android app
