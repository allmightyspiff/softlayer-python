# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Brand(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Brand'
        self.client = client

    def createCustomerAccount(
        self,
        account: 'SoftLayer_Account',
        bypassDuplicateAccountCheck: bool,
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
        templateObject: 'SoftLayer_Brand',
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
        accountId: int,
        identifier: int
    ) -> 'void':

        data = self.client.call(
            self.service,
            'disableAccount',
            accountId,
            id=identifier
        )
        
        return data


    def getAllTicketSubjects(
        self,
        account: 'SoftLayer_Account',
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Ticket_Subject]':

        data = self.client.call(
            self.service,
            'getAllTicketSubjects',
            account,
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Ticket.Subject import Subject
        return Subject(data)


    def getBillingItemSnapshotsForSingleOwnedAccount(
        self,
        accountId: int,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Item_Chronicle]':

        data = self.client.call(
            self.service,
            'getBillingItemSnapshotsForSingleOwnedAccount',
            accountId,
            id=identifier,
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
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Item_Chronicle]':

        data = self.client.call(
            self.service,
            'getBillingItemSnapshotsWithExternalAccountId',
            externalAccountId,
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Item.Chronicle import Chronicle
        return Chronicle(data)


    def getContactInformation(
        self,
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Brand_Contact]':

        data = self.client.call(
            self.service,
            'getContactInformation',
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Brand.Contact import Contact
        return Contact(data)


    def getMerchantName(
        self,
        identifier: int
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getMerchantName',
            id=identifier
        )
        
        return data


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Brand':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Brand import Brand
        return Brand(data)


    def getToken(
        self,
        userId: int,
        identifier: int
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getToken',
            userId,
            id=identifier
        )
        
        return data


    def isIbmSlicBrand(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'isIbmSlicBrand',
            id=identifier
        )
        
        return data


    def isPlatformServicesBrand(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'isPlatformServicesBrand',
            id=identifier
        )
        
        return data


    def migrateExternalAccount(
        self,
        accountId: int,
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Account_Brand_Migration_Request':

        data = self.client.call(
            self.service,
            'migrateExternalAccount',
            accountId,
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Account.Brand.Migration.Request import Request
        return Request(data)


    def reactivateAccount(
        self,
        accountId: int,
        identifier: int
    ) -> 'void':

        data = self.client.call(
            self.service,
            'reactivateAccount',
            accountId,
            id=identifier
        )
        
        return data


    def refreshBillingItemSnapshot(
        self,
        accountId: int,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'refreshBillingItemSnapshot',
            accountId,
            id=identifier
        )
        
        return data


    def verifyCanDisableAccount(
        self,
        accountId: int,
        identifier: int
    ) -> 'void':

        data = self.client.call(
            self.service,
            'verifyCanDisableAccount',
            accountId,
            id=identifier
        )
        
        return data


    def verifyCanReactivateAccount(
        self,
        accountId: int,
        identifier: int
    ) -> 'void':

        data = self.client.call(
            self.service,
            'verifyCanReactivateAccount',
            accountId,
            id=identifier
        )
        
        return data


    def getAccount(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account':

        data = self.client.call(
            self.service,
            'getAccount',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account import Account
        return Account(data)


    def getAllOwnedAccounts(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Account]':

        data = self.client.call(
            self.service,
            'getAllOwnedAccounts',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Account import Account
        return Account(data)


    def getAllowAccountCreationFlag(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getAllowAccountCreationFlag',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getBillingItemSnapshots(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Item_Chronicle]':

        data = self.client.call(
            self.service,
            'getBillingItemSnapshots',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Item.Chronicle import Chronicle
        return Chronicle(data)


    def getBusinessPartner(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Brand_Business_Partner':

        data = self.client.call(
            self.service,
            'getBusinessPartner',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Brand.Business.Partner import Partner
        return Partner(data)


    def getBusinessPartnerFlag(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getBusinessPartnerFlag',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getCatalog(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Product_Catalog':

        data = self.client.call(
            self.service,
            'getCatalog',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Product.Catalog import Catalog
        return Catalog(data)


    def getContacts(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Brand_Contact]':

        data = self.client.call(
            self.service,
            'getContacts',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Brand.Contact import Contact
        return Contact(data)


    def getCustomerCountryLocationRestrictions(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Brand_Restriction_Location_CustomerCountry]':

        data = self.client.call(
            self.service,
            'getCustomerCountryLocationRestrictions',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Brand.Restriction.Location.CustomerCountry import CustomerCountry
        return CustomerCountry(data)


    def getDistributor(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Brand':

        data = self.client.call(
            self.service,
            'getDistributor',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Brand import Brand
        return Brand(data)


    def getDistributorChildFlag(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getDistributorChildFlag',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getDistributorFlag(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getDistributorFlag',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getHardware(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':

        data = self.client.call(
            self.service,
            'getHardware',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


    def getHasAgentAdvancedSupportFlag(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getHasAgentAdvancedSupportFlag',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getHasAgentSupportFlag(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getHasAgentSupportFlag',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getOpenTickets(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Ticket]':

        data = self.client.call(
            self.service,
            'getOpenTickets',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Ticket import Ticket
        return Ticket(data)


    def getOwnedAccounts(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Account]':

        data = self.client.call(
            self.service,
            'getOwnedAccounts',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Account import Account
        return Account(data)


    def getSecurityLevel(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Security_Level':

        data = self.client.call(
            self.service,
            'getSecurityLevel',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Security.Level import Level
        return Level(data)


    def getTicketGroups(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Ticket_Group]':

        data = self.client.call(
            self.service,
            'getTicketGroups',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Ticket.Group import Group
        return Group(data)


    def getTickets(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Ticket]':

        data = self.client.call(
            self.service,
            'getTickets',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Ticket import Ticket
        return Ticket(data)


    def getUsers(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_Customer]':

        data = self.client.call(
            self.service,
            'getUsers',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.Customer import Customer
        return Customer(data)


    def getVirtualGuests(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest]':

        data = self.client.call(
            self.service,
            'getVirtualGuests',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest import Guest
        return Guest(data)


