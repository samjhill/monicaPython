"""
@author: Shahzeb Afroze

We will put functions to help us clean the data concerning gmail

"""
import re
import time
import pandas as pd
from datetime import datetime
from social.gmail_preprocessing import Preprocessing
from social.utils import Utils
from pprint import pprint

# import sys
# sys.path.append('..')

from monica.conversations import Conversations
from monica.contact_field_types import Contact_Field_Types


class Gmail_Monica_Client:
    def __init__(self, access_token, wait_time=0.2):
        """
        Preparing gmail data for monica conversations

        Parameters:
        -----------

        """

        self.conversations = Conversations(
            access_token=access_token, wait_time=wait_time
        )
        self.contact_field_types = Contact_Field_Types(access_token=access_token)

    def upload_emails_to_monica(self, df_preprocessed):
        conversations = self.conversations
        contact_field_types = self.contact_field_types

        df_preprocessed = df_preprocessed[
            df_preprocessed["contact_id"] != ""
        ]  # remove contacts which are not on monica
        df_preprocessed = df_preprocessed[
            ~df_preprocessed["key"].isna()
        ]  # remove nan for subjects

        contact_field_type_id = contact_field_types.get_contact_field_type_id("Email")

        unique_keys = list(df_preprocessed["key"].unique())
        # unique_keys = [x for x in unique_keys if str(x) == 'permission432610'] # testing

        for key in unique_keys:
            print(key)
            print()
            subset = df_preprocessed[df_preprocessed["key"] == key]
            subset.sort_values(by="date_time", inplace=True)
            contact_id = subset["contact_id"].values[0]
            happened_at = subset["date"].values[0]  # started conv
            conversation_id = conversations.create_conversation_object(
                happened_at=happened_at,
                contact_field_type_id=contact_field_type_id,
                contact_id=contact_id,
            )
            conversations.add_multiple_messages(
                contact_id=contact_id, conversation_id=conversation_id, df=subset
            )
