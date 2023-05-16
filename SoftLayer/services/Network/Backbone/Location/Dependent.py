# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Backbone_Location_Dependent(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Backbone_Location_Dependent'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def getAllObjects(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'list[SoftLayer_Network_Backbone_Location_Dependent]':
        data = self.client.call(
            self.service,
            'getAllObjects',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Backbone.Location.Dependent import Dependent
        return SL_Dependent(data)

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Backbone_Location_Dependent':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Backbone.Location.Dependent import Dependent
        return SL_Dependent(data)

# This file was automatically generated with tools/generateTypes.py
    def getSourceDependentsByName(
        self,
        locationName: str,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Location':
        data = self.client.call(
            self.service,
            'getSourceDependentsByName',
            locationName,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Location import Location
        return SL_Location(data)

# This file was automatically generated with tools/generateTypes.py
    def getDependentLocation(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Location':
        data = self.client.call(
            self.service,
            'getDependentLocation',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Location import Location
        return SL_Location(data)

# This file was automatically generated with tools/generateTypes.py
    def getSourceLocation(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Location':
        data = self.client.call(
            self.service,
            'getSourceLocation',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Location import Location
        return SL_Location(data)


