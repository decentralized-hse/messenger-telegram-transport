# Messenger: Telegram transport

### Send and recieve messages with the usage of Telegram

TODO:

- Kotlin classes
- Demo

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
python .\testbot.py read -n testchannelname
```

#### Usage: Kotlin library

TODO