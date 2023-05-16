# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Security_Certificate(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Security_Certificate'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def createObject(
        self,
        templateObject: SoftLayer_Security_Certificate,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Security_Certificate':
        data = self.client.call(
            self.service,
            'createObject',
            templateObject,
            mask=objectMask
        )
        from SoftLayer.datatypes.Security.Certificate import Certificate
        return SL_Certificate(data)

# This file was automatically generated with tools/generateTypes.py
    def deleteObject(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'deleteObject',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def editObject(
        self,
        templateObject: SoftLayer_Security_Certificate
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'editObject',
            templateObject
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def findByCommonName(
        self,
        commonName: str,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Security_Certificate]':
        data = self.client.call(
            self.service,
            'findByCommonName',
            commonName,
            mask=objectMask
        )
        from SoftLayer.datatypes.Security.Certificate import Certificate
        return SL_Certificate(data)

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Security_Certificate':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Security.Certificate import Certificate
        return SL_Certificate(data)

# This file was automatically generated with tools/generateTypes.py
    def getPemFormat(
        self,
        
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getPemFormat',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getAssociatedServiceCount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'int':
        data = self.client.call(
            self.service,
            'getAssociatedServiceCount',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getLbaasListeners(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_LBaaS_Listener]':
        data = self.client.call(
            self.service,
            'getLbaasListeners',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.LBaaS.Listener import Listener
        return SL_Listener(data)

# This file was automatically generated with tools/generateTypes.py
    def getLoadBalancerVirtualIpAddresses(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress]':
        data = self.client.call(
            self.service,
            'getLoadBalancerVirtualIpAddresses',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Application.Delivery.Controller.LoadBalancer.VirtualIpAddress import VirtualIpAddress
        return SL_VirtualIpAddress(data)


