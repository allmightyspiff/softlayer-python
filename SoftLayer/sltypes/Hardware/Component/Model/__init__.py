from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Hardware_Component_Model(Entity):
    """The SoftLayer_Hardware_Component_Model data type contains general information relating to a single SoftLayer
component model.  A component model represents a vendor specific representation of a hardware component.
Every piece of hardware on a server will have a specific hardware component model."""
    architectureTypeId: str
    capacity: float
    description: str
    hardwareGenericComponentModelId: int
    id_: int
    longDescription: str
    manufacturer: str
    name: str
    version: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Hardware_Component_Model'

    def getObject(self, identifier: int) -> 'Hardware_Component_Model':
        """Retrieve a SoftLayer_Hardware_Component_Model record."""
        data = self.client.call('SoftLayer_Hardware_Component_Model', 'getObject', id=identifier)
        from SoftLayer.sltypes.Hardware_Component_Model import Hardware_Component_Model
        return data

    def getArchitectureType(self, identifier: int) -> 'Hardware_Component_Model_Architecture_Type':
        """"""
        data = self.client.call('SoftLayer_Hardware_Component_Model', 'getArchitectureType', id=identifier)
        from SoftLayer.sltypes.Hardware_Component_Model_Architecture_Type import Hardware_Component_Model_Architecture_Type
        return data

    def getAttributes(self, identifier: int) -> list['Hardware_Component_Model_Attribute']:
        """"""
        data = self.client.call('SoftLayer_Hardware_Component_Model', 'getAttributes', id=identifier)
        from SoftLayer.sltypes.Hardware_Component_Model_Attribute import Hardware_Component_Model_Attribute
        return data

    def getCompatibleArrayTypes(self, identifier: int) -> list['Configuration_Storage_Group_Array_Type']:
        """"""
        data = self.client.call('SoftLayer_Hardware_Component_Model', 'getCompatibleArrayTypes', id=identifier)
        from SoftLayer.sltypes.Configuration_Storage_Group_Array_Type import Configuration_Storage_Group_Array_Type
        return data

    def getCompatibleChildComponentModels(self, identifier: int) -> list['Hardware_Component_Model']:
        """"""
        data = self.client.call('SoftLayer_Hardware_Component_Model', 'getCompatibleChildComponentModels', id=identifier)
        from SoftLayer.sltypes.Hardware_Component_Model import Hardware_Component_Model
        return data

    def getCompatibleParentComponentModels(self, identifier: int) -> list['Hardware_Component_Model']:
        """"""
        data = self.client.call('SoftLayer_Hardware_Component_Model', 'getCompatibleParentComponentModels', id=identifier)
        from SoftLayer.sltypes.Hardware_Component_Model import Hardware_Component_Model
        return data

    def getFirmwareQuantity(self, identifier: int) -> int:
        """"""
        data = self.client.call('SoftLayer_Hardware_Component_Model', 'getFirmwareQuantity', id=identifier)
        return data

    def getFirmwares(self, identifier: int) -> list['Hardware_Component_Firmware']:
        """"""
        data = self.client.call('SoftLayer_Hardware_Component_Model', 'getFirmwares', id=identifier)
        from SoftLayer.sltypes.Hardware_Component_Firmware import Hardware_Component_Firmware
        return data

    def getHardwareComponents(self, identifier: int) -> list['Hardware_Component']:
        """"""
        data = self.client.call('SoftLayer_Hardware_Component_Model', 'getHardwareComponents', id=identifier)
        from SoftLayer.sltypes.Hardware_Component import Hardware_Component
        return data

    def getHardwareGenericComponentModel(self, identifier: int) -> 'Hardware_Component_Model_Generic':
        """"""
        data = self.client.call('SoftLayer_Hardware_Component_Model', 'getHardwareGenericComponentModel', id=identifier)
        from SoftLayer.sltypes.Hardware_Component_Model_Generic import Hardware_Component_Model_Generic
        return data

    def getInfinibandCompatibleAttribute(self, identifier: int) -> 'Hardware_Component_Model_Attribute':
        """"""
        data = self.client.call('SoftLayer_Hardware_Component_Model', 'getInfinibandCompatibleAttribute', id=identifier)
        from SoftLayer.sltypes.Hardware_Component_Model_Attribute import Hardware_Component_Model_Attribute
        return data

    def getIsFlexSkuCompatible(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Hardware_Component_Model', 'getIsFlexSkuCompatible', id=identifier)
        return data

    def getIsInfinibandCompatible(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Hardware_Component_Model', 'getIsInfinibandCompatible', id=identifier)
        return data

    def getQualifiedFirmwares(self, identifier: int) -> list['Hardware_Component_Firmware']:
        """"""
        data = self.client.call('SoftLayer_Hardware_Component_Model', 'getQualifiedFirmwares', id=identifier)
        from SoftLayer.sltypes.Hardware_Component_Firmware import Hardware_Component_Firmware
        return data

    def getRebootTime(self, identifier: int) -> 'Hardware_Component_Motherboard_Reboot_Time':
        """"""
        data = self.client.call('SoftLayer_Hardware_Component_Model', 'getRebootTime', id=identifier)
        from SoftLayer.sltypes.Hardware_Component_Motherboard_Reboot_Time import Hardware_Component_Motherboard_Reboot_Time
        return data

    def getType(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Hardware_Component_Model', 'getType', id=identifier)
        return data

    def getValidAttributeTypes(self, identifier: int) -> list['Hardware_Component_Model_Attribute_Type']:
        """"""
        data = self.client.call('SoftLayer_Hardware_Component_Model', 'getValidAttributeTypes', id=identifier)
        from SoftLayer.sltypes.Hardware_Component_Model_Attribute_Type import Hardware_Component_Model_Attribute_Type
        return data
