# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Provisioning_Maintenance_Classification_Item_Category(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Provisioning_Maintenance_Classification_Item_Category'
        self.client = client

    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Provisioning_Maintenance_Classification_Item_Category':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Provisioning.Maintenance.Classification.Item.Category import Category
        return Category(data)


    def getMaintenanceClassification(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Provisioning_Maintenance_Classification':

        data = self.client.call(
            self.service,
            'getMaintenanceClassification',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Provisioning.Maintenance.Classification import Classification
        return Classification(data)


