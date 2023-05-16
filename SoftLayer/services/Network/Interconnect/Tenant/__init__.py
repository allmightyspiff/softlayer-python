# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Interconnect_Tenant(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Interconnect_Tenant'
        self.client = client

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


    def createConnection(
        self,
        templateObject: 'SoftLayer_Network_Interconnect_Tenant'
    ) -> 'string':

        data = self.client.call(
            self.service,
            'createConnection',
            templateObject
        )
        
        return data


    def deleteConnection(
        self,
        receivedObject: 'SoftLayer_Network_Interconnect_Tenant'
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deleteConnection',
            receivedObject
        )
        
        return data


    def editConnection(
        self,
        receivedObject: 'SoftLayer_Network_Interconnect_Tenant'
    ) -> 'string':

        data = self.client.call(
            self.service,
            'editConnection',
            receivedObject
        )
        
        return data


    def getAllConnections(
        self,
        
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getAllConnections',
            
        )
        
        return data


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
        return Tenant(data)


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


    def getBgpIpRange(
        self,
        
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getBgpIpRange',
            
        )
        
        return data


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


    def getNetworkZones(
        self,
        
    ) -> 'list[string]':

        data = self.client.call(
            self.service,
            'getNetworkZones',
            
        )
        
        return data


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Interconnect_Tenant':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Interconnect.Tenant import Tenant
        return Tenant(data)


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


    def isAdnAccount(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'isAdnAccount',
            
        )
        
        return data


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


    def getBillingItem(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Item_Network_Interconnect':

        data = self.client.call(
            self.service,
            'getBillingItem',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Item.Network.Interconnect import Interconnect
        return Interconnect(data)


    def getDatacenterName(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getDatacenterName',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getPortLabel(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getPortLabel',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getServiceType(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_DirectLink_ServiceType':

        data = self.client.call(
            self.service,
            'getServiceType',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.DirectLink.ServiceType import ServiceType
        return ServiceType(data)


    def getVendorName(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getVendorName',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getZoneName(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getZoneName',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


