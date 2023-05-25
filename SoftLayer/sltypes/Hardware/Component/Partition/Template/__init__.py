from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Hardware_Component_Partition_Template(Entity):
    """The SoftLayer_Hardware_Component_Partition_Template data type contains general information relating to a
single SoftLayer partition template.  Partition templates group 1 or more partition configurations that can
be used to predefine how a hard drive's partitions will be configured."""
    accountId: int
    description: str
    id_: int
    partitionOperatingSystemId: int
    statusCode: str
    templateType: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Hardware_Component_Partition_Template'

    def getObject(self, identifier: int) -> 'Hardware_Component_Partition_Template':
        """Retrieve a SoftLayer_Hardware_Component_Partition_Template record."""
        data = self.client.call('SoftLayer_Hardware_Component_Partition_Template', 'getObject', id=identifier)
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Hardware_Component_Partition_Template', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getData(self, identifier: int) -> list['Hardware_Component_Partition_Template_Partition']:
        """"""
        data = self.client.call('SoftLayer_Hardware_Component_Partition_Template', 'getData', id=identifier)
        from SoftLayer.sltypes.Hardware_Component_Partition_Template_Partition import Hardware_Component_Partition_Template_Partition
        return data

    def getExpireDate(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Hardware_Component_Partition_Template', 'getExpireDate', id=identifier)
        return data

    def getPartitionOperatingSystem(self, identifier: int) -> 'Hardware_Component_Partition_OperatingSystem':
        """"""
        data = self.client.call('SoftLayer_Hardware_Component_Partition_Template', 'getPartitionOperatingSystem', id=identifier)
        from SoftLayer.sltypes.Hardware_Component_Partition_OperatingSystem import Hardware_Component_Partition_OperatingSystem
        return data

    def getPartitionTemplatePartition(self, identifier: int) -> list['Hardware_Component_Partition_Template_Partition']:
        """"""
        data = self.client.call('SoftLayer_Hardware_Component_Partition_Template', 'getPartitionTemplatePartition', id=identifier)
        from SoftLayer.sltypes.Hardware_Component_Partition_Template_Partition import Hardware_Component_Partition_Template_Partition
        return data
