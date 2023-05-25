from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Account_Media(Entity):
    """The SoftLayer_Account_Media data type contains information on a single piece of media associated with a Data
Transfer Service request."""
    description: str
    id_: int
    requestId: int
    serialNumber: str
    typeId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Account_Media'

    def editObject(self, identifier: int, templateObject: 'Account_Media') -> bool:
        """Edit a media."""
        data = self.client.call('SoftLayer_Account_Media', 'editObject', templateObject, id=identifier)
        return data

    def getAllMediaTypes(self) -> list['Account_Media_Type']:
        """Retrieve a list supported media types."""
        data = self.client.call('SoftLayer_Account_Media', 'getAllMediaTypes')
        from SoftLayer.sltypes.Account_Media_Type import Account_Media_Type
        return data

    def getObject(self, identifier: int) -> 'Account_Media':
        """Retrieve a SoftLayer_Account_Media record."""
        data = self.client.call('SoftLayer_Account_Media', 'getObject', id=identifier)
        from SoftLayer.sltypes.Account_Media import Account_Media
        return data

    def removeMediaFromList(self, mediaTemplate: 'Account_Media') -> int:
        """Remove a media from a SoftLayer account's list of media."""
        data = self.client.call('SoftLayer_Account_Media', 'removeMediaFromList', mediaTemplate)
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Account_Media', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getCreateUser(self, identifier: int) -> 'User_Customer':
        """"""
        data = self.client.call('SoftLayer_Account_Media', 'getCreateUser', id=identifier)
        from SoftLayer.sltypes.User_Customer import User_Customer
        return data

    def getDatacenter(self, identifier: int) -> 'Location':
        """"""
        data = self.client.call('SoftLayer_Account_Media', 'getDatacenter', id=identifier)
        from SoftLayer.sltypes.Location import Location
        return data

    def getModifyEmployee(self, identifier: int) -> 'User_Employee':
        """"""
        data = self.client.call('SoftLayer_Account_Media', 'getModifyEmployee', id=identifier)
        from SoftLayer.sltypes.User_Employee import User_Employee
        return data

    def getModifyUser(self, identifier: int) -> 'User_Customer':
        """"""
        data = self.client.call('SoftLayer_Account_Media', 'getModifyUser', id=identifier)
        from SoftLayer.sltypes.User_Customer import User_Customer
        return data

    def getRequest(self, identifier: int) -> 'Account_Media_Data_Transfer_Request':
        """"""
        data = self.client.call('SoftLayer_Account_Media', 'getRequest', id=identifier)
        from SoftLayer.sltypes.Account_Media_Data_Transfer_Request import Account_Media_Data_Transfer_Request
        return data

    def getType(self, identifier: int) -> 'Account_Media_Type':
        """"""
        data = self.client.call('SoftLayer_Account_Media', 'getType', id=identifier)
        from SoftLayer.sltypes.Account_Media_Type import Account_Media_Type
        return data

    def getVolume(self, identifier: int) -> 'Network_Storage':
        """"""
        data = self.client.call('SoftLayer_Account_Media', 'getVolume', id=identifier)
        from SoftLayer.sltypes.Network_Storage import Network_Storage
        return data
