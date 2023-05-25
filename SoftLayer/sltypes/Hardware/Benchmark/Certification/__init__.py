from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Hardware_Benchmark_Certification(Entity):
    """The SoftLayer_Hardware_Benchmark_Certification data type contains general information relating to a single
SoftLayer hardware benchmark certification document."""
    accountId: int
    createDate: datetime
    hardwareId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Hardware_Benchmark_Certification'

    def getObject(self, identifier: int) -> 'Hardware_Benchmark_Certification':
        """Retrieve a SoftLayer_Hardware_Benchmark_Certification record."""
        data = self.client.call('SoftLayer_Hardware_Benchmark_Certification', 'getObject', id=identifier)
        return data

    def getResultFile(self, identifier: int) -> str:
        """Retrieve the file for a benchmark certification result, if is exists."""
        data = self.client.call('SoftLayer_Hardware_Benchmark_Certification', 'getResultFile', id=identifier)
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Hardware_Benchmark_Certification', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getHardware(self, identifier: int) -> 'Hardware':
        """"""
        data = self.client.call('SoftLayer_Hardware_Benchmark_Certification', 'getHardware', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data
