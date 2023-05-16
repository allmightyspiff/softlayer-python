# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_LoadBalancer_VirtualIpAddress(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_LoadBalancer_VirtualIpAddress'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def disable(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'disable',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def editObject(
        self,
        templateObject: SoftLayer_Network_LoadBalancer_VirtualIpAddress
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'editObject',
            templateObject
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def enable(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'enable',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_LoadBalancer_VirtualIpAddress':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.LoadBalancer.VirtualIpAddress import VirtualIpAddress
        return SL_VirtualIpAddress(data)

# This file was automatically generated with tools/generateTypes.py
    def kickAllConnections(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'kickAllConnections',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def upgradeConnectionLimit(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'upgradeConnectionLimit',
            
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
        return SL_Item(data)

# This file was automatically generated with tools/generateTypes.py
    def getCustomerManagedFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'int':
        data = self.client.call(
            self.service,
            'getCustomerManagedFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getManagedResourceFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'getManagedResourceFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getServices(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_LoadBalancer_Service]':
        data = self.client.call(
            self.service,
            'getServices',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.LoadBalancer.Service import Service
        return SL_Service(data)


