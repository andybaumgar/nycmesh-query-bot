import logging
import os
import re

from dotenv import load_dotenv
import pyjokes
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from utils.message_process import get_install_number_from_message 
import config

load_dotenv()

app = App(token=os.environ["SLACK_USER_TOKEN"], name="Query Bot")
logger = logging.getLogger(__name__)

result = app.client.search_messages(query=config.query)

messages = result._initial_data['messages']
message_contents = [x['text'] for x in messages['matches']]

install_numbers = [get_install_number_from_message(x, asap=config.asap) for x in message_contents]
install_numbers_no_none = [x for x in install_numbers if x is not None]
install_number_strings = [str(x) for x in install_numbers_no_none] 

numbers_list_url = '-'.join(install_number_strings)

map_url = config.map_url_base + numbers_list_url

print (map_url)

def main():
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()

    


# if __name__ == "__main__":
#     main()
