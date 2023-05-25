from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Brand(Entity):
    """The SoftLayer_Brand data type contains brand information relating to the single SoftLayer customer account.
IBM Cloud Infrastructure customers are unable to change their brand information in the portal or the API."""
    catalogId: int
    id_: int
    keyName: str
    longName: str
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Brand'

    def createCustomerAccount(self, account: 'Account', bypassDuplicateAccountCheck: bool) -> 'Account':
        """Create a new customer account record."""
        data = self.client.call('SoftLayer_Brand', 'createCustomerAccount', account, bypassDuplicateAccountCheck)
        from SoftLayer.sltypes.Account import Account
        return data

    def createObject(self, templateObject: 'Brand') -> 'Brand':
        """Create a new brand."""
        data = self.client.call('SoftLayer_Brand', 'createObject', templateObject)
        return data

    def disableAccount(self, identifier: int, accountId: int) -> None:
        data = self.client.call('SoftLayer_Brand', 'disableAccount', accountId, id=identifier)
        return data

    def getAllTicketSubjects(self, identifier: int, account: 'Account') -> list['Ticket_Subject']:
        data = self.client.call('SoftLayer_Brand', 'getAllTicketSubjects', account, id=identifier)
        from SoftLayer.sltypes.Ticket_Subject import Ticket_Subject
        return data

    def getBillingItemSnapshotsForSingleOwnedAccount(self, identifier: int, accountId: int) -> list['Billing_Item_Chronicle']:
        """Returns billing item snapshots on accounts owned by specific brands."""
        data = self.client.call('SoftLayer_Brand', 'getBillingItemSnapshotsForSingleOwnedAccount', accountId, id=identifier)
        from SoftLayer.sltypes.Billing_Item_Chronicle import Billing_Item_Chronicle
        return data

    def getBillingItemSnapshotsWithExternalAccountId(self, identifier: int, externalAccountId: str) -> list['Billing_Item_Chronicle']:
        """Returns billing item snapshots on accounts owned by specific brands."""
        data = self.client.call('SoftLayer_Brand', 'getBillingItemSnapshotsWithExternalAccountId', externalAccountId, id=identifier)
        from SoftLayer.sltypes.Billing_Item_Chronicle import Billing_Item_Chronicle
        return data

    def getContactInformation(self, identifier: int) -> list['Brand_Contact']:
        """Retrieve the contact information for the customer account brand."""
        data = self.client.call('SoftLayer_Brand', 'getContactInformation', id=identifier)
        from SoftLayer.sltypes.Brand_Contact import Brand_Contact
        return data

    def getMerchantName(self, identifier: int) -> str:
        data = self.client.call('SoftLayer_Brand', 'getMerchantName', id=identifier)
        return data

    def getObject(self, identifier: int) -> 'Brand':
        """Retrieve a SoftLayer_Brand record."""
        data = self.client.call('SoftLayer_Brand', 'getObject', id=identifier)
        return data

    def getToken(self, identifier: int, userId: int) -> str:
        data = self.client.call('SoftLayer_Brand', 'getToken', userId, id=identifier)
        return data

    def isIbmSlicBrand(self, identifier: int) -> bool:
        """Check if the brand is IBM SLIC top level brand or sub brand."""
        data = self.client.call('SoftLayer_Brand', 'isIbmSlicBrand', id=identifier)
        return data

    def isPlatformServicesBrand(self, identifier: int) -> bool:
        """Check if the alternate billing system of brand is Bluemix."""
        data = self.client.call('SoftLayer_Brand', 'isPlatformServicesBrand', id=identifier)
        return data

    def migrateExternalAccount(self, identifier: int, accountId: int) -> 'Account_Brand_Migration_Request':
        """Migrates an account from an external brand to this brand."""
        data = self.client.call('SoftLayer_Brand', 'migrateExternalAccount', accountId, id=identifier)
        from SoftLayer.sltypes.Account_Brand_Migration_Request import Account_Brand_Migration_Request
        return data

    def reactivateAccount(self, identifier: int, accountId: int) -> None:
        data = self.client.call('SoftLayer_Brand', 'reactivateAccount', accountId, id=identifier)
        return data

    def refreshBillingItemSnapshot(self, identifier: int, accountId: int) -> bool:
        """Begins the process for refreshing the billing item snapshots"""
        data = self.client.call('SoftLayer_Brand', 'refreshBillingItemSnapshot', accountId, id=identifier)
        return data

    def verifyCanDisableAccount(self, identifier: int, accountId: int) -> None:
        data = self.client.call('SoftLayer_Brand', 'verifyCanDisableAccount', accountId, id=identifier)
        return data

    def verifyCanReactivateAccount(self, identifier: int, accountId: int) -> None:
        data = self.client.call('SoftLayer_Brand', 'verifyCanReactivateAccount', accountId, id=identifier)
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Brand', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getAllOwnedAccounts(self, identifier: int) -> list['Account']:
        """"""
        data = self.client.call('SoftLayer_Brand', 'getAllOwnedAccounts', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getAllowAccountCreationFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Brand', 'getAllowAccountCreationFlag', id=identifier)
        return data

    def getBillingItemSnapshots(self, identifier: int) -> list['Billing_Item_Chronicle']:
        """"""
        data = self.client.call('SoftLayer_Brand', 'getBillingItemSnapshots', id=identifier)
        from SoftLayer.sltypes.Billing_Item_Chronicle import Billing_Item_Chronicle
        return data

    def getBusinessPartner(self, identifier: int) -> 'Brand_Business_Partner':
        """"""
        data = self.client.call('SoftLayer_Brand', 'getBusinessPartner', id=identifier)
        from SoftLayer.sltypes.Brand_Business_Partner import Brand_Business_Partner
        return data

    def getBusinessPartnerFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Brand', 'getBusinessPartnerFlag', id=identifier)
        return data

    def getCatalog(self, identifier: int) -> 'Product_Catalog':
        """"""
        data = self.client.call('SoftLayer_Brand', 'getCatalog', id=identifier)
        from SoftLayer.sltypes.Product_Catalog import Product_Catalog
        return data

    def getContacts(self, identifier: int) -> list['Brand_Contact']:
        """"""
        data = self.client.call('SoftLayer_Brand', 'getContacts', id=identifier)
        from SoftLayer.sltypes.Brand_Contact import Brand_Contact
        return data

    def getCustomerCountryLocationRestrictions(self, identifier: int) -> list['Brand_Restriction_Location_CustomerCountry']:
        """"""
        data = self.client.call('SoftLayer_Brand', 'getCustomerCountryLocationRestrictions', id=identifier)
        from SoftLayer.sltypes.Brand_Restriction_Location_CustomerCountry import Brand_Restriction_Location_CustomerCountry
        return data

    def getDistributor(self, identifier: int) -> 'Brand':
        """"""
        data = self.client.call('SoftLayer_Brand', 'getDistributor', id=identifier)
        return data

    def getDistributorChildFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Brand', 'getDistributorChildFlag', id=identifier)
        return data

    def getDistributorFlag(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Brand', 'getDistributorFlag', id=identifier)
        return data

    def getHardware(self, identifier: int) -> list['Hardware']:
        """"""
        data = self.client.call('SoftLayer_Brand', 'getHardware', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getHasAgentAdvancedSupportFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Brand', 'getHasAgentAdvancedSupportFlag', id=identifier)
        return data

    def getHasAgentSupportFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Brand', 'getHasAgentSupportFlag', id=identifier)
        return data

    def getOpenTickets(self, identifier: int) -> list['Ticket']:
        """"""
        data = self.client.call('SoftLayer_Brand', 'getOpenTickets', id=identifier)
        from SoftLayer.sltypes.Ticket import Ticket
        return data

    def getOwnedAccounts(self, identifier: int) -> list['Account']:
        """"""
        data = self.client.call('SoftLayer_Brand', 'getOwnedAccounts', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getSecurityLevel(self, identifier: int) -> 'Security_Level':
        """"""
        data = self.client.call('SoftLayer_Brand', 'getSecurityLevel', id=identifier)
        from SoftLayer.sltypes.Security_Level import Security_Level
        return data

    def getTicketGroups(self, identifier: int) -> list['Ticket_Group']:
        """"""
        data = self.client.call('SoftLayer_Brand', 'getTicketGroups', id=identifier)
        from SoftLayer.sltypes.Ticket_Group import Ticket_Group
        return data

    def getTickets(self, identifier: int) -> list['Ticket']:
        """"""
        data = self.client.call('SoftLayer_Brand', 'getTickets', id=identifier)
        from SoftLayer.sltypes.Ticket import Ticket
        return data

    def getUsers(self, identifier: int) -> list['User_Customer']:
        """"""
        data = self.client.call('SoftLayer_Brand', 'getUsers', id=identifier)
        from SoftLayer.sltypes.User_Customer import User_Customer
        return data

    def getVirtualGuests(self, identifier: int) -> list['Virtual_Guest']:
        """"""
        data = self.client.call('SoftLayer_Brand', 'getVirtualGuests', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest import Virtual_Guest
        return data
