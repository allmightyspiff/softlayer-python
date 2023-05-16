# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Dns_Domain_Registration(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Dns_Domain_Registration'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
    def getAuthenticationCode(
        self,
        
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getAuthenticationCode',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getDomainInformation(
        self,
        
    ) -> 'SoftLayer_Container_Dns_Domain_Registration_Information':
        data = self.client.call(
            self.service,
            'getDomainInformation',
            
        )
        from SoftLayer.datatypes.Container.Dns.Domain.Registration.Information import Information
        return SL_Information(data)

# This file was automatically generated with tools/generateTypes.py
    def getDomainNameservers(
        self,
        
    ) -> 'list[SoftLayer_Container_Dns_Domain_Registration_Nameserver]':
        data = self.client.call(
            self.service,
            'getDomainNameservers',
            
        )
        from SoftLayer.datatypes.Container.Dns.Domain.Registration.Nameserver import Nameserver
        return SL_Nameserver(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_ExtendedAttribute(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Registration(data)

# This file was automatically generated with tools/generateTypes.py
    def getRegisteredNameserver(
        self,
        
    ) -> 'SoftLayer_Container_Dns_Domain_Registration_Nameserver':
        data = self.client.call(
            self.service,
            'getRegisteredNameserver',
            
        )
        from SoftLayer.datatypes.Container.Dns.Domain.Registration.Nameserver import Nameserver
        return SL_Nameserver(data)

# This file was automatically generated with tools/generateTypes.py
    def getRegistrantVerificationStatusDetail(
        self,
        
    ) -> 'SoftLayer_Container_Dns_Domain_Registration_Registrant_Verification_StatusDetail':
        data = self.client.call(
            self.service,
            'getRegistrantVerificationStatusDetail',
            
        )
        from SoftLayer.datatypes.Container.Dns.Domain.Registration.Registrant.Verification.StatusDetail import StatusDetail
        return SL_StatusDetail(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Information(data)

# This file was automatically generated with tools/generateTypes.py
    def lockDomain(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'lockDomain',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Lookup(data)

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
    def sendAuthenticationCode(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'sendAuthenticationCode',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def sendRegistrantVerificationEmail(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'sendRegistrantVerificationEmail',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def sendTransferApprovalEmail(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'sendTransferApprovalEmail',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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

# This file was automatically generated with tools/generateTypes.py
    def unlockDomain(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'unlockDomain',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Account(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Status(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Status(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Provider(data)


