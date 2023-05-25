from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Account_Address(Entity):
    """The SoftLayer_Account_Address data type contains information on an address associated with a SoftLayer
account."""
    accountId: int
    address1: str
    address2: str
    city: str
    contactName: str
    country: str
    description: str
    id_: int
    isActive: int
    locationId: int
    postalCode: str
    state: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Account_Address'

    def createObject(self, templateObject: 'Account_Address') -> 'Account_Address':
        """Create a new address record."""
        data = self.client.call('SoftLayer_Account_Address', 'createObject', templateObject)
        from SoftLayer.sltypes.Account_Address import Account_Address
        return data

    def editObject(self, identifier: int, templateObject: 'Account_Address') -> bool:
        """Edit an address record."""
        data = self.client.call('SoftLayer_Account_Address', 'editObject', templateObject, id=identifier)
        return data

    def getAllDataCenters(self) -> list['Account_Address']:
        """Retrieve a list of SoftLayer datacenter addresses."""
        data = self.client.call('SoftLayer_Account_Address', 'getAllDataCenters')
        from SoftLayer.sltypes.Account_Address import Account_Address
        return data

    def getNetworkAddress(self, name: str) -> list['Account_Address']:
        """Retrieve a list of SoftLayer datacenter addresses."""
        data = self.client.call('SoftLayer_Account_Address', 'getNetworkAddress', name)
        from SoftLayer.sltypes.Account_Address import Account_Address
        return data

    def getObject(self, identifier: int) -> 'Account_Address':
        """Retrieve a SoftLayer_Account_Address record."""
        data = self.client.call('SoftLayer_Account_Address', 'getObject', id=identifier)
        from SoftLayer.sltypes.Account_Address import Account_Address
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Account_Address', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getCreateUser(self, identifier: int) -> 'User_Customer':
        """"""
        data = self.client.call('SoftLayer_Account_Address', 'getCreateUser', id=identifier)
        from SoftLayer.sltypes.User_Customer import User_Customer
        return data

    def getLocation(self, identifier: int) -> 'Location':
        """"""
        data = self.client.call('SoftLayer_Account_Address', 'getLocation', id=identifier)
        from SoftLayer.sltypes.Location import Location
        return data

    def getModifyEmployee(self, identifier: int) -> 'User_Employee':
        """"""
        data = self.client.call('SoftLayer_Account_Address', 'getModifyEmployee', id=identifier)
        from SoftLayer.sltypes.User_Employee import User_Employee
        return data

    def getModifyUser(self, identifier: int) -> 'User_Customer':
        """"""
        data = self.client.call('SoftLayer_Account_Address', 'getModifyUser', id=identifier)
        from SoftLayer.sltypes.User_Customer import User_Customer
        return data

    def getType(self, identifier: int) -> 'Account_Address_Type':
        """"""
        data = self.client.call('SoftLayer_Account_Address', 'getType', id=identifier)
        from SoftLayer.sltypes.Account_Address_Type import Account_Address_Type
        return data
