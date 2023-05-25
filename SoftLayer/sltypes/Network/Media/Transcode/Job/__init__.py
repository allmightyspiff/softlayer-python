from SoftLayer.sltypes.Container.Network.Media.Transcode.Job.Watermark import Container_Network_Media_Transcode_Job_Watermark
from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Media_Transcode_Job(Entity):
    """The SoftLayer_Network_Media_Transcode_Job contains information regarding a transcode job such as input file,
output format, user id and so on."""
    autoDeleteDuration: int
    byteIn: int
    createDate: datetime
    id_: int
    inputFile: str
    modifyDate: datetime
    name: str
    outputFile: str
    transcodeAccountId: int
    transcodeJobGuid: str
    transcodePresetGuid: str
    transcodePresetName: str
    transcodeStatusId: int
    userId: int
    watermark: Container_Network_Media_Transcode_Job_Watermark

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Media_Transcode_Job'

    def createObject(self, templateObject: 'Network_Media_Transcode_Job') -> 'Network_Media_Transcode_Job':
        """Creates a transcode job"""
        data = self.client.call('SoftLayer_Network_Media_Transcode_Job', 'createObject', templateObject)
        from SoftLayer.sltypes.Network_Media_Transcode_Job import Network_Media_Transcode_Job
        return data

    def getObject(self, identifier: int) -> 'Network_Media_Transcode_Job':
        """Retrieve a SoftLayer_Network_Media_Transcode_Job record."""
        data = self.client.call('SoftLayer_Network_Media_Transcode_Job', 'getObject', id=identifier)
        from SoftLayer.sltypes.Network_Media_Transcode_Job import Network_Media_Transcode_Job
        return data

    def getHistory(self, identifier: int) -> list['Network_Media_Transcode_Job_History']:
        """"""
        data = self.client.call('SoftLayer_Network_Media_Transcode_Job', 'getHistory', id=identifier)
        from SoftLayer.sltypes.Network_Media_Transcode_Job_History import Network_Media_Transcode_Job_History
        return data

    def getTranscodeAccount(self, identifier: int) -> 'Network_Media_Transcode_Account':
        """"""
        data = self.client.call('SoftLayer_Network_Media_Transcode_Job', 'getTranscodeAccount', id=identifier)
        from SoftLayer.sltypes.Network_Media_Transcode_Account import Network_Media_Transcode_Account
        return data

    def getTranscodeStatus(self, identifier: int) -> 'Network_Media_Transcode_Job_Status':
        """"""
        data = self.client.call('SoftLayer_Network_Media_Transcode_Job', 'getTranscodeStatus', id=identifier)
        from SoftLayer.sltypes.Network_Media_Transcode_Job_Status import Network_Media_Transcode_Job_Status
        return data

    def getTranscodeStatusName(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Media_Transcode_Job', 'getTranscodeStatusName', id=identifier)
        return data

    def getUser(self, identifier: int) -> 'User_Customer':
        """"""
        data = self.client.call('SoftLayer_Network_Media_Transcode_Job', 'getUser', id=identifier)
        from SoftLayer.sltypes.User_Customer import User_Customer
        return data
