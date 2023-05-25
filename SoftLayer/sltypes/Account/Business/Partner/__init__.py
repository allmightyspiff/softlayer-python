from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Account_Business_Partner(Entity):
    """Contains business partner details associated with an account. Country Enterprise Identifier (CEID), Channel
ID, Segment ID and Reseller Level."""
    channelId: int
    countryEnterpriseCode: str
    resellerLevel: int
    segmentId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Account_Business_Partner'

    def getObject(self, identifier: int) -> 'Account_Business_Partner':
        """Retrieve a SoftLayer_Account_Business_Partner record."""
        data = self.client.call('SoftLayer_Account_Business_Partner', 'getObject', id=identifier)
        from SoftLayer.sltypes.Account_Business_Partner import Account_Business_Partner
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Account_Business_Partner', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getChannel(self, identifier: int) -> 'Business_Partner_Channel':
        """"""
        data = self.client.call('SoftLayer_Account_Business_Partner', 'getChannel', id=identifier)
        from SoftLayer.sltypes.Business_Partner_Channel import Business_Partner_Channel
        return data

    def getSegment(self, identifier: int) -> 'Business_Partner_Segment':
        """"""
        data = self.client.call('SoftLayer_Account_Business_Partner', 'getSegment', id=identifier)
        from SoftLayer.sltypes.Business_Partner_Segment import Business_Partner_Segment
        return data
