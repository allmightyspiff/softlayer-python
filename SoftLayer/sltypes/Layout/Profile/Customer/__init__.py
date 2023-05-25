from SoftLayer.sltypes.Layout.Profile import Layout_Profile
from SoftLayer.sltypes.Layout_Profile import Layout_Profile
from SoftLayer import BaseClient

class Layout_Profile_Customer(Layout_Profile):
    pass

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Layout_Profile_Customer'

    def getObject(self, identifier: int) -> 'Layout_Profile_Customer':
        """Retrieve a SoftLayer_Layout_Profile_Customer record."""
        data = self.client.call('SoftLayer_Layout_Profile_Customer', 'getObject', id=identifier)
        return data

    def getUserRecord(self, identifier: int) -> 'User_Customer':
        """"""
        data = self.client.call('SoftLayer_Layout_Profile_Customer', 'getUserRecord', id=identifier)
        from SoftLayer.sltypes.User_Customer import User_Customer
        return data
