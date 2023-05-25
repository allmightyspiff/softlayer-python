from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Software_VirtualLicense(Entity):
    """SoftLayer_Software_VirtualLicense is the application class that handles a special type of Software License.
Most software licenses are licensed to a specific hardware ID;  virtual licenses are designed for virtual
machines and therefore are assigned to an IP Address.  Not all software packages can be "virtual licensed"."""
    accountId: int
    hostHardwareId: int
    id_: int
    ipAddress: str
    key: str
    notes: str
    softwareDescriptionId: int
    subnetId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Software_VirtualLicense'

    def getLicenseFile(self, identifier: int) -> str:
        """Get the file for a virtual license, if it exists"""
        data = self.client.call('SoftLayer_Software_VirtualLicense', 'getLicenseFile', id=identifier)
        return data

    def getObject(self, identifier: int) -> 'Software_VirtualLicense':
        """Retrieve a SoftLayer_Software_VirtualLicense record."""
        data = self.client.call('SoftLayer_Software_VirtualLicense', 'getObject', id=identifier)
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Software_VirtualLicense', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getBillingItem(self, identifier: int) -> 'Billing_Item':
        """"""
        data = self.client.call('SoftLayer_Software_VirtualLicense', 'getBillingItem', id=identifier)
        from SoftLayer.sltypes.Billing_Item import Billing_Item
        return data

    def getHostHardware(self, identifier: int) -> 'Hardware_Server':
        """"""
        data = self.client.call('SoftLayer_Software_VirtualLicense', 'getHostHardware', id=identifier)
        from SoftLayer.sltypes.Hardware_Server import Hardware_Server
        return data

    def getIpAddressRecord(self, identifier: int) -> 'Network_Subnet_IpAddress':
        """"""
        data = self.client.call('SoftLayer_Software_VirtualLicense', 'getIpAddressRecord', id=identifier)
        from SoftLayer.sltypes.Network_Subnet_IpAddress import Network_Subnet_IpAddress
        return data

    def getSoftwareDescription(self, identifier: int) -> 'Software_Description':
        """"""
        data = self.client.call('SoftLayer_Software_VirtualLicense', 'getSoftwareDescription', id=identifier)
        from SoftLayer.sltypes.Software_Description import Software_Description
        return data

    def getSubnet(self, identifier: int) -> 'Network_Subnet':
        """"""
        data = self.client.call('SoftLayer_Software_VirtualLicense', 'getSubnet', id=identifier)
        from SoftLayer.sltypes.Network_Subnet import Network_Subnet
        return data
