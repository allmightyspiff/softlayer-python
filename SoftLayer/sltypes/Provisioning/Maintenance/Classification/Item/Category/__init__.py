from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Provisioning_Maintenance_Classification_Item_Category(Entity):
    itemCategoryId: int
    maintenanceClassificationId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Provisioning_Maintenance_Classification_Item_Category'

    def getObject(self, identifier: int) -> 'Provisioning_Maintenance_Classification_Item_Category':
        """Retrieve a SoftLayer_Provisioning_Maintenance_Classification_Item_Category record."""
        data = self.client.call('SoftLayer_Provisioning_Maintenance_Classification_Item_Category', 'getObject', id=identifier)
        return data

    def getMaintenanceClassification(self, identifier: int) -> 'Provisioning_Maintenance_Classification':
        """"""
        data = self.client.call('SoftLayer_Provisioning_Maintenance_Classification_Item_Category', 'getMaintenanceClassification', id=identifier)
        from SoftLayer.sltypes.Provisioning_Maintenance_Classification import Provisioning_Maintenance_Classification
        return data
