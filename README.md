# message-collect
Collect (nearly) every message in a discord channel using a self-bot.

# Note:
Automating user accounts is against the Discord ToS. This script is for educational purposes only and I cannot recommend using it. Do so at your own risk.
This script uses the [discord.py-self](https://github.com/dolfies/discord.py-self) library.

# Usage:
This script is meant to collect every message in a discord channel using a discord self-bot and filter out certain messages:
- Messages from bots
- Messages with files
- Messages with embedded attachments such as gifs
The script is also meant to remove user, channel, role mentions and custom emojis (meaning that a message that is only a user mention - say for example `<@1111121289>` - will be returned empty)

- Replace `CHANNEL_ID_HERE` and `GUILD_ID_HERE` with your own id's.
- Replace `FILE_NAME` with your desired file name.
- Replace `TOKEN` with your own discord user token. If you don't know how to get it, you can find out [here.](https://gist.github.com/MarvNC/e601f3603df22f36ebd3102c501116c6)
