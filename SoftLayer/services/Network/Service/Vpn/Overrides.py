# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Service_Vpn_Overrides(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Service_Vpn_Overrides'
        self.client = client

    def createObjects(
        self,
        templateObjects: SoftLayer_Network_Service_Vpn_Overrides
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'createObjects',
            templateObjects
        )
        
        return data


    def deleteObject(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deleteObject',
            
        )
        
        return data


    def deleteObjects(
        self,
        templateObjects: SoftLayer_Network_Service_Vpn_Overrides
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deleteObjects',
            templateObjects
        )
        
        return data


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Service_Vpn_Overrides':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Service.Vpn.Overrides import Overrides
        return Overrides(data)


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


    def getUser(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Customer':

        data = self.client.call(
            self.service,
            'getUser',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Customer import Customer
        return Customer(data)


