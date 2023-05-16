# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Storage_Iscsi_OS_Type(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Storage_Iscsi_OS_Type'
        self.client = client

    def getAllObjects(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'list[SoftLayer_Network_Storage_Iscsi_OS_Type]':

        data = self.client.call(
            self.service,
            'getAllObjects',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Storage.Iscsi.OS.Type import Type
        return Type(data)


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Storage_Iscsi_OS_Type':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Storage.Iscsi.OS.Type import Type
        return Type(data)


