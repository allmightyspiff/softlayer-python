from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Storage_Allowed_Host(Entity):
    accountId: int
    credentialId: int
    id_: int
    name: str
    resourceTableId: int
    resourceTableName: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Storage_Allowed_Host'

    def assignSubnetsToAcl(self, identifier: int, subnetIds: int) -> list[int]:
        data = self.client.call('SoftLayer_Network_Storage_Allowed_Host', 'assignSubnetsToAcl', subnetIds, id=identifier)
        return data

    def editObject(self, identifier: int, templateObject: 'Network_Storage_Allowed_Host') -> bool:
        data = self.client.call('SoftLayer_Network_Storage_Allowed_Host', 'editObject', templateObject, id=identifier)
        return data

    def getAllObjects(self) -> list['Network_Storage_Allowed_Host']:
        data = self.client.call('SoftLayer_Network_Storage_Allowed_Host', 'getAllObjects')
        return data

    def getObject(self, identifier: int) -> 'Network_Storage_Allowed_Host':
        """Retrieve a SoftLayer_Network_Storage_Allowed_Host record."""
        data = self.client.call('SoftLayer_Network_Storage_Allowed_Host', 'getObject', id=identifier)
        return data

    def removeSubnetsFromAcl(self, identifier: int, subnetIds: int) -> list[int]:
        data = self.client.call('SoftLayer_Network_Storage_Allowed_Host', 'removeSubnetsFromAcl', subnetIds, id=identifier)
        return data

    def setCredentialPassword(self, identifier: int, password: str) -> bool:
        """Modify the credential password for this SoftLayer_Network_Storage_Allowed_Host"""
        data = self.client.call('SoftLayer_Network_Storage_Allowed_Host', 'setCredentialPassword', password, id=identifier)
        return data

    def getAssignedGroups(self, identifier: int) -> list['Network_Storage_Group']:
        """"""
        data = self.client.call('SoftLayer_Network_Storage_Allowed_Host', 'getAssignedGroups', id=identifier)
        from SoftLayer.sltypes.Network_Storage_Group import Network_Storage_Group
        return data

    def getAssignedIscsiVolumes(self, identifier: int) -> list['Network_Storage']:
        """"""
        data = self.client.call('SoftLayer_Network_Storage_Allowed_Host', 'getAssignedIscsiVolumes', id=identifier)
        from SoftLayer.sltypes.Network_Storage import Network_Storage
        return data

    def getAssignedNfsVolumes(self, identifier: int) -> list['Network_Storage']:
        """"""
        data = self.client.call('SoftLayer_Network_Storage_Allowed_Host', 'getAssignedNfsVolumes', id=identifier)
        from SoftLayer.sltypes.Network_Storage import Network_Storage
        return data

    def getAssignedReplicationVolumes(self, identifier: int) -> list['Network_Storage']:
        """"""
        data = self.client.call('SoftLayer_Network_Storage_Allowed_Host', 'getAssignedReplicationVolumes', id=identifier)
        from SoftLayer.sltypes.Network_Storage import Network_Storage
        return data

    def getAssignedVolumes(self, identifier: int) -> list['Network_Storage']:
        """"""
        data = self.client.call('SoftLayer_Network_Storage_Allowed_Host', 'getAssignedVolumes', id=identifier)
        from SoftLayer.sltypes.Network_Storage import Network_Storage
        return data

    def getCredential(self, identifier: int) -> 'Network_Storage_Credential':
        """"""
        data = self.client.call('SoftLayer_Network_Storage_Allowed_Host', 'getCredential', id=identifier)
        from SoftLayer.sltypes.Network_Storage_Credential import Network_Storage_Credential
        return data

    def getSourceSubnet(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Storage_Allowed_Host', 'getSourceSubnet', id=identifier)
        return data

    def getSubnetsInAcl(self, identifier: int) -> list['Network_Subnet']:
        """"""
        data = self.client.call('SoftLayer_Network_Storage_Allowed_Host', 'getSubnetsInAcl', id=identifier)
        from SoftLayer.sltypes.Network_Subnet import Network_Subnet
        return data
