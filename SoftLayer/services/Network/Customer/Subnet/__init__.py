# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Customer_Subnet(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Customer_Subnet'
        self.client = client

    def createObject(
        self,
        templateObject: 'SoftLayer_Network_Customer_Subnet',
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_Customer_Subnet':

        data = self.client.call(
            self.service,
            'createObject',
            templateObject,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Customer.Subnet import Subnet
        return Subnet(data)


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Customer_Subnet':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Customer.Subnet import Subnet
        return Subnet(data)


    def getIpAddresses(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Customer_Subnet_IpAddress]':

        data = self.client.call(
            self.service,
            'getIpAddresses',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Customer.Subnet.IpAddress import IpAddress
        return IpAddress(data)


