# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Marketplace_Partner(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Marketplace_Partner'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
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
        return SL_Partner(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Partner(data)

# This file was automatically generated with tools/generateTypes.py
    def getFeaturedPartners(
        self,
        non: boolean,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Marketplace_Partner]':
        data = self.client.call(
            self.service,
            'getFeaturedPartners',
            non,
            mask=objectMask
        )
        from SoftLayer.datatypes.Marketplace.Partner import Partner
        return SL_Partner(data)

# This file was automatically generated with tools/generateTypes.py
    def getFile(
        self,
        name: str
    ) -> 'SoftLayer_Marketplace_Partner_File':
        data = self.client.call(
            self.service,
            'getFile',
            name
        )
        from SoftLayer.datatypes.Marketplace.Partner.File import File
        return SL_File(data)

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Marketplace_Partner':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Marketplace.Partner import Partner
        return SL_Partner(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Partner(data)

# This file was automatically generated with tools/generateTypes.py
    def getAttachments(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Marketplace_Partner_Attachment]':
        data = self.client.call(
            self.service,
            'getAttachments',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Marketplace.Partner.Attachment import Attachment
        return SL_Attachment(data)

# This file was automatically generated with tools/generateTypes.py
    def getLogoMedium(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Marketplace_Partner_Attachment':
        data = self.client.call(
            self.service,
            'getLogoMedium',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Marketplace.Partner.Attachment import Attachment
        return SL_Attachment(data)

# This file was automatically generated with tools/generateTypes.py
    def getLogoMediumTemp(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Marketplace_Partner_Attachment':
        data = self.client.call(
            self.service,
            'getLogoMediumTemp',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Marketplace.Partner.Attachment import Attachment
        return SL_Attachment(data)

# This file was automatically generated with tools/generateTypes.py
    def getLogoSmall(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Marketplace_Partner_Attachment':
        data = self.client.call(
            self.service,
            'getLogoSmall',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Marketplace.Partner.Attachment import Attachment
        return SL_Attachment(data)

# This file was automatically generated with tools/generateTypes.py
    def getLogoSmallTemp(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Marketplace_Partner_Attachment':
        data = self.client.call(
            self.service,
            'getLogoSmallTemp',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Marketplace.Partner.Attachment import Attachment
        return SL_Attachment(data)


