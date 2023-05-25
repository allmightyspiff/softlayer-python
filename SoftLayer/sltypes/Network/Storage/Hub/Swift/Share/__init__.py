from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Storage_Hub_Swift_Share(Entity):
    pass

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Storage_Hub_Swift_Share'

    def getContainerList(self) -> list['Container_Network_Storage_Hub_ObjectStorage_Folder']:
        """Get a list of the file containers for a brand."""
        data = self.client.call('SoftLayer_Network_Storage_Hub_Swift_Share', 'getContainerList')
        from SoftLayer.sltypes.Container_Network_Storage_Hub_ObjectStorage_Folder import Container_Network_Storage_Hub_ObjectStorage_Folder
        return data

    def getFile(self, fileName: str, container: str) -> 'Container_Network_Storage_Hub_ObjectStorage_File':
        """Download a file."""
        data = self.client.call('SoftLayer_Network_Storage_Hub_Swift_Share', 'getFile', fileName, container)
        from SoftLayer.sltypes.Container_Network_Storage_Hub_ObjectStorage_File import Container_Network_Storage_Hub_ObjectStorage_File
        return data

    def getFileList(self, container: str, path: str) -> list['Container_Utility_File_Entity']:
        """Get a list of the files in a container and path."""
        data = self.client.call('SoftLayer_Network_Storage_Hub_Swift_Share', 'getFileList', container, path)
        from SoftLayer.sltypes.Container_Utility_File_Entity import Container_Utility_File_Entity
        return data
