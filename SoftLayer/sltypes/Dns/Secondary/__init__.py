from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Dns_Secondary(Entity):
    """The SoftLayer_Dns_Secondary data type contains information on a single secondary DNS zone which is managed
through SoftLayer's zone transfer service. Domains created via zone transfer may not be modified by the
SoftLayer portal or API."""
    createDate: datetime
    id_: int
    lastUpdate: datetime
    masterIpAddress: str
    statusId: int
    statusText: str
    transferFrequency: int
    zoneName: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Dns_Secondary'

    def convertToPrimary(self, identifier: int) -> bool:
        """Convert a secondary DNS record into a primary DNS record."""
        data = self.client.call('SoftLayer_Dns_Secondary', 'convertToPrimary', id=identifier)
        return data

    def createObject(self, templateObject: 'Dns_Secondary') -> 'Dns_Secondary':
        """Create a secondary DNS record."""
        data = self.client.call('SoftLayer_Dns_Secondary', 'createObject', templateObject)
        return data

    def createObjects(self, templateObjects: 'Dns_Secondary') -> list['Dns_Secondary']:
        """Create multiple secondary DNS records."""
        data = self.client.call('SoftLayer_Dns_Secondary', 'createObjects', templateObjects)
        return data

    def deleteObject(self, identifier: int) -> bool:
        """Delete a secondary DNS record"""
        data = self.client.call('SoftLayer_Dns_Secondary', 'deleteObject', id=identifier)
        return data

    def editObject(self, identifier: int, templateObject: 'Dns_Secondary') -> bool:
        """Edit a secondary DNS record."""
        data = self.client.call('SoftLayer_Dns_Secondary', 'editObject', templateObject, id=identifier)
        return data

    def getByDomainName(self, name: str) -> list['Dns_Secondary']:
        """Search for secondary domains by name."""
        data = self.client.call('SoftLayer_Dns_Secondary', 'getByDomainName', name)
        return data

    def getObject(self, identifier: int) -> 'Dns_Secondary':
        """Retrieve a SoftLayer_Dns_Secondary record."""
        data = self.client.call('SoftLayer_Dns_Secondary', 'getObject', id=identifier)
        return data

    def transferNow(self, identifier: int) -> bool:
        """Initiate a zone transfer for a secondary DNS record."""
        data = self.client.call('SoftLayer_Dns_Secondary', 'transferNow', id=identifier)
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Dns_Secondary', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getDomain(self, identifier: int) -> 'Dns_Domain':
        """"""
        data = self.client.call('SoftLayer_Dns_Secondary', 'getDomain', id=identifier)
        from SoftLayer.sltypes.Dns_Domain import Dns_Domain
        return data

    def getErrorMessages(self, identifier: int) -> list['Dns_Message']:
        """"""
        data = self.client.call('SoftLayer_Dns_Secondary', 'getErrorMessages', id=identifier)
        from SoftLayer.sltypes.Dns_Message import Dns_Message
        return data

    def getStatus(self, identifier: int) -> 'Dns_Status':
        """"""
        data = self.client.call('SoftLayer_Dns_Secondary', 'getStatus', id=identifier)
        from SoftLayer.sltypes.Dns_Status import Dns_Status
        return data
