# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Software_VirtualLicense(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Software_VirtualLicense'
        self.client = client

    def getLicenseFile(
        self,
        
    ) -> 'base64Binary':

        data = self.client.call(
            self.service,
            'getLicenseFile',
            
        )
        
        return data


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Software_VirtualLicense':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Software.VirtualLicense import VirtualLicense
        return VirtualLicense(data)


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


    def getHostHardware(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Hardware_Server':

        data = self.client.call(
            self.service,
            'getHostHardware',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Hardware.Server import Server
        return Server(data)


    def getIpAddressRecord(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Subnet_IpAddress':

        data = self.client.call(
            self.service,
            'getIpAddressRecord',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Subnet.IpAddress import IpAddress
        return IpAddress(data)


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


    def getSubnet(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Subnet':

        data = self.client.call(
            self.service,
            'getSubnet',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Subnet import Subnet
        return Subnet(data)


