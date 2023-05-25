from SoftLayer.sltypes.Dns.Domain.ResourceRecord import Dns_Domain_ResourceRecord
from SoftLayer.sltypes.Dns_Domain_ResourceRecord import Dns_Domain_ResourceRecord
from SoftLayer import BaseClient

class Dns_Domain_ResourceRecord_MxType(Dns_Domain_ResourceRecord):
    """SoftLayer_Dns_Domain_ResourceRecord_MxType is a SoftLayer_Dns_Domain_ResourceRecord object whose ''type''
property is set to "mx" and used to describe MX resource records. MX records control which hosts are
responsible as mail exchangers for a domain. For instance, in the domain example.org, an MX record whose host
is "@" and data is "mail" says that the host "mail.example.org" is responsible for handling mail for
example.org. That means mail sent to users @example.org are delivered to mail.example.org.   Domains can have
more than one MX record if it uses more than one server to send mail through. Multiple MX records are denoted
by their priority, defined by the mxPriority property.   MX records must be defined for hosts with
accompanying A or AAAA resource records. They may not point mail towards a host defined by a CNAME record."""

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Dns_Domain_ResourceRecord_MxType'

    def createObject(self, templateObject: 'Dns_Domain_ResourceRecord_MxType') -> 'Dns_Domain_ResourceRecord_MxType':
        """Create an MX record."""
        data = self.client.call('SoftLayer_Dns_Domain_ResourceRecord_MxType', 'createObject', templateObject)
        return data

    def createObjects(self, templateObjects: 'Dns_Domain_ResourceRecord') -> list['Dns_Domain_ResourceRecord']:
        """Create multiple MX records."""
        data = self.client.call('SoftLayer_Dns_Domain_ResourceRecord_MxType', 'createObjects', templateObjects)
        from SoftLayer.sltypes.Dns_Domain_ResourceRecord import Dns_Domain_ResourceRecord
        return data

    def deleteObject(self, identifier: int) -> bool:
        """Delete a domain's MX record."""
        data = self.client.call('SoftLayer_Dns_Domain_ResourceRecord_MxType', 'deleteObject', id=identifier)
        return data

    def deleteObjects(self, templateObjects: 'Dns_Domain_ResourceRecord_MxType') -> bool:
        """Delete multiple MX records from a domain."""
        data = self.client.call('SoftLayer_Dns_Domain_ResourceRecord_MxType', 'deleteObjects', templateObjects)
        return data

    def editObject(self, identifier: int, templateObject: 'Dns_Domain_ResourceRecord_MxType') -> bool:
        """Edit a domain's MX record."""
        data = self.client.call('SoftLayer_Dns_Domain_ResourceRecord_MxType', 'editObject', templateObject, id=identifier)
        return data

    def editObjects(self, templateObjects: 'Dns_Domain_ResourceRecord_MxType') -> bool:
        """Edit multiple domain MX records."""
        data = self.client.call('SoftLayer_Dns_Domain_ResourceRecord_MxType', 'editObjects', templateObjects)
        return data

    def getObject(self, identifier: int) -> 'Dns_Domain_ResourceRecord_MxType':
        """Retrieve a SoftLayer_Dns_Domain_ResourceRecord_MxType record."""
        data = self.client.call('SoftLayer_Dns_Domain_ResourceRecord_MxType', 'getObject', id=identifier)
        return data
