from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Subnet_Registration(Entity):
    """The subnet registration data type contains general information relating to a single subnet registration
instance. These registration instances can be updated to reflect changes, and will record the changes in the
[[SoftLayer_Network_Subnet_Registration_Event|events]]."""
    accountId: int
    cidr: int
    createDate: datetime
    id_: int
    modifyDate: datetime
    networkHandle: str
    networkIdentifier: str
    regionalInternetRegistryHandleId: int
    regionalInternetRegistryId: int
    statusId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Subnet_Registration'

    def clearRegistration(self, identifier: int) -> bool:
        """Clear an existing registration"""
        data = self.client.call('SoftLayer_Network_Subnet_Registration', 'clearRegistration', id=identifier)
        return data

    def createObject(self, templateObject: 'Network_Subnet_Registration') -> 'Network_Subnet_Registration':
        """Create a new subnet registration"""
        data = self.client.call('SoftLayer_Network_Subnet_Registration', 'createObject', templateObject)
        from SoftLayer.sltypes.Network_Subnet_Registration import Network_Subnet_Registration
        return data

    def createObjects(self, templateObjects: 'Network_Subnet_Registration') -> list['Network_Subnet_Registration']:
        """Create registrations for multiple subnets"""
        data = self.client.call('SoftLayer_Network_Subnet_Registration', 'createObjects', templateObjects)
        from SoftLayer.sltypes.Network_Subnet_Registration import Network_Subnet_Registration
        return data

    def editObject(self, identifier: int, templateObject: 'Network_Subnet_Registration') -> bool:
        """Edit an existing registration object"""
        data = self.client.call('SoftLayer_Network_Subnet_Registration', 'editObject', templateObject, id=identifier)
        return data

    def editRegistrationAttachedDetails(self, personObjectSkeleton: 'Network_Subnet_Registration_Details', networkObjectSkeleton: 'Network_Subnet_Registration_Details') -> bool:
        """Modify the link between a [[SoftLayer_Network_Subnet_Registration]] object and two
[[SoftLayer_Account_Regional_Registry_Detail]] objects simultaneously."""
        data = self.client.call('SoftLayer_Network_Subnet_Registration', 'editRegistrationAttachedDetails', personObjectSkeleton, networkObjectSkeleton)
        return data

    def getObject(self, identifier: int) -> 'Network_Subnet_Registration':
        """Retrieve a SoftLayer_Network_Subnet_Registration record."""
        data = self.client.call('SoftLayer_Network_Subnet_Registration', 'getObject', id=identifier)
        from SoftLayer.sltypes.Network_Subnet_Registration import Network_Subnet_Registration
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Network_Subnet_Registration', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getDetailReferences(self, identifier: int) -> list['Network_Subnet_Registration_Details']:
        """"""
        data = self.client.call('SoftLayer_Network_Subnet_Registration', 'getDetailReferences', id=identifier)
        from SoftLayer.sltypes.Network_Subnet_Registration_Details import Network_Subnet_Registration_Details
        return data

    def getEvents(self, identifier: int) -> list['Network_Subnet_Registration_Event']:
        """"""
        data = self.client.call('SoftLayer_Network_Subnet_Registration', 'getEvents', id=identifier)
        from SoftLayer.sltypes.Network_Subnet_Registration_Event import Network_Subnet_Registration_Event
        return data

    def getNetworkDetail(self, identifier: int) -> 'Account_Regional_Registry_Detail':
        """"""
        data = self.client.call('SoftLayer_Network_Subnet_Registration', 'getNetworkDetail', id=identifier)
        from SoftLayer.sltypes.Account_Regional_Registry_Detail import Account_Regional_Registry_Detail
        return data

    def getPersonDetail(self, identifier: int) -> 'Account_Regional_Registry_Detail':
        """"""
        data = self.client.call('SoftLayer_Network_Subnet_Registration', 'getPersonDetail', id=identifier)
        from SoftLayer.sltypes.Account_Regional_Registry_Detail import Account_Regional_Registry_Detail
        return data

    def getRegionalInternetRegistry(self, identifier: int) -> 'Network_Regional_Internet_Registry':
        """"""
        data = self.client.call('SoftLayer_Network_Subnet_Registration', 'getRegionalInternetRegistry', id=identifier)
        from SoftLayer.sltypes.Network_Regional_Internet_Registry import Network_Regional_Internet_Registry
        return data

    def getRegionalInternetRegistryHandle(self, identifier: int) -> 'Account_Rwhois_Handle':
        """"""
        data = self.client.call('SoftLayer_Network_Subnet_Registration', 'getRegionalInternetRegistryHandle', id=identifier)
        from SoftLayer.sltypes.Account_Rwhois_Handle import Account_Rwhois_Handle
        return data

    def getStatus(self, identifier: int) -> 'Network_Subnet_Registration_Status':
        """"""
        data = self.client.call('SoftLayer_Network_Subnet_Registration', 'getStatus', id=identifier)
        from SoftLayer.sltypes.Network_Subnet_Registration_Status import Network_Subnet_Registration_Status
        return data

    def getSubnet(self, identifier: int) -> 'Network_Subnet':
        """"""
        data = self.client.call('SoftLayer_Network_Subnet_Registration', 'getSubnet', id=identifier)
        from SoftLayer.sltypes.Network_Subnet import Network_Subnet
        return data
