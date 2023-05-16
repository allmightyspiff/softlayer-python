# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Email_Subscription(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Email_Subscription'
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
    def enable(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'enable',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getAllObjects(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Email_Subscription]':
        data = self.client.call(
            self.service,
            'getAllObjects',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Email.Subscription import Subscription
        return SL_Subscription(data)

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Email_Subscription':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Email.Subscription import Subscription
        return SL_Subscription(data)

# This file was automatically generated with tools/generateTypes.py
    def getEnabled(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'getEnabled',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


