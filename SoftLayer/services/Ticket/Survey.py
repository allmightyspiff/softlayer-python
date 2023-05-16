# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Ticket_Survey(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Ticket_Survey'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def getPreference(
        self,
        
    ) -> 'void':
        data = self.client.call(
            self.service,
            'getPreference',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def optIn(
        self,
        
    ) -> 'void':
        data = self.client.call(
            self.service,
            'optIn',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def optOut(
        self,
        
    ) -> 'void':
        data = self.client.call(
            self.service,
            'optOut',
            
        )
        
        return data


