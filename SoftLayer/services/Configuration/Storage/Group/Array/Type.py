# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Configuration_Storage_Group_Array_Type(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Configuration_Storage_Group_Array_Type'
        self.client = client

    def getAllObjects(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'list[SoftLayer_Configuration_Storage_Group_Array_Type]':

        data = self.client.call(
            self.service,
            'getAllObjects',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Configuration.Storage.Group.Array.Type import Type
        return Type(data)


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Configuration_Storage_Group_Array_Type':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Configuration.Storage.Group.Array.Type import Type
        return Type(data)


    def getHardwareComponentModels(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware_Component_Model]':

        data = self.client.call(
            self.service,
            'getHardwareComponentModels',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware.Component.Model import Model
        return Model(data)


