import logging
import os

from dotenv import load_dotenv
from slack_bolt import App
from querybot.utils.message_process import get_install_number_from_message 
import querybot.config as config

load_dotenv()

def get_install_team_map():

    app = App(token=os.environ["SLACK_USER_TOKEN"], name="Query Bot")
    logger = logging.getLogger(__name__)

    search_result = app.client.search_messages(query=config.query)

    messages = search_result._initial_data['messages']
    messages_contents = [x['text'] for x in messages['matches']]

    install_numbers = [get_install_number_from_message(x, asap=config.asap) for x in messages_contents]
    install_numbers_no_none = [x for x in install_numbers if x is not None]
    install_number_strings = [str(x) for x in install_numbers_no_none] 

    numbers_list_url = '-'.join(install_number_strings)

    map_url = config.map_url_base + numbers_list_url

    return map_url