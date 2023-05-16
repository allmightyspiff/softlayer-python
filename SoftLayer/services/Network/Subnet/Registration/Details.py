# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Subnet_Registration_Details(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Subnet_Registration_Details'
        self.client = client

    def createObject(
        self,
        templateObject: SoftLayer_Network_Subnet_Registration_Details,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_Subnet_Registration_Details':

        data = self.client.call(
            self.service,
            'createObject',
            templateObject,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Subnet.Registration.Details import Details
        return Details(data)


    def deleteObject(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deleteObject',
            
        )
        
        return data


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Subnet_Registration_Details':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Subnet.Registration.Details import Details
        return Details(data)


    def getDetail(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_Regional_Registry_Detail':

        data = self.client.call(
            self.service,
            'getDetail',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Regional.Registry.Detail import Detail
        return Detail(data)


    def getRegistration(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Subnet_Registration':

        data = self.client.call(
            self.service,
            'getRegistration',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Subnet.Registration import Registration
        return Registration(data)


