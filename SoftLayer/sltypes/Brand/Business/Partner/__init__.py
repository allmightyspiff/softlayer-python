from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Brand_Business_Partner(Entity):
    """Contains business partner details associated with a brand. Country Enterprise Identifier (CEID), Channel ID,
Segment ID and Reseller Level."""
    channelId: int
    countryEnterpriseCode: str
    resellerLevel: int
    segmentId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Brand_Business_Partner'

    def getObject(self, identifier: int) -> 'Brand_Business_Partner':
        """Retrieve a SoftLayer_Brand_Business_Partner record."""
        data = self.client.call('SoftLayer_Brand_Business_Partner', 'getObject', id=identifier)
        return data

    def getBrand(self, identifier: int) -> 'Brand':
        """"""
        data = self.client.call('SoftLayer_Brand_Business_Partner', 'getBrand', id=identifier)
        from SoftLayer.sltypes.Brand import Brand
        return data

    def getChannel(self, identifier: int) -> 'Business_Partner_Channel':
        """"""
        data = self.client.call('SoftLayer_Brand_Business_Partner', 'getChannel', id=identifier)
        from SoftLayer.sltypes.Business_Partner_Channel import Business_Partner_Channel
        return data

    def getSegment(self, identifier: int) -> 'Business_Partner_Segment':
        """"""
        data = self.client.call('SoftLayer_Brand_Business_Partner', 'getSegment', id=identifier)
        from SoftLayer.sltypes.Business_Partner_Segment import Business_Partner_Segment
        return data
