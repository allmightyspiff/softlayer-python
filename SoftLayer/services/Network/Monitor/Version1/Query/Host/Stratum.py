# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Monitor_Version1_Query_Host_Stratum(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Monitor_Version1_Query_Host_Stratum'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def getAllQueryTypes(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Network_Monitor_Version1_Query_Type]':
        data = self.client.call(
            self.service,
            'getAllQueryTypes',
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Monitor.Version1.Query.Type import Type
        return SL_Type(data)

# This file was automatically generated with tools/generateTypes.py
    def getAllResponseTypes(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Network_Monitor_Version1_Query_ResponseType]':
        data = self.client.call(
            self.service,
            'getAllResponseTypes',
            mask=objectMask
        )
        from SoftLayer.datatypes.Network.Monitor.Version1.Query.ResponseType import ResponseType
        return SL_ResponseType(data)

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Monitor_Version1_Query_Host_Stratum':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Monitor.Version1.Query.Host.Stratum import Stratum
        return SL_Stratum(data)

# This file was automatically generated with tools/generateTypes.py
    def getHardware(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Hardware':
        data = self.client.call(
            self.service,
            'getHardware',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return SL_Hardware(data)


