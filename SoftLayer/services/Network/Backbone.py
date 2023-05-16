# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Backbone(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Backbone'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def getAllBackbones(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Backbone]':
        data = self.client.call(
            self.service,
            'getAllBackbones',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Backbone import Backbone
        return SL_Backbone(data)

# This file was automatically generated with tools/generateTypes.py
    def getBackbonesForLocationName(
        self,
        locationName: str,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Network_Backbone]':
        data = self.client.call(
            self.service,
            'getBackbonesForLocationName',
            locationName,
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Backbone import Backbone
        return SL_Backbone(data)

# This file was automatically generated with tools/generateTypes.py
    def getGraphImage(
        self,
        
    ) -> 'base64Binary':
        data = self.client.call(
            self.service,
            'getGraphImage',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Backbone':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Backbone import Backbone
        return SL_Backbone(data)

# This file was automatically generated with tools/generateTypes.py
    def getHealth(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':
        data = self.client.call(
            self.service,
            'getHealth',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getLocation(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Location':
        data = self.client.call(
            self.service,
            'getLocation',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Location import Location
        return SL_Location(data)

# This file was automatically generated with tools/generateTypes.py
    def getNetworkComponent(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Component':
        data = self.client.call(
            self.service,
            'getNetworkComponent',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Component import Component
        return SL_Component(data)


