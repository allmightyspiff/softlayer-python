# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Media_Transcode_Account(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Media_Transcode_Account'
        self.client = client

    def createTranscodeAccount(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'createTranscodeAccount',
            
        )
        
        return data


    def createTranscodeJob(
        self,
        newJob: 'SoftLayer_Network_Media_Transcode_Job',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'createTranscodeJob',
            newJob,
            id=identifier
        )
        
        return data


    def getDirectoryInformation(
        self,
        directoryName: str,
        extensionFilter: str,
        identifier: int
    ) -> 'list[SoftLayer_Container_Network_Directory_Listing]':

        data = self.client.call(
            self.service,
            'getDirectoryInformation',
            directoryName,
            extensionFilter,
            id=identifier
        )
        from SoftLayer.datatypes.Container.Network.Directory.Listing import Listing
        return Listing(data)


    def getFileDetail(
        self,
        source: str,
        identifier: int
    ) -> 'SoftLayer_Container_Network_Media_Information':

        data = self.client.call(
            self.service,
            'getFileDetail',
            source,
            id=identifier
        )
        from SoftLayer.datatypes.Container.Network.Media.Information import Information
        return Information(data)


    def getFtpAttributes(
        self,
        identifier: int
    ) -> 'SoftLayer_Container_Network_Authentication_Data':

        data = self.client.call(
            self.service,
            'getFtpAttributes',
            id=identifier
        )
        from SoftLayer.datatypes.Container.Network.Authentication.Data import Data
        return Data(data)


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Media_Transcode_Account':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Media.Transcode.Account import Account
        return Account(data)


    def getPresetDetail(
        self,
        guid: str,
        identifier: int
    ) -> 'list[SoftLayer_Container_Network_Media_Transcode_Preset_Element]':

        data = self.client.call(
            self.service,
            'getPresetDetail',
            guid,
            id=identifier
        )
        from SoftLayer.datatypes.Container.Network.Media.Transcode.Preset.Element import Element
        return Element(data)


    def getPresets(
        self,
        identifier: int
    ) -> 'list[SoftLayer_Container_Network_Media_Transcode_Preset]':

        data = self.client.call(
            self.service,
            'getPresets',
            id=identifier
        )
        from SoftLayer.datatypes.Container.Network.Media.Transcode.Preset import Preset
        return Preset(data)


    def getAccount(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account':

        data = self.client.call(
            self.service,
            'getAccount',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account import Account
        return Account(data)


    def getTranscodeJobs(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Media_Transcode_Job]':

        data = self.client.call(
            self.service,
            'getTranscodeJobs',
            id=identifier,
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Media.Transcode.Job import Job
        return Job(data)


