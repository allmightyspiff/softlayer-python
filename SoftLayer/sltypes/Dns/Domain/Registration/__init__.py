from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Dns_Domain_Registration(Entity):
    """The SoftLayer_Dns_Domain_Registration data type represents a domain registration record."""
    createDate: datetime
    domainRegistrationStatusId: int
    expireDate: datetime
    id_: int
    lockedFlag: int
    modifyDate: datetime
    name: str
    registrantVerificationStatusId: int
    serviceProviderId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Dns_Domain_Registration'

    def addNameserversToDomain(self, identifier: int, nameservers: str) -> bool:
        """Adds nameservers to a domain."""
        data = self.client.call('SoftLayer_Dns_Domain_Registration', 'addNameserversToDomain', nameservers, id=identifier)
        return data

    def deleteRegisteredNameserver(self, identifier: int, nameserver: str) -> bool:
        """Deletes a registered nameserver."""
        data = self.client.call('SoftLayer_Dns_Domain_Registration', 'deleteRegisteredNameserver', nameserver, id=identifier)
        return data

    def getAuthenticationCode(self, identifier: int) -> str:
        """Get the authentication code for a domain."""
        data = self.client.call('SoftLayer_Dns_Domain_Registration', 'getAuthenticationCode', id=identifier)
        return data

    def getDomainInformation(self, identifier: int) -> 'Container_Dns_Domain_Registration_Information':
        """Retrieve all domain information."""
        data = self.client.call('SoftLayer_Dns_Domain_Registration', 'getDomainInformation', id=identifier)
        from SoftLayer.sltypes.Container_Dns_Domain_Registration_Information import Container_Dns_Domain_Registration_Information
        return data

    def getDomainNameservers(self, identifier: int) -> list['Container_Dns_Domain_Registration_Nameserver']:
        """Retrieve domain nameservers."""
        data = self.client.call('SoftLayer_Dns_Domain_Registration', 'getDomainNameservers', id=identifier)
        from SoftLayer.sltypes.Container_Dns_Domain_Registration_Nameserver import Container_Dns_Domain_Registration_Nameserver
        return data

    def getExtendedAttributes(self, domainName: str) -> list['Container_Dns_Domain_Registration_ExtendedAttribute']:
        """Retrieves extended attributes."""
        data = self.client.call('SoftLayer_Dns_Domain_Registration', 'getExtendedAttributes', domainName)
        from SoftLayer.sltypes.Container_Dns_Domain_Registration_ExtendedAttribute import Container_Dns_Domain_Registration_ExtendedAttribute
        return data

    def getObject(self, identifier: int) -> 'Dns_Domain_Registration':
        """Retrieve a SoftLayer_Dns_Domain_Registration record."""
        data = self.client.call('SoftLayer_Dns_Domain_Registration', 'getObject', id=identifier)
        from SoftLayer.sltypes.Dns_Domain_Registration import Dns_Domain_Registration
        return data

    def getRegisteredNameserver(self, identifier: int) -> 'Container_Dns_Domain_Registration_Nameserver':
        """Retrieves a registered nameserver."""
        data = self.client.call('SoftLayer_Dns_Domain_Registration', 'getRegisteredNameserver', id=identifier)
        from SoftLayer.sltypes.Container_Dns_Domain_Registration_Nameserver import Container_Dns_Domain_Registration_Nameserver
        return data

    def getRegistrantVerificationStatusDetail(self, identifier: int) -> 'Container_Dns_Domain_Registration_Registrant_Verification_StatusDetail':
        """Retrieves registrant verification status."""
        data = self.client.call('SoftLayer_Dns_Domain_Registration', 'getRegistrantVerificationStatusDetail', id=identifier)
        from SoftLayer.sltypes.Container_Dns_Domain_Registration_Registrant_Verification_StatusDetail import Container_Dns_Domain_Registration_Registrant_Verification_StatusDetail
        return data

    def getTransferInformation(self, domainName: str) -> 'Container_Dns_Domain_Registration_Transfer_Information':
        """Retrieve domain transfer information."""
        data = self.client.call('SoftLayer_Dns_Domain_Registration', 'getTransferInformation', domainName)
        from SoftLayer.sltypes.Container_Dns_Domain_Registration_Transfer_Information import Container_Dns_Domain_Registration_Transfer_Information
        return data

    def lockDomain(self, identifier: int) -> bool:
        """Locks a domain."""
        data = self.client.call('SoftLayer_Dns_Domain_Registration', 'lockDomain', id=identifier)
        return data

    def lookupDomain(self, domainName: str) -> list['Container_Dns_Domain_Registration_Lookup']:
        """Lookup available domains and suggests other similar domain names"""
        data = self.client.call('SoftLayer_Dns_Domain_Registration', 'lookupDomain', domainName)
        from SoftLayer.sltypes.Container_Dns_Domain_Registration_Lookup import Container_Dns_Domain_Registration_Lookup
        return data

    def modifyContact(self, identifier: int, contact: 'Container_Dns_Domain_Registration_Contact') -> bool:
        """Modifies contact information for a domain."""
        data = self.client.call('SoftLayer_Dns_Domain_Registration', 'modifyContact', contact, id=identifier)
        return data

    def modifyRegisteredNameserver(self, identifier: int, oldNameserver: str, newNameserver: str, ipAddress: str) -> bool:
        """Modifies a registered nameserver."""
        data = self.client.call('SoftLayer_Dns_Domain_Registration', 'modifyRegisteredNameserver', oldNameserver, newNameserver, ipAddress, id=identifier)
        return data

    def registerNameserver(self, identifier: int, nameserver: str, ipAddress: str) -> bool:
        """Creates a nameserver."""
        data = self.client.call('SoftLayer_Dns_Domain_Registration', 'registerNameserver', nameserver, ipAddress, id=identifier)
        return data

    def removeNameserversFromDomain(self, identifier: int, nameservers: str) -> bool:
        """Removes nameservers from a domain."""
        data = self.client.call('SoftLayer_Dns_Domain_Registration', 'removeNameserversFromDomain', nameservers, id=identifier)
        return data

    def sendAuthenticationCode(self, identifier: int) -> bool:
        """Sends the authentication code"""
        data = self.client.call('SoftLayer_Dns_Domain_Registration', 'sendAuthenticationCode', id=identifier)
        return data

    def sendRegistrantVerificationEmail(self, identifier: int) -> bool:
        """Sends verification email to the registrant."""
        data = self.client.call('SoftLayer_Dns_Domain_Registration', 'sendRegistrantVerificationEmail', id=identifier)
        return data

    def sendTransferApprovalEmail(self, identifier: int) -> bool:
        """Resends a transfer approval email message."""
        data = self.client.call('SoftLayer_Dns_Domain_Registration', 'sendTransferApprovalEmail', id=identifier)
        return data

    def setAuthenticationCode(self, identifier: int, authenticationCode: str) -> bool:
        """Sets the authentication code for a domain."""
        data = self.client.call('SoftLayer_Dns_Domain_Registration', 'setAuthenticationCode', authenticationCode, id=identifier)
        return data

    def unlockDomain(self, identifier: int) -> bool:
        """Unlocks a domain."""
        data = self.client.call('SoftLayer_Dns_Domain_Registration', 'unlockDomain', id=identifier)
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Dns_Domain_Registration', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getDomainRegistrationStatus(self, identifier: int) -> 'Dns_Domain_Registration_Status':
        """"""
        data = self.client.call('SoftLayer_Dns_Domain_Registration', 'getDomainRegistrationStatus', id=identifier)
        from SoftLayer.sltypes.Dns_Domain_Registration_Status import Dns_Domain_Registration_Status
        return data

    def getRegistrantVerificationStatus(self, identifier: int) -> 'Dns_Domain_Registration_Registrant_Verification_Status':
        """"""
        data = self.client.call('SoftLayer_Dns_Domain_Registration', 'getRegistrantVerificationStatus', id=identifier)
        from SoftLayer.sltypes.Dns_Domain_Registration_Registrant_Verification_Status import Dns_Domain_Registration_Registrant_Verification_Status
        return data

    def getServiceProvider(self, identifier: int) -> 'Service_Provider':
        """"""
        data = self.client.call('SoftLayer_Dns_Domain_Registration', 'getServiceProvider', id=identifier)
        from SoftLayer.sltypes.Service_Provider import Service_Provider
        return data
