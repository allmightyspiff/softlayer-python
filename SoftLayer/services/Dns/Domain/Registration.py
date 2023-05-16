# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Dns_Domain_Registration(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Dns_Domain_Registration'
        self.client = client

    def addNameserversToDomain(
        self,
        nameservers: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'addNameserversToDomain',
            nameservers
        )
        
        return data


    def deleteRegisteredNameserver(
        self,
        nameserver: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deleteRegisteredNameserver',
            nameserver
        )
        
        return data


    def getAuthenticationCode(
        self,
        
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getAuthenticationCode',
            
        )
        
        return data


    def getDomainInformation(
        self,
        
    ) -> 'SoftLayer_Container_Dns_Domain_Registration_Information':

        data = self.client.call(
            self.service,
            'getDomainInformation',
            
        )
        from SoftLayer.datatypes.Container.Dns.Domain.Registration.Information import Information
        return Information(data)


    def getDomainNameservers(
        self,
        
    ) -> 'list[SoftLayer_Container_Dns_Domain_Registration_Nameserver]':

        data = self.client.call(
            self.service,
            'getDomainNameservers',
            
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
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Dns_Domain_Registration':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Dns.Domain.Registration import Registration
        return Registration(data)


    def getRegisteredNameserver(
        self,
        
    ) -> 'SoftLayer_Container_Dns_Domain_Registration_Nameserver':

        data = self.client.call(
            self.service,
            'getRegisteredNameserver',
            
        )
        from SoftLayer.datatypes.Container.Dns.Domain.Registration.Nameserver import Nameserver
        return Nameserver(data)


    def getRegistrantVerificationStatusDetail(
        self,
        
    ) -> 'SoftLayer_Container_Dns_Domain_Registration_Registrant_Verification_StatusDetail':

        data = self.client.call(
            self.service,
            'getRegistrantVerificationStatusDetail',
            
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
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'lockDomain',
            
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
        contact: SoftLayer_Container_Dns_Domain_Registration_Contact
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'modifyContact',
            contact
        )
        
        return data


    def modifyRegisteredNameserver(
        self,
        oldNameserver: str,
        newNameserver: str,
        ipAddress: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'modifyRegisteredNameserver',
            oldNameserver,
            newNameserver,
            ipAddress
        )
        
        return data


    def registerNameserver(
        self,
        nameserver: str,
        ipAddress: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'registerNameserver',
            nameserver,
            ipAddress
        )
        
        return data


    def removeNameserversFromDomain(
        self,
        nameservers: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeNameserversFromDomain',
            nameservers
        )
        
        return data


    def sendAuthenticationCode(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'sendAuthenticationCode',
            
        )
        
        return data


    def sendRegistrantVerificationEmail(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'sendRegistrantVerificationEmail',
            
        )
        
        return data


    def sendTransferApprovalEmail(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'sendTransferApprovalEmail',
            
        )
        
        return data


    def setAuthenticationCode(
        self,
        authenticationCode: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'setAuthenticationCode',
            authenticationCode
        )
        
        return data


    def unlockDomain(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'unlockDomain',
            
        )
        
        return data


    def getAccount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account':

        data = self.client.call(
            self.service,
            'getAccount',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account import Account
        return Account(data)


    def getDomainRegistrationStatus(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Dns_Domain_Registration_Status':

        data = self.client.call(
            self.service,
            'getDomainRegistrationStatus',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Dns.Domain.Registration.Status import Status
        return Status(data)


    def getRegistrantVerificationStatus(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Dns_Domain_Registration_Registrant_Verification_Status':

        data = self.client.call(
            self.service,
            'getRegistrantVerificationStatus',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Dns.Domain.Registration.Registrant.Verification.Status import Status
        return Status(data)


    def getServiceProvider(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Service_Provider':

        data = self.client.call(
            self.service,
            'getServiceProvider',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Service.Provider import Provider
        return Provider(data)


