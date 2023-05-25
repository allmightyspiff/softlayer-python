from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Monitor(Entity):
    pass

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Monitor'

    def getIpAddressesByHardware(self, hardware: 'Hardware', partialIpAddress: str) -> list['Network_Subnet_IpAddress']:
        """Returns an ArrayObject of subnet ip address objects for a hardware"""
        data = self.client.call('SoftLayer_Network_Monitor', 'getIpAddressesByHardware', hardware, partialIpAddress)
        from SoftLayer.sltypes.Network_Subnet_IpAddress import Network_Subnet_IpAddress
        return data

    def getIpAddressesByVirtualGuest(self, guest: 'Virtual_Guest', partialIpAddress: str) -> list['Network_Subnet_IpAddress']:
        """Returns an ArrayObject of subnet ip address objects for a guest resource."""
        data = self.client.call('SoftLayer_Network_Monitor', 'getIpAddressesByVirtualGuest', guest, partialIpAddress)
        from SoftLayer.sltypes.Network_Subnet_IpAddress import Network_Subnet_IpAddress
        return data
