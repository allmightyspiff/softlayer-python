# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Hardware_Component_Partition_OperatingSystem(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Hardware_Component_Partition_OperatingSystem'
        self.client = client

    def getAllObjects(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Hardware_Component_Partition_OperatingSystem]':

        data = self.client.call(
            self.service,
            'getAllObjects',
            mask=objectMask
        )
        from SoftLayer.datatypes.Hardware.Component.Partition.OperatingSystem import OperatingSystem
        return OperatingSystem(data)


    def getByDescription(
        self,
        description: str,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Hardware_Component_Partition_OperatingSystem':

        data = self.client.call(
            self.service,
            'getByDescription',
            description,
            mask=objectMask
        )
        from SoftLayer.datatypes.Hardware.Component.Partition.OperatingSystem import OperatingSystem
        return OperatingSystem(data)


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Hardware_Component_Partition_OperatingSystem':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Hardware.Component.Partition.OperatingSystem import OperatingSystem
        return OperatingSystem(data)


    def getPartitionTemplates(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware_Component_Partition_Template]':

        data = self.client.call(
            self.service,
            'getPartitionTemplates',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware.Component.Partition.Template import Template
        return Template(data)


