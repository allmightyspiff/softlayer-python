from SoftLayer.sltypes.Network.Storage.Backup import Network_Storage_Backup
from SoftLayer.sltypes.Network_Storage_Backup import Network_Storage_Backup
from SoftLayer import BaseClient

class Network_Storage_Backup_Evault(Network_Storage_Backup):
    """The SoftLayer_Network_Storage_Backup_Evault contains general information regarding an EVault Storage service
such as account id, username, maximum capacity, password, Storage's product type and the server id."""

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Storage_Backup_Evault'

    def deleteTasks(self, identifier: int, tasks: int) -> bool:
        """Delete task(s)"""
        data = self.client.call('SoftLayer_Network_Storage_Backup_Evault', 'deleteTasks', tasks, id=identifier)
        return data

    def getHardwareWithEvaultFirst(self, option: str, exactMatch: bool, criteria: str, mode: str) -> list['Hardware']:
        """Retrieve all the hardware for the account listing the hardware with EVault Storage service first. The output
will be paginated having 25 items on each page."""
        data = self.client.call('SoftLayer_Network_Storage_Backup_Evault', 'getHardwareWithEvaultFirst', option, exactMatch, criteria, mode)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getObject(self, identifier: int) -> 'Network_Storage_Backup_Evault':
        """Retrieve a SoftLayer_Network_Storage_Backup_Evault record."""
        data = self.client.call('SoftLayer_Network_Storage_Backup_Evault', 'getObject', id=identifier)
        from SoftLayer.sltypes.Network_Storage_Backup_Evault import Network_Storage_Backup_Evault
        return data

    def getWebCCAuthenticationDetails(self) -> 'Container_Network_Storage_Backup_Evault_WebCc_Authentication_Details':
        """Retrieve WebCC authentication details value. This value is required for the login process associated to the
session information for WebCC."""
        data = self.client.call('SoftLayer_Network_Storage_Backup_Evault', 'getWebCCAuthenticationDetails')
        from SoftLayer.sltypes.Container_Network_Storage_Backup_Evault_WebCc_Authentication_Details import Container_Network_Storage_Backup_Evault_WebCc_Authentication_Details
        return data

    def initiateBareMetalRestore(self, identifier: int) -> bool:
        """Initiate a bare metal restore for the server tied to the EVault account"""
        data = self.client.call('SoftLayer_Network_Storage_Backup_Evault', 'initiateBareMetalRestore', id=identifier)
        return data

    def initiateBareMetalRestoreForServer(self, identifier: int, hardwareId: int) -> bool:
        """Initiate a bare metal restore for the specified server"""
        data = self.client.call('SoftLayer_Network_Storage_Backup_Evault', 'initiateBareMetalRestoreForServer', hardwareId, id=identifier)
        return data
