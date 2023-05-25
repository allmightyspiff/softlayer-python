from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Subnet_Registration_Details(Entity):
    """The SoftLayer_Network_Subnet_Registration_Details objects are used to relate
[[SoftLayer_Account_Regional_Registry_Detail]] objects to a [[SoftLayer_Network_Subnet_Registration]] object.
This allows for easy reuse of registration details. It is important to note that only one detail object per
type may be associated to a registration object."""
    createDate: datetime
    detailId: int
    id_: int
    modifyDate: datetime
    registrationId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Subnet_Registration_Details'

    def createObject(self, templateObject: 'Network_Subnet_Registration_Details') -> 'Network_Subnet_Registration_Details':
        """Create a new association between a [[SoftLayer_Network_Subnet_Registration]] object and a
[[SoftLayer_Account_Regional_Registry_Detail]] object."""
        data = self.client.call('SoftLayer_Network_Subnet_Registration_Details', 'createObject', templateObject)
        return data

    def deleteObject(self, identifier: int) -> bool:
        """Remove an existing association between a [[SoftLayer_Network_Subnet_Registration]] object and a
[[SoftLayer_Account_Regional_Registry_Detail]] object."""
        data = self.client.call('SoftLayer_Network_Subnet_Registration_Details', 'deleteObject', id=identifier)
        return data

    def getObject(self, identifier: int) -> 'Network_Subnet_Registration_Details':
        """Retrieve a SoftLayer_Network_Subnet_Registration_Details record."""
        data = self.client.call('SoftLayer_Network_Subnet_Registration_Details', 'getObject', id=identifier)
        return data

    def getDetail(self, identifier: int) -> 'Account_Regional_Registry_Detail':
        """"""
        data = self.client.call('SoftLayer_Network_Subnet_Registration_Details', 'getDetail', id=identifier)
        from SoftLayer.sltypes.Account_Regional_Registry_Detail import Account_Regional_Registry_Detail
        return data

    def getRegistration(self, identifier: int) -> 'Network_Subnet_Registration':
        """"""
        data = self.client.call('SoftLayer_Network_Subnet_Registration_Details', 'getRegistration', id=identifier)
        from SoftLayer.sltypes.Network_Subnet_Registration import Network_Subnet_Registration
        return data
