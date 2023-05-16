# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Event_Log(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Event_Log'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def getAllEventNames(
        self,
        objectName: str
    ) -> 'list[string]':
        data = self.client.call(
            self.service,
            'getAllEventNames',
            objectName
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getAllEventObjectNames(
        self,
        
    ) -> 'list[string]':
        data = self.client.call(
            self.service,
            'getAllEventObjectNames',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getAllObjects(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Event_Log]':
        data = self.client.call(
            self.service,
            'getAllObjects',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Event.Log import Log
        return SL_Log(data)

# This file was automatically generated with tools/generateTypes.py
    def getAllUserTypes(
        self,
        
    ) -> 'list[string]':
        data = self.client.call(
            self.service,
            'getAllUserTypes',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getUser(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Customer':
        data = self.client.call(
            self.service,
            'getUser',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Customer import Customer
        return SL_Customer(data)


