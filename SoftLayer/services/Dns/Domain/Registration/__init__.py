# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Dns_Domain_Registration(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Dns_Domain_Registration'
        self.client = client

    def addNameserversToDomain(
        self,
        nameservers: str,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'addNameserversToDomain',
            nameservers,
            id=identifier
        )
        
        return data


    def deleteRegisteredNameserver(
        self,
        nameserver: str,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deleteRegisteredNameserver',
            nameserver,
            id=identifier
        )
        
        return data


    def getAuthenticationCode(
        self,
        identifier: int
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getAuthenticationCode',
            id=identifier
        )
        
        return data


    def getDomainInformation(
        self,
        identifier: int
    ) -> 'SoftLayer_Container_Dns_Domain_Registration_Information':

        data = self.client.call(
            self.service,
            'getDomainInformation',
            id=identifier
        )
        from SoftLayer.datatypes.Container.Dns.Domain.Registration.Information import Information
        return Information(data)


    def getDomainNameservers(
        self,
        identifier: int
    ) -> 'list[SoftLayer_Container_Dns_Domain_Registration_Nameserver]':

        data = self.client.call(
            self.service,
            'getDomainNameservers',
            id=identifier
        )
        from SoftLayer.datatypes.Container.Dns.Domain.Registration.Nameserver import Nameserver
        return Nameserver(data)


    def getExtendedAttributes(
        self,
        domainName: str
    ) -> 'list[SoftLayer_Container_Dns_Domain_Registration_ExtendedAttribute]':

        data = self.client.call(
            self.service,
            'getExtendedAttributes',
            domainName
        )
        from SoftLayer.datatypes.Container.Dns.Domain.Registration.ExtendedAttribute import ExtendedAttribute
        return ExtendedAttribute(data)


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Dns_Domain_Registration':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Dns.Domain.Registration import Registration
        return Registration(data)


    def getRegisteredNameserver(
        self,
        identifier: int
    ) -> 'SoftLayer_Container_Dns_Domain_Registration_Nameserver':

        data = self.client.call(
            self.service,
            'getRegisteredNameserver',
            id=identifier
        )
        from SoftLayer.datatypes.Container.Dns.Domain.Registration.Nameserver import Nameserver
        return Nameserver(data)


    def getRegistrantVerificationStatusDetail(
        self,
        identifier: int
    ) -> 'SoftLayer_Container_Dns_Domain_Registration_Registrant_Verification_StatusDetail':

        data = self.client.call(
            self.service,
            'getRegistrantVerificationStatusDetail',
            id=identifier
        )
        from SoftLayer.datatypes.Container.Dns.Domain.Registration.Registrant.Verification.StatusDetail import StatusDetail
        return StatusDetail(data)


    def getTransferInformation(
        self,
        domainName: str
    ) -> 'SoftLayer_Container_Dns_Domain_Registration_Transfer_Information':

        data = self.client.call(
            self.service,
            'getTransferInformation',
            domainName
        )
        from SoftLayer.datatypes.Container.Dns.Domain.Registration.Transfer.Information import Information
        return Information(data)


    def lockDomain(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'lockDomain',
            id=identifier
        )
        
        return data


    def lookupDomain(
        self,
        domainName: str
    ) -> 'list[SoftLayer_Container_Dns_Domain_Registration_Lookup]':

        data = self.client.call(
            self.service,
            'lookupDomain',
            domainName
        )
        from SoftLayer.datatypes.Container.Dns.Domain.Registration.Lookup import Lookup
        return Lookup(data)


    def modifyContact(
        self,
        contact: 'SoftLayer_Container_Dns_Domain_Registration_Contact',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'modifyContact',
            contact,
            id=identifier
        )
        
        return data


    def modifyRegisteredNameserver(
        self,
        oldNameserver: str,
        newNameserver: str,
        ipAddress: str,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'modifyRegisteredNameserver',
            oldNameserver,
            newNameserver,
            ipAddress,
            id=identifier
        )
        
        return data


    def registerNameserver(
        self,
        nameserver: str,
        ipAddress: str,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'registerNameserver',
            nameserver,
            ipAddress,
            id=identifier
        )
        
        return data


    def removeNameserversFromDomain(
        self,
        nameservers: str,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeNameserversFromDomain',
            nameservers,
            id=identifier
        )
        
        return data


    def sendAuthenticationCode(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'sendAuthenticationCode',
            id=identifier
        )
        
        return data


    def sendRegistrantVerificationEmail(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'sendRegistrantVerificationEmail',
            id=identifier
        )
        
        return data


    def sendTransferApprovalEmail(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'sendTransferApprovalEmail',
            id=identifier
        )
        
        return data


    def setAuthenticationCode(
        self,
        authenticationCode: str,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'setAuthenticationCode',
            authenticationCode,
            id=identifier
        )
        
        return data


    def unlockDomain(
        self,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'unlockDomain',
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


    def getDomainRegistrationStatus(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Dns_Domain_Registration_Status':

        data = self.client.call(
            self.service,
            'getDomainRegistrationStatus',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Dns.Domain.Registration.Status import Status
        return Status(data)


    def getRegistrantVerificationStatus(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Dns_Domain_Registration_Registrant_Verification_Status':

        data = self.client.call(
            self.service,
            'getRegistrantVerificationStatus',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Dns.Domain.Registration.Registrant.Verification.Status import Status
        return Status(data)


    def getServiceProvider(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Service_Provider':

        data = self.client.call(
            self.service,
            'getServiceProvider',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Service.Provider import Provider
        return Provider(data)


