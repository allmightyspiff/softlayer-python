from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Subnet_Swip_Transaction(Entity):
    """**DEPRECATED** The SoftLayer_Network_Subnet_Swip_Transaction data type contains basic information tracked at
SoftLayer to allow automation of Swip creation, update, and removal requests.  A specific transaction is
attached to an accountId and a subnetId. This also contains a "Status Name" which tells the customer what the
transaction is doing:    * REQUEST QUEUED:  Request is queued up to be sent to ARIN * REQUEST SENT:  The
email request has been sent to ARIN * REQUEST CONFIRMED:  ARIN has confirmed that the request is good, and
should be available in 24 hours * OK:  The subnet has been checked with WHOIS and it the SWIP transaction has
completed correctly * REMOVE QUEUED:  A subnet is queued to be removed from ARIN's systems * REMOVE SENT:
The removal email request has been sent to ARIN * REMOVE CONFIRMED:  ARIN has confirmed that the removal
request is good, and the subnet should be clear in WHOIS in 24 hours * DELETED:  This specific SWIP
Transaction has been removed from ARIN and is no longer in effect * SOFTLAYER MANUALLY PROCESSING:  Sometimes
a request doesn't go through correctly and has to be manually processed by SoftLayer.  This may take some
time."""
    id_: int
    statusName: str
    subnetId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Subnet_Swip_Transaction'

    def findMyTransactions(self) -> list['Network_Subnet_Swip_Transaction']:
        """returns SWIP transaction objects that are currently in transaction with ARIN."""
        data = self.client.call('SoftLayer_Network_Subnet_Swip_Transaction', 'findMyTransactions')
        from SoftLayer.sltypes.Network_Subnet_Swip_Transaction import Network_Subnet_Swip_Transaction
        return data

    def getObject(self, identifier: int) -> 'Network_Subnet_Swip_Transaction':
        """Retrieve a SoftLayer_Network_Subnet_Swip_Transaction record."""
        data = self.client.call('SoftLayer_Network_Subnet_Swip_Transaction', 'getObject', id=identifier)
        from SoftLayer.sltypes.Network_Subnet_Swip_Transaction import Network_Subnet_Swip_Transaction
        return data

    def removeAllSubnetSwips(self) -> int:
        """Removes registration information from ARIN for all your subnets"""
        data = self.client.call('SoftLayer_Network_Subnet_Swip_Transaction', 'removeAllSubnetSwips')
        return data

    def removeSwipData(self, identifier: int) -> bool:
        """Deletes registration information from ARIN for a single subnet"""
        data = self.client.call('SoftLayer_Network_Subnet_Swip_Transaction', 'removeSwipData', id=identifier)
        return data

    def resendSwipData(self, identifier: int) -> bool:
        """Sends updated RWHOIS information to ARIN for a single subnet."""
        data = self.client.call('SoftLayer_Network_Subnet_Swip_Transaction', 'resendSwipData', id=identifier)
        return data

    def swipAllSubnets(self) -> int:
        """create SWIP transactions for all subnets that do not already have a SWIP transaction in progress."""
        data = self.client.call('SoftLayer_Network_Subnet_Swip_Transaction', 'swipAllSubnets')
        return data

    def updateAllSubnetSwips(self) -> int:
        """Update all subnets on the account with an "OK" status."""
        data = self.client.call('SoftLayer_Network_Subnet_Swip_Transaction', 'updateAllSubnetSwips')
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Network_Subnet_Swip_Transaction', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getSubnet(self, identifier: int) -> 'Network_Subnet':
        """"""
        data = self.client.call('SoftLayer_Network_Subnet_Swip_Transaction', 'getSubnet', id=identifier)
        from SoftLayer.sltypes.Network_Subnet import Network_Subnet
        return data
