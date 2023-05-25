from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Hardware_Component_Locator(Entity):
    pass

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Hardware_Component_Locator'

    def getGenericComponentModelAvailability(self, genericComponentModelIds: int) -> list['Hardware_Component_Locator_Result']:
        """An API to retrieve Generic Components Model availability at data centers"""
        data = self.client.call('SoftLayer_Hardware_Component_Locator', 'getGenericComponentModelAvailability', genericComponentModelIds)
        from SoftLayer.sltypes.Hardware_Component_Locator_Result import Hardware_Component_Locator_Result
        return data

    def getPackageItemsAvailability(self, packageId: int) -> list['Hardware_Component_Locator_Result']:
        """Retrieve availability of specified product package's GPUs and drives"""
        data = self.client.call('SoftLayer_Hardware_Component_Locator', 'getPackageItemsAvailability', packageId)
        from SoftLayer.sltypes.Hardware_Component_Locator_Result import Hardware_Component_Locator_Result
        return data

    def getServerPackageAvailability(self) -> list['Hardware_Component_Locator_Result']:
        """An API to retrieve server package availability at data centers"""
        data = self.client.call('SoftLayer_Hardware_Component_Locator', 'getServerPackageAvailability')
        from SoftLayer.sltypes.Hardware_Component_Locator_Result import Hardware_Component_Locator_Result
        return data
