"""
@author: Sam Hill

Offical Documentation: https://www.monicahq.com/api/journal

Description: We will put all journal related requests here


"""

import time
import requests
import json
from .utils import Utils
from pprint import pprint
import pandas as pd

basic_api = "https://app.monicahq.com/api"


class Journal:
    def __init__(self, access_token, wait_time=1):
        """
        Connect with monica journals API found at https://www.monicahq.com/api/journal

        Parameters:
        -----------
                access_token: str
                        token retreived from monica platform

                wait_time: int
                        seconds to wait after every request sent

        """
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-type": "application/json",
            "Accept": "text/plain",
        }

        self.headers = headers
        self.basic_api = basic_api
        self.wait_time = wait_time
        self.utils = Utils()

    def list_journal(self):
        """
        Gets the journal entries from monica. Checkout monica API documentation for detailed description.

        Parameters: None
        -----------


        Returns:
        -------
        json_data: dict/json
                can be easily converted to pandas dataframe

        """
        headers = self.headers
        wait_time = self.wait_time
        basic_api = self.basic_api

        api = f"{basic_api}/journal"

        response = requests.get(api, headers=headers)
        print(response)

        json_data = response.json()

        return json_data
    
    
    def update_journal_entry(self, title, content, journal_entry_id):
        headers = self.headers
        wait_time = self.wait_time
        basic_api = self.basic_api

        api = f"{basic_api}/journal/{journal_entry_id}"
        payload = {"title": title, "post": content}
        response = requests.put(api, json=payload, headers=headers)
        print(response)

        json_data = response.json()

        return json_data