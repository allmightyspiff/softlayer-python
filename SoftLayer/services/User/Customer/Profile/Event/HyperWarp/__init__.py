# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_User_Customer_Profile_Event_HyperWarp(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_User_Customer_Profile_Event_HyperWarp'
        self.client = client

    def receiveEventDirect(
        self,
        eventJson: 'SoftLayer_Container_User_Customer_Profile_Event_HyperWarp_ProfileChange'
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'receiveEventDirect',
            eventJson
        )
        
        return data


