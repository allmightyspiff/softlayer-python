# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Hardware_Component_Partition_Template(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Hardware_Component_Partition_Template'
        self.client = client

    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Hardware_Component_Partition_Template':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Hardware.Component.Partition.Template import Template
        return Template(data)


    def getAccount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account':

        data = self.client.call(
            self.service,
            'getAccount',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account import Account
        return Account(data)


    def getData(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware_Component_Partition_Template_Partition]':

        data = self.client.call(
            self.service,
            'getData',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware.Component.Partition.Template.Partition import Partition
        return Partition(data)


    def getExpireDate(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getExpireDate',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getPartitionOperatingSystem(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Hardware_Component_Partition_OperatingSystem':

        data = self.client.call(
            self.service,
            'getPartitionOperatingSystem',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Hardware.Component.Partition.OperatingSystem import OperatingSystem
        return OperatingSystem(data)


    def getPartitionTemplatePartition(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware_Component_Partition_Template_Partition]':

        data = self.client.call(
            self.service,
            'getPartitionTemplatePartition',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware.Component.Partition.Template.Partition import Partition
        return Partition(data)


