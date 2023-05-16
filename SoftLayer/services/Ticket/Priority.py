# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Ticket_Priority(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Ticket_Priority'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def getPriorities(
        self,
        
    ) -> 'list[SoftLayer_Container_Ticket_Priority]':
        data = self.client.call(
            self.service,
            'getPriorities',
            
        )
        from SoftLayer.datatypes.Container.Ticket.Priority import Priority
        return SL_Priority(data)


