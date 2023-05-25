from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Subnet_Rwhois_Data(Entity):
    """Every SoftLayer customer account has contact information associated with it for reverse WHOIS purposes. An
account's RWHOIS data, modeled by the SoftLayer_Network_Subnet_Rwhois_Data data type, is used by SoftLayer's
reverse WHOIS server as well as for SWIP transactions. SoftLayer's reverse WHOIS servers respond to WHOIS
queries for IP addresses belonging to a customer's servers, returning this RWHOIS data.   A SoftLayer
customer's RWHOIS data may not necessarily match their account or portal users' contact information."""
    abuseEmail: str
    accountId: int
    address1: str
    address2: str
    city: str
    companyName: str
    country: str
    createDate: datetime
    firstName: str
    id_: int
    lastName: str
    modifyDate: datetime
    postalCode: str
    privateResidenceFlag: bool
    state: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Subnet_Rwhois_Data'

    def editObject(self, identifier: int, templateObject: 'Network_Subnet_Rwhois_Data') -> bool:
        """Edit the RWHOIS record by passing in a modified version of the record object. All fields are editable. The
fields are as follows:  * companyName * firstName * lastName * city * country * postalCode * abuseEmail *
address1"""
        data = self.client.call('SoftLayer_Network_Subnet_Rwhois_Data', 'editObject', templateObject, id=identifier)
        return data

    def getObject(self, identifier: int) -> 'Network_Subnet_Rwhois_Data':
        """Retrieve a SoftLayer_Network_Subnet_Rwhois_Data record."""
        data = self.client.call('SoftLayer_Network_Subnet_Rwhois_Data', 'getObject', id=identifier)
        from SoftLayer.sltypes.Network_Subnet_Rwhois_Data import Network_Subnet_Rwhois_Data
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Network_Subnet_Rwhois_Data', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data
