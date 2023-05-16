# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Software_Component(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Software_Component'
        self.client = client

    def getLicenseFile(
        self,
        
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getLicenseFile',
            
        )
        
        return data


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Software_Component':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Software.Component import Component
        return Component(data)


    def getVendorSetUpConfiguration(
        self,
        
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getVendorSetUpConfiguration',
            
        )
        
        return data


    def getAverageInstallationDuration(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'unsignedLong':

        data = self.client.call(
            self.service,
            'getAverageInstallationDuration',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getBillingItem(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Item':

        data = self.client.call(
            self.service,
            'getBillingItem',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Item import Item
        return Item(data)


    def getHardware(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Hardware':

        data = self.client.call(
            self.service,
            'getHardware',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


    def getPasswordHistory(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Software_Component_Password_History]':

        data = self.client.call(
            self.service,
            'getPasswordHistory',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Software.Component.Password.History import History
        return History(data)


    def getPasswords(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Software_Component_Password]':

        data = self.client.call(
            self.service,
            'getPasswords',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Software.Component.Password import Password
        return Password(data)


    def getSoftwareDescription(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Software_Description':

        data = self.client.call(
            self.service,
            'getSoftwareDescription',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Software.Description import Description
        return Description(data)


    def getSoftwareLicense(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Software_License':

        data = self.client.call(
            self.service,
            'getSoftwareLicense',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Software.License import License
        return License(data)


    def getVirtualGuest(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Virtual_Guest':

        data = self.client.call(
            self.service,
            'getVirtualGuest',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Virtual.Guest import Guest
        return Guest(data)


