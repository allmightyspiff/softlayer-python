# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Brand(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Brand'
        self.client = client

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
        return Account(data)


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
        return Brand(data)


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
        return Subject(data)


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
        return Chronicle(data)


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
        return Chronicle(data)


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
        return Contact(data)


    def getMerchantName(
        self,
        
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getMerchantName',
            
        )
        
        return data


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
        return Brand(data)


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


    def isIbmSlicBrand(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'isIbmSlicBrand',
            
        )
        
        return data


    def isPlatformServicesBrand(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'isPlatformServicesBrand',
            
        )
        
        return data


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
        return Request(data)


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
        return Account(data)


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
        return Account(data)


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
        return Chronicle(data)


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
        return Partner(data)


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
        return Catalog(data)


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
        return Contact(data)


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
        return CustomerCountry(data)


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
        return Brand(data)


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
        return Hardware(data)


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
        return Ticket(data)


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
        return Account(data)


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
        return Level(data)


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
        return Group(data)


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
        return Ticket(data)


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
        return Customer(data)


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
        return Guest(data)


