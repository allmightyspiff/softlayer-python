# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_SecurityGroup(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_SecurityGroup'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def addRules(
        self,
        ruleTemplates: SoftLayer_Network_SecurityGroup_Rule
    ) -> 'SoftLayer_Network_SecurityGroup_RequestRules':
        data = self.client.call(
            self.service,
            'addRules',
            ruleTemplates
        )
        from SoftLayer.datatypes.Network.SecurityGroup.RequestRules import RequestRules
        return SL_RequestRules(data)

# This file was automatically generated with tools/generateTypes.py
    def attachNetworkComponents(
        self,
        networkComponentIds: int
    ) -> 'SoftLayer_Network_SecurityGroup_Request':
        data = self.client.call(
            self.service,
            'attachNetworkComponents',
            networkComponentIds
        )
        from SoftLayer.datatypes.Network.SecurityGroup.Request import Request
        return SL_Request(data)

# This file was automatically generated with tools/generateTypes.py
    def createObject(
        self,
        templateObject: SoftLayer_Network_SecurityGroup,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Network_SecurityGroup':
        data = self.client.call(
            self.service,
            'createObject',
            templateObject,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.SecurityGroup import SecurityGroup
        return SL_SecurityGroup(data)

# This file was automatically generated with tools/generateTypes.py
    def createObjects(
        self,
        templateObjects: SoftLayer_Network_SecurityGroup,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Network_SecurityGroup]':
        data = self.client.call(
            self.service,
            'createObjects',
            templateObjects,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.SecurityGroup import SecurityGroup
        return SL_SecurityGroup(data)

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
    def deleteObjects(
        self,
        templateObjects: SoftLayer_Network_SecurityGroup
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'deleteObjects',
            templateObjects
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def detachNetworkComponents(
        self,
        networkComponentIds: int
    ) -> 'SoftLayer_Network_SecurityGroup_Request':
        data = self.client.call(
            self.service,
            'detachNetworkComponents',
            networkComponentIds
        )
        from SoftLayer.datatypes.Network.SecurityGroup.Request import Request
        return SL_Request(data)

# This file was automatically generated with tools/generateTypes.py
    def editObject(
        self,
        templateObject: SoftLayer_Network_SecurityGroup
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'editObject',
            templateObject
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def editObjects(
        self,
        templateObjects: SoftLayer_Network_SecurityGroup
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'editObjects',
            templateObjects
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def editRules(
        self,
        ruleTemplates: SoftLayer_Network_SecurityGroup_Rule
    ) -> 'SoftLayer_Network_SecurityGroup_RequestRules':
        data = self.client.call(
            self.service,
            'editRules',
            ruleTemplates
        )
        from SoftLayer.datatypes.Network.SecurityGroup.RequestRules import RequestRules
        return SL_RequestRules(data)

# This file was automatically generated with tools/generateTypes.py
    def getAllObjects(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_SecurityGroup]':
        data = self.client.call(
            self.service,
            'getAllObjects',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.SecurityGroup import SecurityGroup
        return SL_SecurityGroup(data)

# This file was automatically generated with tools/generateTypes.py
    def getLimits(
        self,
        
    ) -> 'list[SoftLayer_Container_Network_SecurityGroup_Limit]':
        data = self.client.call(
            self.service,
            'getLimits',
            
        )
        from SoftLayer.datatypes.Container.Network.SecurityGroup.Limit import Limit
        return SL_Limit(data)

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_SecurityGroup':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.SecurityGroup import SecurityGroup
        return SL_SecurityGroup(data)

# This file was automatically generated with tools/generateTypes.py
    def getSupportedDataCenters(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Location]':
        data = self.client.call(
            self.service,
            'getSupportedDataCenters',
            mask=objectMask
        )
        from SoftLayer.datatypes.Location import Location
        return SL_Location(data)

# This file was automatically generated with tools/generateTypes.py
    def removeRules(
        self,
        ruleIds: int
    ) -> 'SoftLayer_Network_SecurityGroup_RequestRules':
        data = self.client.call(
            self.service,
            'removeRules',
            ruleIds
        )
        from SoftLayer.datatypes.Network.SecurityGroup.RequestRules import RequestRules
        return SL_RequestRules(data)

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
    def getNetworkComponentBindings(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Network_SecurityGroup_NetworkComponentBinding]':
        data = self.client.call(
            self.service,
            'getNetworkComponentBindings',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Network.SecurityGroup.NetworkComponentBinding import NetworkComponentBinding
        return SL_NetworkComponentBinding(data)

# This file was automatically generated with tools/generateTypes.py
    def getOrderBindings(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_SecurityGroup_OrderBinding]':
        data = self.client.call(
            self.service,
            'getOrderBindings',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.SecurityGroup.OrderBinding import OrderBinding
        return SL_OrderBinding(data)

# This file was automatically generated with tools/generateTypes.py
    def getRules(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_SecurityGroup_Rule]':
        data = self.client.call(
            self.service,
            'getRules',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.SecurityGroup.Rule import Rule
        return SL_Rule(data)


