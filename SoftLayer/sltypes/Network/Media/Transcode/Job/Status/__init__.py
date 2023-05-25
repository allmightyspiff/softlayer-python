from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Media_Transcode_Job_Status(Entity):
    """The SoftLayer_Network_Media_Transcode_Job_Status contains information on a transcode job status."""
    description: str
    id_: int
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Media_Transcode_Job_Status'

    def getAllStatuses(self) -> list['Network_Media_Transcode_Job_Status']:
        """Returns all transcode job statuses"""
        data = self.client.call('SoftLayer_Network_Media_Transcode_Job_Status', 'getAllStatuses')
        return data

    def getObject(self, identifier: int) -> 'Network_Media_Transcode_Job_Status':
        """Retrieve a SoftLayer_Network_Media_Transcode_Job_Status record."""
        data = self.client.call('SoftLayer_Network_Media_Transcode_Job_Status', 'getObject', id=identifier)
        return data
