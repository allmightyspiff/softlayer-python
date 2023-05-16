# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Provisioning_Maintenance_Classification(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Provisioning_Maintenance_Classification'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def getMaintenanceClassification(
        self,
        maintenanceClassificationId: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'list[SoftLayer_Provisioning_Maintenance_Classification]':
        data = self.client.call(
            self.service,
            'getMaintenanceClassification',
            maintenanceClassificationId,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Provisioning.Maintenance.Classification import Classification
        return SL_Classification(data)

# This file was automatically generated with tools/generateTypes.py
    def getMaintenanceClassificationsByItemCategory(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'list[SoftLayer_Provisioning_Maintenance_Classification_Item_Category]':
        data = self.client.call(
            self.service,
            'getMaintenanceClassificationsByItemCategory',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Provisioning.Maintenance.Classification.Item.Category import Category
        return SL_Category(data)

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Provisioning_Maintenance_Classification':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Provisioning.Maintenance.Classification import Classification
        return SL_Classification(data)

# This file was automatically generated with tools/generateTypes.py
    def getItemCategories(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Provisioning_Maintenance_Classification_Item_Category]':
        data = self.client.call(
            self.service,
            'getItemCategories',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Provisioning.Maintenance.Classification.Item.Category import Category
        return SL_Category(data)


