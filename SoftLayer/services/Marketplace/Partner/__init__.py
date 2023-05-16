# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Marketplace_Partner(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Marketplace_Partner'
        self.client = client

    def getAllObjects(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Marketplace_Partner]':

        data = self.client.call(
            self.service,
            'getAllObjects',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Marketplace.Partner import Partner
        return Partner(data)


    def getAllPublishedPartners(
        self,
        searchTerm: str,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Marketplace_Partner]':

        data = self.client.call(
            self.service,
            'getAllPublishedPartners',
            searchTerm,
            mask=objectMask
        )
        from SoftLayer.datatypes.Marketplace.Partner import Partner
        return Partner(data)


    def getFeaturedPartners(
        self,
        non: bool,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Marketplace_Partner]':

        data = self.client.call(
            self.service,
            'getFeaturedPartners',
            non,
            mask=objectMask
        )
        from SoftLayer.datatypes.Marketplace.Partner import Partner
        return Partner(data)


    def getFile(
        self,
        name: str,
        identifier: int
    ) -> 'SoftLayer_Marketplace_Partner_File':

        data = self.client.call(
            self.service,
            'getFile',
            name,
            id=identifier
        )
        from SoftLayer.datatypes.Marketplace.Partner.File import File
        return File(data)


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Marketplace_Partner':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Marketplace.Partner import Partner
        return Partner(data)


    def getPartnerByUrlIdentifier(
        self,
        urlIdentifier: str,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Marketplace_Partner':

        data = self.client.call(
            self.service,
            'getPartnerByUrlIdentifier',
            urlIdentifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Marketplace.Partner import Partner
        return Partner(data)


    def getAttachments(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Marketplace_Partner_Attachment]':

        data = self.client.call(
            self.service,
            'getAttachments',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Marketplace.Partner.Attachment import Attachment
        return Attachment(data)


    def getLogoMedium(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Marketplace_Partner_Attachment':

        data = self.client.call(
            self.service,
            'getLogoMedium',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Marketplace.Partner.Attachment import Attachment
        return Attachment(data)


    def getLogoMediumTemp(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Marketplace_Partner_Attachment':

        data = self.client.call(
            self.service,
            'getLogoMediumTemp',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Marketplace.Partner.Attachment import Attachment
        return Attachment(data)


    def getLogoSmall(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Marketplace_Partner_Attachment':

        data = self.client.call(
            self.service,
            'getLogoSmall',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Marketplace.Partner.Attachment import Attachment
        return Attachment(data)


    def getLogoSmallTemp(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Marketplace_Partner_Attachment':

        data = self.client.call(
            self.service,
            'getLogoSmallTemp',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Marketplace.Partner.Attachment import Attachment
        return Attachment(data)


