# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Hardware_Component_Model(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Hardware_Component_Model'
        self.client = client

    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Hardware_Component_Model':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Hardware.Component.Model import Model
        return Model(data)


    def getArchitectureType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Hardware_Component_Model_Architecture_Type':

        data = self.client.call(
            self.service,
            'getArchitectureType',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Hardware.Component.Model.Architecture.Type import Type
        return Type(data)


    def getAttributes(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware_Component_Model_Attribute]':

        data = self.client.call(
            self.service,
            'getAttributes',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware.Component.Model.Attribute import Attribute
        return Attribute(data)


    def getCompatibleArrayTypes(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Configuration_Storage_Group_Array_Type]':

        data = self.client.call(
            self.service,
            'getCompatibleArrayTypes',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Configuration.Storage.Group.Array.Type import Type
        return Type(data)


    def getCompatibleChildComponentModels(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware_Component_Model]':

        data = self.client.call(
            self.service,
            'getCompatibleChildComponentModels',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware.Component.Model import Model
        return Model(data)


    def getCompatibleParentComponentModels(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware_Component_Model]':

        data = self.client.call(
            self.service,
            'getCompatibleParentComponentModels',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware.Component.Model import Model
        return Model(data)


    def getFirmwareQuantity(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'unsignedInt':

        data = self.client.call(
            self.service,
            'getFirmwareQuantity',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getFirmwares(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware_Component_Firmware]':

        data = self.client.call(
            self.service,
            'getFirmwares',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware.Component.Firmware import Firmware
        return Firmware(data)


    def getHardwareComponents(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware_Component]':

        data = self.client.call(
            self.service,
            'getHardwareComponents',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware.Component import Component
        return Component(data)


    def getHardwareGenericComponentModel(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Hardware_Component_Model_Generic':

        data = self.client.call(
            self.service,
            'getHardwareGenericComponentModel',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Hardware.Component.Model.Generic import Generic
        return Generic(data)


    def getInfinibandCompatibleAttribute(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Hardware_Component_Model_Attribute':

        data = self.client.call(
            self.service,
            'getInfinibandCompatibleAttribute',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Hardware.Component.Model.Attribute import Attribute
        return Attribute(data)


    def getIsFlexSkuCompatible(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getIsFlexSkuCompatible',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getIsInfinibandCompatible(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getIsInfinibandCompatible',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getQualifiedFirmwares(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware_Component_Firmware]':

        data = self.client.call(
            self.service,
            'getQualifiedFirmwares',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware.Component.Firmware import Firmware
        return Firmware(data)


    def getRebootTime(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Hardware_Component_Motherboard_Reboot_Time':

        data = self.client.call(
            self.service,
            'getRebootTime',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Hardware.Component.Motherboard.Reboot.Time import Time
        return Time(data)


    def getType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getType',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getValidAttributeTypes(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware_Component_Model_Attribute_Type]':

        data = self.client.call(
            self.service,
            'getValidAttributeTypes',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware.Component.Model.Attribute.Type import Type
        return Type(data)


