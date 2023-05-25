from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Provisioning_Maintenance_Classification(Entity):
    """The SoftLayer_Provisioning_Maintenance_Classification represent a maintenance type for the specific hardware
maintenance desired."""
    id_: int
    slots: int
    type_: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Provisioning_Maintenance_Classification'

    def getMaintenanceClassification(self, maintenanceClassificationId: int) -> list['Provisioning_Maintenance_Classification']:
        """Retrieve a maintenance classification."""
        data = self.client.call('SoftLayer_Provisioning_Maintenance_Classification', 'getMaintenanceClassification', maintenanceClassificationId)
        return data

    def getMaintenanceClassificationsByItemCategory(self) -> list['Provisioning_Maintenance_Classification_Item_Category']:
        """Retrieve all maintenance classifications."""
        data = self.client.call('SoftLayer_Provisioning_Maintenance_Classification', 'getMaintenanceClassificationsByItemCategory')
        from SoftLayer.sltypes.Provisioning_Maintenance_Classification_Item_Category import Provisioning_Maintenance_Classification_Item_Category
        return data

    def getObject(self, identifier: int) -> 'Provisioning_Maintenance_Classification':
        """Retrieve a SoftLayer_Provisioning_Maintenance_Classification record."""
        data = self.client.call('SoftLayer_Provisioning_Maintenance_Classification', 'getObject', id=identifier)
        return data

    def getItemCategories(self, identifier: int) -> list['Provisioning_Maintenance_Classification_Item_Category']:
        """"""
        data = self.client.call('SoftLayer_Provisioning_Maintenance_Classification', 'getItemCategories', id=identifier)
        from SoftLayer.sltypes.Provisioning_Maintenance_Classification_Item_Category import Provisioning_Maintenance_Classification_Item_Category
        return data
