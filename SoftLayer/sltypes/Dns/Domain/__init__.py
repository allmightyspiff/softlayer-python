from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Dns_Domain(Entity):
    """The SoftLayer_Dns_Domain data type represents a single DNS domain record hosted on the SoftLayer nameservers.
Domains contain general information about the domain name such as name and serial. Individual records such as
A, AAAA, CTYPE, and MX records are stored in the domain's associated [[SoftLayer_Dns_Domain_ResourceRecord
(type)|SoftLayer_Dns_Domain_ResourceRecord]] records."""
    id_: int
    name: str
    serial: int
    updateDate: datetime

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Dns_Domain'

    def createARecord(self, identifier: int, host: str, data: str, ttl: int) -> 'Dns_Domain_ResourceRecord_AType':
        """Create an A record on a domain."""
        data = self.client.call('SoftLayer_Dns_Domain', 'createARecord', host, data, ttl, id=identifier)
        from SoftLayer.sltypes.Dns_Domain_ResourceRecord_AType import Dns_Domain_ResourceRecord_AType
        return data

    def createAaaaRecord(self, identifier: int, host: str, data: str, ttl: int) -> 'Dns_Domain_ResourceRecord_AaaaType':
        """Create an AAAA record on a domain."""
        data = self.client.call('SoftLayer_Dns_Domain', 'createAaaaRecord', host, data, ttl, id=identifier)
        from SoftLayer.sltypes.Dns_Domain_ResourceRecord_AaaaType import Dns_Domain_ResourceRecord_AaaaType
        return data

    def createCnameRecord(self, identifier: int, host: str, data: str, ttl: int) -> 'Dns_Domain_ResourceRecord_CnameType':
        """Create a CNAME record on a domain."""
        data = self.client.call('SoftLayer_Dns_Domain', 'createCnameRecord', host, data, ttl, id=identifier)
        from SoftLayer.sltypes.Dns_Domain_ResourceRecord_CnameType import Dns_Domain_ResourceRecord_CnameType
        return data

    def createMxRecord(self, identifier: int, host: str, data: str, ttl: int, mxPriority: int) -> 'Dns_Domain_ResourceRecord_MxType':
        """Create an MX record on a domain."""
        data = self.client.call('SoftLayer_Dns_Domain', 'createMxRecord', host, data, ttl, mxPriority, id=identifier)
        from SoftLayer.sltypes.Dns_Domain_ResourceRecord_MxType import Dns_Domain_ResourceRecord_MxType
        return data

    def createNsRecord(self, identifier: int, host: str, data: str, ttl: int) -> 'Dns_Domain_ResourceRecord_NsType':
        """Create an NS record on a domain."""
        data = self.client.call('SoftLayer_Dns_Domain', 'createNsRecord', host, data, ttl, id=identifier)
        from SoftLayer.sltypes.Dns_Domain_ResourceRecord_NsType import Dns_Domain_ResourceRecord_NsType
        return data

    def createObject(self, templateObject: 'Dns_Domain') -> 'Dns_Domain':
        """Create a new domain."""
        data = self.client.call('SoftLayer_Dns_Domain', 'createObject', templateObject)
        from SoftLayer.sltypes.Dns_Domain import Dns_Domain
        return data

    def createObjects(self, templateObjects: 'Dns_Domain') -> list['Dns_Domain']:
        """Create multiple domains at once."""
        data = self.client.call('SoftLayer_Dns_Domain', 'createObjects', templateObjects)
        from SoftLayer.sltypes.Dns_Domain import Dns_Domain
        return data

    def createPtrRecord(self, ipAddress: str, ptrRecord: str, ttl: int) -> 'Dns_Domain_ResourceRecord':
        """Edit the PTR record for a single IP address."""
        data = self.client.call('SoftLayer_Dns_Domain', 'createPtrRecord', ipAddress, ptrRecord, ttl)
        from SoftLayer.sltypes.Dns_Domain_ResourceRecord import Dns_Domain_ResourceRecord
        return data

    def createSpfRecord(self, identifier: int, host: str, data: str, ttl: int) -> 'Dns_Domain_ResourceRecord_SpfType':
        """Create an SPF record on a domain."""
        data = self.client.call('SoftLayer_Dns_Domain', 'createSpfRecord', host, data, ttl, id=identifier)
        from SoftLayer.sltypes.Dns_Domain_ResourceRecord_SpfType import Dns_Domain_ResourceRecord_SpfType
        return data

    def createTxtRecord(self, identifier: int, host: str, data: str, ttl: int) -> 'Dns_Domain_ResourceRecord_TxtType':
        """Create a TXT record on a domain."""
        data = self.client.call('SoftLayer_Dns_Domain', 'createTxtRecord', host, data, ttl, id=identifier)
        from SoftLayer.sltypes.Dns_Domain_ResourceRecord_TxtType import Dns_Domain_ResourceRecord_TxtType
        return data

    def deleteObject(self, identifier: int) -> bool:
        """Remove a domain."""
        data = self.client.call('SoftLayer_Dns_Domain', 'deleteObject', id=identifier)
        return data

    def getByDomainName(self, name: str) -> list['Dns_Domain']:
        """Search for domains by name."""
        data = self.client.call('SoftLayer_Dns_Domain', 'getByDomainName', name)
        from SoftLayer.sltypes.Dns_Domain import Dns_Domain
        return data

    def getObject(self, identifier: int) -> 'Dns_Domain':
        """Retrieve a SoftLayer_Dns_Domain record."""
        data = self.client.call('SoftLayer_Dns_Domain', 'getObject', id=identifier)
        from SoftLayer.sltypes.Dns_Domain import Dns_Domain
        return data

    def getZoneFileContents(self, identifier: int) -> str:
        """Return a domain's data formatted as zone file text."""
        data = self.client.call('SoftLayer_Dns_Domain', 'getZoneFileContents', id=identifier)
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Dns_Domain', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getManagedResourceFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Dns_Domain', 'getManagedResourceFlag', id=identifier)
        return data

    def getResourceRecords(self, identifier: int) -> list['Dns_Domain_ResourceRecord']:
        """"""
        data = self.client.call('SoftLayer_Dns_Domain', 'getResourceRecords', id=identifier)
        from SoftLayer.sltypes.Dns_Domain_ResourceRecord import Dns_Domain_ResourceRecord
        return data

    def getSecondary(self, identifier: int) -> 'Dns_Secondary':
        """"""
        data = self.client.call('SoftLayer_Dns_Domain', 'getSecondary', id=identifier)
        from SoftLayer.sltypes.Dns_Secondary import Dns_Secondary
        return data

    def getSoaResourceRecord(self, identifier: int) -> 'Dns_Domain_ResourceRecord_SoaType':
        """"""
        data = self.client.call('SoftLayer_Dns_Domain', 'getSoaResourceRecord', id=identifier)
        from SoftLayer.sltypes.Dns_Domain_ResourceRecord_SoaType import Dns_Domain_ResourceRecord_SoaType
        return data
