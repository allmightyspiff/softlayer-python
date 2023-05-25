from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Dns_Domain_ResourceRecord(Entity):
    """The SoftLayer_Dns_Domain_ResourceRecord data type represents a single resource record entry in a SoftLayer
hosted domain. Each resource record contains a ''host'' and ''data'' property, defining a resource's name and
it's target data. Domains contain multiple types of resource records. The ''type'' property separates out
resource records by type. ''Type'' can take one of the following values:  * '''"a"''' for
[[SoftLayer_Dns_Domain_ResourceRecord_AType|address]] records * '''"aaaa"''' for
[[SoftLayer_Dns_Domain_ResourceRecord_AaaaType|address]] records * '''"cname"''' for
[[SoftLayer_Dns_Domain_ResourceRecord_CnameType|canonical name]] records * '''"mx"''' for
[[SoftLayer_Dns_Domain_ResourceRecord_MxType|mail exchanger]] records * '''"ns"''' for
[[SoftLayer_Dns_Domain_ResourceRecord_NsType|name server]] records * '''"ptr"''' for
[[SoftLayer_Dns_Domain_ResourceRecord_PtrType|pointer]] records in reverse domains * '''"soa"''' for a
domain's [[SoftLayer_Dns_Domain_ResourceRecord_SoaType|start of authority]] record * '''"spf"''' for
[[SoftLayer_Dns_Domain_ResourceRecord_SpfType|sender policy framework]] records * '''"srv"''' for
[[SoftLayer_Dns_Domain_ResourceRecord_SrvType|service]] records * '''"txt"''' for
[[SoftLayer_Dns_Domain_ResourceRecord_TxtType|text]] records   As ''SoftLayer_Dns_Domain_ResourceRecord''
objects are created and loaded, the API verifies the ''type'' property and casts the object as the
appropriate type."""
    data: str
    domainId: int
    expire: int
    host: str
    id_: int
    minimum: int
    mxPriority: int
    refresh: int
    responsiblePerson: str
    retry: int
    ttl: int
    type_: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Dns_Domain_ResourceRecord'

    def createObject(self, templateObject: 'Dns_Domain_ResourceRecord') -> 'Dns_Domain_ResourceRecord':
        """Create a domain's resource record."""
        data = self.client.call('SoftLayer_Dns_Domain_ResourceRecord', 'createObject', templateObject)
        from SoftLayer.sltypes.Dns_Domain_ResourceRecord import Dns_Domain_ResourceRecord
        return data

    def createObjects(self, templateObjects: 'Dns_Domain_ResourceRecord') -> list['Dns_Domain_ResourceRecord']:
        """Create multiple domain resource records."""
        data = self.client.call('SoftLayer_Dns_Domain_ResourceRecord', 'createObjects', templateObjects)
        from SoftLayer.sltypes.Dns_Domain_ResourceRecord import Dns_Domain_ResourceRecord
        return data

    def deleteObject(self, identifier: int) -> bool:
        """Delete a domain's resource record."""
        data = self.client.call('SoftLayer_Dns_Domain_ResourceRecord', 'deleteObject', id=identifier)
        return data

    def deleteObjects(self, templateObjects: 'Dns_Domain_ResourceRecord') -> bool:
        """Delete multiple resource records from a domain."""
        data = self.client.call('SoftLayer_Dns_Domain_ResourceRecord', 'deleteObjects', templateObjects)
        return data

    def editObject(self, identifier: int, templateObject: 'Dns_Domain_ResourceRecord') -> bool:
        """Edit a domain's resource record."""
        data = self.client.call('SoftLayer_Dns_Domain_ResourceRecord', 'editObject', templateObject, id=identifier)
        return data

    def editObjects(self, templateObjects: 'Dns_Domain_ResourceRecord') -> bool:
        """Edit multiple domain resource records."""
        data = self.client.call('SoftLayer_Dns_Domain_ResourceRecord', 'editObjects', templateObjects)
        return data

    def getObject(self, identifier: int) -> 'Dns_Domain_ResourceRecord':
        """Retrieve a SoftLayer_Dns_Domain_ResourceRecord record."""
        data = self.client.call('SoftLayer_Dns_Domain_ResourceRecord', 'getObject', id=identifier)
        from SoftLayer.sltypes.Dns_Domain_ResourceRecord import Dns_Domain_ResourceRecord
        return data

    def getDomain(self, identifier: int) -> 'Dns_Domain':
        """"""
        data = self.client.call('SoftLayer_Dns_Domain_ResourceRecord', 'getDomain', id=identifier)
        from SoftLayer.sltypes.Dns_Domain import Dns_Domain
        return data
