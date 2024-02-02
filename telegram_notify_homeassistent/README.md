# Telegram Unread Message Notifier for Home Assistant

This Python script utilizes the Telethon library to check for unread messages on Telegram and updates a specified Home Assistant entity with the total unread message count.

## Prerequisites

- Python 3.6 or higher
- Home Assistant instance

## Setup

1. Install required Python libraries:

   ```bash
   pip3 install -r requirements.txt
   ```
2. Rename config_exmaple.py to config.py
3. fill config.py
4. first run in terminal and follow instruction

```
python3 tlg_check_messages_count.py
```
5. add to cron or systemd

run every one minute
```
* * * * * python3 /path/to/your/tlg_check_messages_count.py > /dev/null
```
