# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Interconnect_Tenant(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Interconnect_Tenant'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def allowDeleteConnection(
        self,
        serviceKey: str
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'allowDeleteConnection',
            serviceKey
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def createConnection(
        self,
        templateObject: SoftLayer_Network_Interconnect_Tenant
    ) -> 'string':
        data = self.client.call(
            self.service,
            'createConnection',
            templateObject
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def deleteConnection(
        self,
        receivedObject: SoftLayer_Network_Interconnect_Tenant
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'deleteConnection',
            receivedObject
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def editConnection(
        self,
        receivedObject: SoftLayer_Network_Interconnect_Tenant
    ) -> 'string':
        data = self.client.call(
            self.service,
            'editConnection',
            receivedObject
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getAllConnections(
        self,
        
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getAllConnections',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getAllObjects(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Interconnect_Tenant]':
        data = self.client.call(
            self.service,
            'getAllObjects',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Interconnect.Tenant import Tenant
        return SL_Tenant(data)

# This file was automatically generated with tools/generateTypes.py
    def getAllPortLabelsWithCurrentUsage(
        self,
        directLinkLocationId: int
    ) -> 'list[string]':
        data = self.client.call(
            self.service,
            'getAllPortLabelsWithCurrentUsage',
            directLinkLocationId
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getBgpIpRange(
        self,
        
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getBgpIpRange',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getConnection(
        self,
        serviceKey: str,
        provider: str
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getConnection',
            serviceKey,
            provider
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getDirectLinkSpeeds(
        self,
        offeringType: str
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getDirectLinkSpeeds',
            offeringType
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getNetworkZones(
        self,
        
    ) -> 'list[string]':
        data = self.client.call(
            self.service,
            'getNetworkZones',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Interconnect_Tenant':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Interconnect.Tenant import Tenant
        return SL_Tenant(data)

# This file was automatically generated with tools/generateTypes.py
    def getPorts(
        self,
        provider: str
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getPorts',
            provider
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def isAdnAccount(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'isAdnAccount',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def rejectApprovalRequests(
        self,
        serviceKey: str
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'rejectApprovalRequests',
            serviceKey
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def updateConnectionStatus(
        self,
        tenantId: int
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'updateConnectionStatus',
            tenantId
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getBillingItem(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Item_Network_Interconnect':
        data = self.client.call(
            self.service,
            'getBillingItem',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Item.Network.Interconnect import Interconnect
        return SL_Interconnect(data)

# This file was automatically generated with tools/generateTypes.py
    def getDatacenterName(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getDatacenterName',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getPortLabel(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getPortLabel',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getServiceType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_DirectLink_ServiceType':
        data = self.client.call(
            self.service,
            'getServiceType',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.DirectLink.ServiceType import ServiceType
        return SL_ServiceType(data)

# This file was automatically generated with tools/generateTypes.py
    def getVendorName(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getVendorName',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getZoneName(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getZoneName',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


