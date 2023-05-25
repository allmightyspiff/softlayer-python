from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Utility_Network(Entity):
    pass

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Utility_Network'

    def nsLookup(self, address: str, type_: str) -> str:
        """Perform a nameserver lookup on given address."""
        data = self.client.call('SoftLayer_Utility_Network', 'nsLookup', address, type)
        return data

    def whois(self, address: str) -> str:
        """Perform a WHOIS lookup on a given address."""
        data = self.client.call('SoftLayer_Utility_Network', 'whois', address)
        return data
