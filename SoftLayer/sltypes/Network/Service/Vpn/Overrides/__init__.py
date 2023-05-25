from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Service_Vpn_Overrides(Entity):
    """The SoftLayer_Network_Service_Vpn_Overrides data type contains information relating user ids to subnet ids
when VPN access is manually configured.  It is essentially an entry in a 'white list' of subnets a SoftLayer
portal VPN user may access."""
    id_: int
    subnetId: int
    userId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Service_Vpn_Overrides'

    def createObjects(self, templateObjects: 'Network_Service_Vpn_Overrides') -> bool:
        """Create Softlayer portal user VPN overrides."""
        data = self.client.call('SoftLayer_Network_Service_Vpn_Overrides', 'createObjects', templateObjects)
        return data

    def deleteObject(self, identifier: int) -> bool:
        """Delete single override."""
        data = self.client.call('SoftLayer_Network_Service_Vpn_Overrides', 'deleteObject', id=identifier)
        return data

    def deleteObjects(self, templateObjects: 'Network_Service_Vpn_Overrides') -> bool:
        """Delete multiple entries in the overrides 'white list' for a SoftLayer portal VPN user."""
        data = self.client.call('SoftLayer_Network_Service_Vpn_Overrides', 'deleteObjects', templateObjects)
        return data

    def getObject(self, identifier: int) -> 'Network_Service_Vpn_Overrides':
        """Retrieve a SoftLayer_Network_Service_Vpn_Overrides record."""
        data = self.client.call('SoftLayer_Network_Service_Vpn_Overrides', 'getObject', id=identifier)
        from SoftLayer.sltypes.Network_Service_Vpn_Overrides import Network_Service_Vpn_Overrides
        return data

    def getSubnet(self, identifier: int) -> 'Network_Subnet':
        """"""
        data = self.client.call('SoftLayer_Network_Service_Vpn_Overrides', 'getSubnet', id=identifier)
        from SoftLayer.sltypes.Network_Subnet import Network_Subnet
        return data

    def getUser(self, identifier: int) -> 'User_Customer':
        """"""
        data = self.client.call('SoftLayer_Network_Service_Vpn_Overrides', 'getUser', id=identifier)
        from SoftLayer.sltypes.User_Customer import User_Customer
        return data
