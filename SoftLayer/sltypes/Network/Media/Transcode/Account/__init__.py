from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Media_Transcode_Account(Entity):
    """The SoftLayer_Network_Media_Transcode_Account contains information regarding a transcode account."""
    accountId: int
    createDate: datetime
    id_: int
    modifyDate: datetime

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Media_Transcode_Account'

    def createTranscodeAccount(self) -> bool:
        """Creates a new transcode account"""
        data = self.client.call('SoftLayer_Network_Media_Transcode_Account', 'createTranscodeAccount')
        return data

    def createTranscodeJob(self, identifier: int, newJob: 'Network_Media_Transcode_Job') -> bool:
        """Creates a transcode job"""
        data = self.client.call('SoftLayer_Network_Media_Transcode_Account', 'createTranscodeJob', newJob, id=identifier)
        return data

    def getDirectoryInformation(self, identifier: int, directoryName: str, extensionFilter: str) -> list['Container_Network_Directory_Listing']:
        """Returns a directory listing"""
        data = self.client.call('SoftLayer_Network_Media_Transcode_Account', 'getDirectoryInformation', directoryName, extensionFilter, id=identifier)
        from SoftLayer.sltypes.Container_Network_Directory_Listing import Container_Network_Directory_Listing
        return data

    def getFileDetail(self, identifier: int, source: str) -> 'Container_Network_Media_Information':
        """Returns detailed information on a video or audio file"""
        data = self.client.call('SoftLayer_Network_Media_Transcode_Account', 'getFileDetail', source, id=identifier)
        from SoftLayer.sltypes.Container_Network_Media_Information import Container_Network_Media_Information
        return data

    def getFtpAttributes(self, identifier: int) -> 'Container_Network_Authentication_Data':
        """Returns Transcode FTP login credentials"""
        data = self.client.call('SoftLayer_Network_Media_Transcode_Account', 'getFtpAttributes', id=identifier)
        from SoftLayer.sltypes.Container_Network_Authentication_Data import Container_Network_Authentication_Data
        return data

    def getObject(self, identifier: int) -> 'Network_Media_Transcode_Account':
        """Retrieve a SoftLayer_Network_Media_Transcode_Account record."""
        data = self.client.call('SoftLayer_Network_Media_Transcode_Account', 'getObject', id=identifier)
        return data

    def getPresetDetail(self, identifier: int, guid: str) -> list['Container_Network_Media_Transcode_Preset_Element']:
        """Returns details on a transcode output preset"""
        data = self.client.call('SoftLayer_Network_Media_Transcode_Account', 'getPresetDetail', guid, id=identifier)
        from SoftLayer.sltypes.Container_Network_Media_Transcode_Preset_Element import Container_Network_Media_Transcode_Preset_Element
        return data

    def getPresets(self, identifier: int) -> list['Container_Network_Media_Transcode_Preset']:
        """Returns an array of transcoding preset objects"""
        data = self.client.call('SoftLayer_Network_Media_Transcode_Account', 'getPresets', id=identifier)
        from SoftLayer.sltypes.Container_Network_Media_Transcode_Preset import Container_Network_Media_Transcode_Preset
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Network_Media_Transcode_Account', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getTranscodeJobs(self, identifier: int) -> list['Network_Media_Transcode_Job']:
        """"""
        data = self.client.call('SoftLayer_Network_Media_Transcode_Account', 'getTranscodeJobs', id=identifier)
        from SoftLayer.sltypes.Network_Media_Transcode_Job import Network_Media_Transcode_Job
        return data
