# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Media_Transcode_Account(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Media_Transcode_Account'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def createTranscodeAccount(
        self,
        
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'createTranscodeAccount',
            
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def createTranscodeJob(
        self,
        newJob: SoftLayer_Network_Media_Transcode_Job
    ) -> 'boolean':
        data = self.client.call(
            self.service,
            'createTranscodeJob',
            newJob
        )
        
        return data

# This file was automatically generated with tools/generateTypes.py
    def getDirectoryInformation(
        self,
        directoryName: str,
        extensionFilter: str
    ) -> 'list[SoftLayer_Container_Network_Directory_Listing]':
        data = self.client.call(
            self.service,
            'getDirectoryInformation',
            directoryName,
            extensionFilter
        )
        from SoftLayer.datatypes.Container.Network.Directory.Listing import Listing
        return SL_Listing(data)

# This file was automatically generated with tools/generateTypes.py
    def getFileDetail(
        self,
        source: str
    ) -> 'SoftLayer_Container_Network_Media_Information':
        data = self.client.call(
            self.service,
            'getFileDetail',
            source
        )
        from SoftLayer.datatypes.Container.Network.Media.Information import Information
        return SL_Information(data)

# This file was automatically generated with tools/generateTypes.py
    def getFtpAttributes(
        self,
        
    ) -> 'SoftLayer_Container_Network_Authentication_Data':
        data = self.client.call(
            self.service,
            'getFtpAttributes',
            
        )
        from SoftLayer.datatypes.Container.Network.Authentication.Data import Data
        return SL_Data(data)

# This file was automatically generated with tools/generateTypes.py
    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Media_Transcode_Account':
        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Media.Transcode.Account import Account
        return SL_Account(data)

# This file was automatically generated with tools/generateTypes.py
    def getPresetDetail(
        self,
        guid: str
    ) -> 'list[SoftLayer_Container_Network_Media_Transcode_Preset_Element]':
        data = self.client.call(
            self.service,
            'getPresetDetail',
            guid
        )
        from SoftLayer.datatypes.Container.Network.Media.Transcode.Preset.Element import Element
        return SL_Element(data)

# This file was automatically generated with tools/generateTypes.py
    def getPresets(
        self,
        
    ) -> 'list[SoftLayer_Container_Network_Media_Transcode_Preset]':
        data = self.client.call(
            self.service,
            'getPresets',
            
        )
        from SoftLayer.datatypes.Container.Network.Media.Transcode.Preset import Preset
        return SL_Preset(data)

# This file was automatically generated with tools/generateTypes.py
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
        return SL_Account(data)

# This file was automatically generated with tools/generateTypes.py
    def getTranscodeJobs(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Media_Transcode_Job]':
        data = self.client.call(
            self.service,
            'getTranscodeJobs',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Media.Transcode.Job import Job
        return SL_Job(data)


