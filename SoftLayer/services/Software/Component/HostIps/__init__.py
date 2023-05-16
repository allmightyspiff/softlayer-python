# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Software_Component_HostIps(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Software_Component_HostIps'
        self.client = client

    def getCurrentHostIpsPolicies(
        self,
        identifier: int
    ) -> 'list[SoftLayer_Container_Software_Component_HostIps_Policy]':

        data = self.client.call(
            self.service,
            'getCurrentHostIpsPolicies',
            id=identifier
        )
        from SoftLayer.datatypes.Container.Software.Component.HostIps.Policy import Policy
        return Policy(data)


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Software_Component_HostIps':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Software.Component.HostIps import HostIps
        return HostIps(data)


    def updateHipsPolicies(
        self,
        newIpsMode: str,
        newIpsProtection: str,
        newFirewallMode: str,
        newFirewallRuleset: str,
        newApplicationMode: str,
        newApplicationRuleset: str,
        newEnforcementPolicy: str,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'updateHipsPolicies',
            newIpsMode,
            newIpsProtection,
            newFirewallMode,
            newFirewallRuleset,
            newApplicationMode,
            newApplicationRuleset,
            newEnforcementPolicy,
            id=identifier
        )
        
        return data


    def getLicenseFile(
        self,
        identifier: int
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getLicenseFile',
            id=identifier
        )
        
        return data


    def getVendorSetUpConfiguration(
        self,
        identifier: int
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getVendorSetUpConfiguration',
            id=identifier
        )
        
        return data


    def getAverageInstallationDuration(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'unsignedLong':

        data = self.client.call(
            self.service,
            'getAverageInstallationDuration',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getBillingItem(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Item':

        data = self.client.call(
            self.service,
            'getBillingItem',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Item import Item
        return Item(data)


    def getHardware(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Hardware':

        data = self.client.call(
            self.service,
            'getHardware',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


    def getPasswordHistory(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Software_Component_Password_History]':

        data = self.client.call(
            self.service,
            'getPasswordHistory',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Software.Component.Password.History import History
        return History(data)


    def getPasswords(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Software_Component_Password]':

        data = self.client.call(
            self.service,
            'getPasswords',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Software.Component.Password import Password
        return Password(data)


    def getSoftwareDescription(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Software_Description':

        data = self.client.call(
            self.service,
            'getSoftwareDescription',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Software.Description import Description
        return Description(data)


    def getSoftwareLicense(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Software_License':

        data = self.client.call(
            self.service,
            'getSoftwareLicense',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Software.License import License
        return License(data)


    def getVirtualGuest(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Guest':

        data = self.client.call(
            self.service,
            'getVirtualGuest',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Guest import Guest
        return Guest(data)


