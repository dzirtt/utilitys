from telethon.sync import TelegramClient 
from telethon import functions, types
from datetime import datetime
from requests import post
import pprint, pytz, asyncio
import logging as log
import config as config

api_id = config.api_id
api_hash = config.api_hash
phone_number = config.phone_number
hass_api_token = config.hass_api_token
logFilePath = config.logFilePath
LogLevel = config.LogLevel
hass_url = config.hass_url
hass_item_id = config.hass_item_id

async def check_unread_messages():
    await client.start(phone_number)
    current_date = datetime.now(pytz.utc)
    
    try:
        unread_count_summary = 0
        async for dialog in client.iter_dialogs(limit=100,ignore_migrated=True):
            if dialog.is_user or dialog.is_group or dialog.is_channel:
                user = await client.get_entity(dialog.id)
                # Get full user information
                notify_settings = await client(functions.account.GetNotifySettingsRequest(user.id))
                
                if (not notify_settings.mute_until or notify_settings.mute_until.astimezone(pytz.utc) < current_date) and dialog.unread_count > 0:
                
                    user_title = user.title if hasattr(user, 'title') else f"{user.username}"
                    user_first_name  = user.first_name if hasattr(user, 'first_name') else ""
                    user_last_name = user.last_name if hasattr(user, 'last_name') else ""
                    
                    #print(f"{user_title}|{user_first_name}|{user_last_name}|{dialog.unread_count}")
                    unread_count_summary+=dialog.unread_count
                    #pprint.pprint(vars(user))
#                    print(f"Unread messages in {user.username}|{user.firstname}: {dialog.unread_count}")

        return unread_count_summary

    except Exception as e:
        print(f"Error: {e}")
        log.error(f'ERROR {e}')

    finally:
        await client.disconnect()
 
def initLogging():
    log.basicConfig(filename=logFilePath, format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S', level=log.getLevelName(LogLevel))
    
    # alose log to std out
    #all lines for debug
    log.getLogger().addHandler(log.StreamHandler())
    log.getLogger().setLevel(log.getLevelName(LogLevel))
    log.getLogger('telethon').setLevel(log.CRITICAL)

    #utility.clean_file(cfg._logfile)

def set_state_hass(item_name,state):
    headers = {"Authorization": f'Bearer {hass_api_token}', "content-type": "application/json"}
    data = {"state": f'{state}'}
    
    full_url = f'{hass_url}/states/{item_name}'
    
    response = post(full_url, headers=headers, json=data)
    log.debug(f'[{response.status_code}] send to hass:{full_url} item:{item_name} state:{state}')
    
if __name__ == '__main__':
    
    initLogging()
    
    client = TelegramClient('tlg_notify_hass', api_id, api_hash, base_logger=log.NullHandler())
    loop = asyncio.get_event_loop()
    unread_count_summary = loop.run_until_complete(check_unread_messages())
    
    set_state_hass(hass_item_id,unread_count_summary)
    log.info(f'unread count:{unread_count_summary}')
        
    exit(0)
    
