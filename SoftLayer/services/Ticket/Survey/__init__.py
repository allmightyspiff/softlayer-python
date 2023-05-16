# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Ticket_Survey(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Ticket_Survey'
        self.client = client

    def getPreference(
        self,
        
    ) -> 'void':

        data = self.client.call(
            self.service,
            'getPreference',
            
        )
        
        return data


    def optIn(
        self,
        
    ) -> 'void':

        data = self.client.call(
            self.service,
            'optIn',
            
        )
        
        return data


    def optOut(
        self,
        
    ) -> 'void':

        data = self.client.call(
            self.service,
            'optOut',
            
        )
        
        return data


