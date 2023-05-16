# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Storage_Hub_Swift_Share(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Storage_Hub_Swift_Share'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def getContainerList(
        self,
        
    ) -> 'list[SoftLayer_Container_Network_Storage_Hub_ObjectStorage_Folder]':
        data = self.client.call(
            self.service,
            'getContainerList',
            
        )
        from SoftLayer.datatypes.Container.Network.Storage.Hub.ObjectStorage.Folder import Folder
        return SL_Folder(data)

# This file was automatically generated with tools/generateTypes.py
    def getFile(
        self,
        fileName: str,
        container: str
    ) -> 'SoftLayer_Container_Network_Storage_Hub_ObjectStorage_File':
        data = self.client.call(
            self.service,
            'getFile',
            fileName,
            container
        )
        from SoftLayer.datatypes.Container.Network.Storage.Hub.ObjectStorage.File import File
        return SL_File(data)

# This file was automatically generated with tools/generateTypes.py
    def getFileList(
        self,
        container: str,
        path: str,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Container_Utility_File_Entity]':
        data = self.client.call(
            self.service,
            'getFileList',
            container,
            path,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Container.Utility.File.Entity import Entity
        return SL_Entity(data)


