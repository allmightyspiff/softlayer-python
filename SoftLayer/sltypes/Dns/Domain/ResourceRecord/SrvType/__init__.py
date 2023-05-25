from SoftLayer.sltypes.Dns.Domain.ResourceRecord import Dns_Domain_ResourceRecord
from SoftLayer.sltypes.Dns_Domain_ResourceRecord import Dns_Domain_ResourceRecord
from SoftLayer import BaseClient

class Dns_Domain_ResourceRecord_SrvType(Dns_Domain_ResourceRecord):
    """SoftLayer_Dns_Domain_ResourceRecord_SrvType is a SoftLayer_Dns_Domain_ResourceRecord object whose ''type''
property is set to "srv" and defines a DNS SRV record on a SoftLayer hosted domain."""
    port: int
    priority: int
    protocol: str
    service: str
    weight: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Dns_Domain_ResourceRecord_SrvType'

    def createObject(self, templateObject: 'Dns_Domain_ResourceRecord_SrvType') -> 'Dns_Domain_ResourceRecord_SrvType':
        """Create an SRV record."""
        data = self.client.call('SoftLayer_Dns_Domain_ResourceRecord_SrvType', 'createObject', templateObject)
        from SoftLayer.sltypes.Dns_Domain_ResourceRecord_SrvType import Dns_Domain_ResourceRecord_SrvType
        return data

    def createObjects(self, templateObjects: 'Dns_Domain_ResourceRecord') -> list['Dns_Domain_ResourceRecord']:
        """Create multiple SRV records."""
        data = self.client.call('SoftLayer_Dns_Domain_ResourceRecord_SrvType', 'createObjects', templateObjects)
        from SoftLayer.sltypes.Dns_Domain_ResourceRecord import Dns_Domain_ResourceRecord
        return data

    def deleteObject(self, identifier: int) -> bool:
        """Delete a domain's SRV record."""
        data = self.client.call('SoftLayer_Dns_Domain_ResourceRecord_SrvType', 'deleteObject', id=identifier)
        return data

    def deleteObjects(self, templateObjects: 'Dns_Domain_ResourceRecord_SrvType') -> bool:
        """Delete multiple SRV records from a domain."""
        data = self.client.call('SoftLayer_Dns_Domain_ResourceRecord_SrvType', 'deleteObjects', templateObjects)
        return data

    def editObject(self, identifier: int, templateObject: 'Dns_Domain_ResourceRecord_SrvType') -> bool:
        """Edit a domain's SRV record."""
        data = self.client.call('SoftLayer_Dns_Domain_ResourceRecord_SrvType', 'editObject', templateObject, id=identifier)
        return data

    def editObjects(self, templateObjects: 'Dns_Domain_ResourceRecord_SrvType') -> bool:
        """Edit multiple domain SRV records."""
        data = self.client.call('SoftLayer_Dns_Domain_ResourceRecord_SrvType', 'editObjects', templateObjects)
        return data

    def getObject(self, identifier: int) -> 'Dns_Domain_ResourceRecord_SrvType':
        """Retrieve a SoftLayer_Dns_Domain_ResourceRecord_SrvType record."""
        data = self.client.call('SoftLayer_Dns_Domain_ResourceRecord_SrvType', 'getObject', id=identifier)
        from SoftLayer.sltypes.Dns_Domain_ResourceRecord_SrvType import Dns_Domain_ResourceRecord_SrvType
        return data
