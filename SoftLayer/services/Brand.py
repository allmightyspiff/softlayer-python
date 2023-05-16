# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Brand(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Brand'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def createCustomerAccount(
        self,
        account: SoftLayer_Account,
        bypassDuplicateAccountCheck: boolean,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Account':
        data = self.client.call(
            self.service,
            'createCustomerAccount',
            account,
            bypassDuplicateAccountCheck,
            mask=objectMask
        )
        from SoftLayer.datatypes.Account import Account
        return SL_Account(data)

# This file was automatically generated with tools/generateTypes.py
    def createObject(
        self,
        templateObject: SoftLayer_Brand,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Brand':
        data = self.client.call(
            self.service,
            'createObject',
            templateObject,
            mask=objectMask
        )
        from SoftLayer.datatypes.Brand import Brand
        return SL_Brand(data)

# This file was automatically generated with tools/generateTypes.py
    def disableAccount(
        self,
        accountId: int
    ) -> 'void':
        data = self.client.call(
            self.service,
            'disableAccount',
            accountId
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getAllTicketSubjects(
        self,
        account: SoftLayer_Account,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Ticket_Subject]':
        data = self.client.call(
            self.service,
            'getAllTicketSubjects',
            account,
            mask=objectMask
        )
        from SoftLayer.datatypes.Ticket.Subject import Subject
        return SL_Subject(data)

# This file was automatically generated with tools/generateTypes.py
    def getBillingItemSnapshotsForSingleOwnedAccount(
        self,
        accountId: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Item_Chronicle]':
        data = self.client.call(
            self.service,
            'getBillingItemSnapshotsForSingleOwnedAccount',
            accountId,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Item.Chronicle import Chronicle
        return SL_Chronicle(data)

# This file was automatically generated with tools/generateTypes.py
    def getBillingItemSnapshotsWithExternalAccountId(
        self,
        externalAccountId: str,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Item_Chronicle]':
        data = self.client.call(
            self.service,
            'getBillingItemSnapshotsWithExternalAccountId',
            externalAccountId,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Item.Chronicle import Chronicle
        return SL_Chronicle(data)

# This file was automatically generated with tools/generateTypes.py
    def getContactInformation(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Brand_Contact]':
        data = self.client.call(
            self.service,
            'getContactInformation',
            mask=objectMask
        )
        from SoftLayer.datatypes.Brand.Contact import Contact
        return SL_Contact(data)

# This file was automatically generated with tools/generateTypes.py
    def getMerchantName(
        self,
        
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getMerchantName',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Brand':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Brand import Brand
        return SL_Brand(data)

# This file was automatically generated with tools/generateTypes.py
    def getToken(
        self,
        userId: int
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getToken',
            userId
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def isIbmSlicBrand(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'isIbmSlicBrand',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def isPlatformServicesBrand(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'isPlatformServicesBrand',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def migrateExternalAccount(
        self,
        accountId: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Account_Brand_Migration_Request':
        data = self.client.call(
            self.service,
            'migrateExternalAccount',
            accountId,
            mask=objectMask
        )
        from SoftLayer.datatypes.Account.Brand.Migration.Request import Request
        return SL_Request(data)

# This file was automatically generated with tools/generateTypes.py
    def reactivateAccount(
        self,
        accountId: int
    ) -> 'void':
        data = self.client.call(
            self.service,
            'reactivateAccount',
            accountId
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def refreshBillingItemSnapshot(
        self,
        accountId: int
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'refreshBillingItemSnapshot',
            accountId
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def verifyCanDisableAccount(
        self,
        accountId: int
    ) -> 'void':
        data = self.client.call(
            self.service,
            'verifyCanDisableAccount',
            accountId
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def verifyCanReactivateAccount(
        self,
        accountId: int
    ) -> 'void':
        data = self.client.call(
            self.service,
            'verifyCanReactivateAccount',
            accountId
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getAccount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account':
        data = self.client.call(
            self.service,
            'getAccount',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account import Account
        return SL_Account(data)

# This file was automatically generated with tools/generateTypes.py
    def getAllOwnedAccounts(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Account]':
        data = self.client.call(
            self.service,
            'getAllOwnedAccounts',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Account import Account
        return SL_Account(data)

# This file was automatically generated with tools/generateTypes.py
    def getAllowAccountCreationFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'getAllowAccountCreationFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getBillingItemSnapshots(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Item_Chronicle]':
        data = self.client.call(
            self.service,
            'getBillingItemSnapshots',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Item.Chronicle import Chronicle
        return SL_Chronicle(data)

# This file was automatically generated with tools/generateTypes.py
    def getBusinessPartner(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Brand_Business_Partner':
        data = self.client.call(
            self.service,
            'getBusinessPartner',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Brand.Business.Partner import Partner
        return SL_Partner(data)

# This file was automatically generated with tools/generateTypes.py
    def getBusinessPartnerFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'getBusinessPartnerFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getCatalog(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Product_Catalog':
        data = self.client.call(
            self.service,
            'getCatalog',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Product.Catalog import Catalog
        return SL_Catalog(data)

# This file was automatically generated with tools/generateTypes.py
    def getContacts(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Brand_Contact]':
        data = self.client.call(
            self.service,
            'getContacts',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Brand.Contact import Contact
        return SL_Contact(data)

# This file was automatically generated with tools/generateTypes.py
    def getCustomerCountryLocationRestrictions(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Brand_Restriction_Location_CustomerCountry]':
        data = self.client.call(
            self.service,
            'getCustomerCountryLocationRestrictions',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Brand.Restriction.Location.CustomerCountry import CustomerCountry
        return SL_CustomerCountry(data)

# This file was automatically generated with tools/generateTypes.py
    def getDistributor(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Brand':
        data = self.client.call(
            self.service,
            'getDistributor',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Brand import Brand
        return SL_Brand(data)

# This file was automatically generated with tools/generateTypes.py
    def getDistributorChildFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'getDistributorChildFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getDistributorFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getDistributorFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getHardware(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':
        data = self.client.call(
            self.service,
            'getHardware',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return SL_Hardware(data)

# This file was automatically generated with tools/generateTypes.py
    def getHasAgentAdvancedSupportFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'getHasAgentAdvancedSupportFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getHasAgentSupportFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'getHasAgentSupportFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getOpenTickets(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Ticket]':
        data = self.client.call(
            self.service,
            'getOpenTickets',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Ticket import Ticket
        return SL_Ticket(data)

# This file was automatically generated with tools/generateTypes.py
    def getOwnedAccounts(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Account]':
        data = self.client.call(
            self.service,
            'getOwnedAccounts',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Account import Account
        return SL_Account(data)

# This file was automatically generated with tools/generateTypes.py
    def getSecurityLevel(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Security_Level':
        data = self.client.call(
            self.service,
            'getSecurityLevel',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Security.Level import Level
        return SL_Level(data)

# This file was automatically generated with tools/generateTypes.py
    def getTicketGroups(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Ticket_Group]':
        data = self.client.call(
            self.service,
            'getTicketGroups',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Ticket.Group import Group
        return SL_Group(data)

# This file was automatically generated with tools/generateTypes.py
    def getTickets(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Ticket]':
        data = self.client.call(
            self.service,
            'getTickets',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Ticket import Ticket
        return SL_Ticket(data)

# This file was automatically generated with tools/generateTypes.py
    def getUsers(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_Customer]':
        data = self.client.call(
            self.service,
            'getUsers',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.Customer import Customer
        return SL_Customer(data)

# This file was automatically generated with tools/generateTypes.py
    def getVirtualGuests(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest]':
        data = self.client.call(
            self.service,
            'getVirtualGuests',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest import Guest
        return SL_Guest(data)


