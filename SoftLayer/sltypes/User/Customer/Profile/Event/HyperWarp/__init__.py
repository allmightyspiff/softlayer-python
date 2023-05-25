from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class User_Customer_Profile_Event_HyperWarp(Entity):
    pass

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_User_Customer_Profile_Event_HyperWarp'

    def receiveEventDirect(self, eventJson: 'Container_User_Customer_Profile_Event_HyperWarp_ProfileChange') -> bool:
        """Modifies linked Paas user data based on changes initiated by Bluemix."""
        data = self.client.call('SoftLayer_User_Customer_Profile_Event_HyperWarp', 'receiveEventDirect', eventJson)
        return data
