# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Application_Delivery_Controller_Configuration_History(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Application_Delivery_Controller_Configuration_History'
        self.client = client

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
    ) -> 'SoftLayer_Network_Application_Delivery_Controller_Configuration_History':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Application.Delivery.Controller.Configuration.History import History
        return History(data)


    def getController(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Application_Delivery_Controller':

        data = self.client.call(
            self.service,
            'getController',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Application.Delivery.Controller import Controller
        return Controller(data)


