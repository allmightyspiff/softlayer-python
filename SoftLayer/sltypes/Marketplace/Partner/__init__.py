from SoftLayer.sltypes.Marketplace.Partner.Attachment import Marketplace_Partner_Attachment
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Marketplace_Partner(Entity):
    accountId: int
    attachedFiles: list[Marketplace_Partner_Attachment]
    companyDescription: str
    companyName: str
    headlineDescription: str
    id_: int
    linkFreeTrial: str
    linkOrderPage: str
    linkWebsite: str
    metaDescription: str
    metaKeywords: str
    productBenefits: str
    productCategoryId: int
    productDescriptionLong: str
    productDescriptionShort: str
    productFeatures: str
    productName: str
    productTitle: str
    urlIdentifier: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Marketplace_Partner'

    def getAllObjects(self) -> list['Marketplace_Partner']:
        data = self.client.call('SoftLayer_Marketplace_Partner', 'getAllObjects')
        return data

    def getAllPublishedPartners(self, searchTerm: str) -> list['Marketplace_Partner']:
        data = self.client.call('SoftLayer_Marketplace_Partner', 'getAllPublishedPartners', searchTerm)
        return data

    def getFeaturedPartners(self, non: bool) -> list['Marketplace_Partner']:
        data = self.client.call('SoftLayer_Marketplace_Partner', 'getFeaturedPartners', non)
        return data

    def getFile(self, identifier: int, name: str) -> 'Marketplace_Partner_File':
        data = self.client.call('SoftLayer_Marketplace_Partner', 'getFile', name, id=identifier)
        from SoftLayer.sltypes.Marketplace_Partner_File import Marketplace_Partner_File
        return data

    def getObject(self, identifier: int) -> 'Marketplace_Partner':
        """Retrieve a SoftLayer_Marketplace_Partner record."""
        data = self.client.call('SoftLayer_Marketplace_Partner', 'getObject', id=identifier)
        return data

    def getPartnerByUrlIdentifier(self, urlIdentifier: str) -> 'Marketplace_Partner':
        data = self.client.call('SoftLayer_Marketplace_Partner', 'getPartnerByUrlIdentifier', urlIdentifier)
        return data

    def getAttachments(self, identifier: int) -> list['Marketplace_Partner_Attachment']:
        """"""
        data = self.client.call('SoftLayer_Marketplace_Partner', 'getAttachments', id=identifier)
        from SoftLayer.sltypes.Marketplace_Partner_Attachment import Marketplace_Partner_Attachment
        return data

    def getLogoMedium(self, identifier: int) -> 'Marketplace_Partner_Attachment':
        """"""
        data = self.client.call('SoftLayer_Marketplace_Partner', 'getLogoMedium', id=identifier)
        from SoftLayer.sltypes.Marketplace_Partner_Attachment import Marketplace_Partner_Attachment
        return data

    def getLogoMediumTemp(self, identifier: int) -> 'Marketplace_Partner_Attachment':
        """"""
        data = self.client.call('SoftLayer_Marketplace_Partner', 'getLogoMediumTemp', id=identifier)
        from SoftLayer.sltypes.Marketplace_Partner_Attachment import Marketplace_Partner_Attachment
        return data

    def getLogoSmall(self, identifier: int) -> 'Marketplace_Partner_Attachment':
        """"""
        data = self.client.call('SoftLayer_Marketplace_Partner', 'getLogoSmall', id=identifier)
        from SoftLayer.sltypes.Marketplace_Partner_Attachment import Marketplace_Partner_Attachment
        return data

    def getLogoSmallTemp(self, identifier: int) -> 'Marketplace_Partner_Attachment':
        """"""
        data = self.client.call('SoftLayer_Marketplace_Partner', 'getLogoSmallTemp', id=identifier)
        from SoftLayer.sltypes.Marketplace_Partner_Attachment import Marketplace_Partner_Attachment
        return data
