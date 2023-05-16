# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Security_Certificate_Request_Status(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Security_Certificate_Request_Status'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Security_Certificate_Request_Status':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Security.Certificate.Request.Status import Status
        return SL_Status(data)

# This file was automatically generated with tools/generateTypes.py
    def getSslRequestStatuses(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Security_Certificate_Request_Status]':
        data = self.client.call(
            self.service,
            'getSslRequestStatuses',
            mask=objectMask
        )
        from SoftLayer.datatypes.Security.Certificate.Request.Status import Status
        return SL_Status(data)


