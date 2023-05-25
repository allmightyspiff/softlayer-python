from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Software_Component_Password(Entity):
    """This SoftLayer_Software_Component_Password data type contains a password for a specific software component
instance."""
    createDate: datetime
    id_: int
    modifyDate: datetime
    notes: str
    password: str
    port: int
    softwareId: int
    username: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Software_Component_Password'

    def createObject(self, templateObject: 'Software_Component_Password') -> 'Software_Component_Password':
        """Create a password for a software component."""
        data = self.client.call('SoftLayer_Software_Component_Password', 'createObject', templateObject)
        from SoftLayer.sltypes.Software_Component_Password import Software_Component_Password
        return data

    def createObjects(self, templateObjects: 'Software_Component_Password') -> bool:
        """Create more than one password for a software component."""
        data = self.client.call('SoftLayer_Software_Component_Password', 'createObjects', templateObjects)
        return data

    def deleteObject(self, identifier: int) -> bool:
        """Delete a password from a software component."""
        data = self.client.call('SoftLayer_Software_Component_Password', 'deleteObject', id=identifier)
        return data

    def deleteObjects(self, templateObjects: 'Software_Component_Password') -> bool:
        """Delete more than one passwords from a software component."""
        data = self.client.call('SoftLayer_Software_Component_Password', 'deleteObjects', templateObjects)
        return data

    def editObject(self, identifier: int, templateObject: 'Software_Component_Password') -> bool:
        """Edit the properties of a software component password."""
        data = self.client.call('SoftLayer_Software_Component_Password', 'editObject', templateObject, id=identifier)
        return data

    def editObjects(self, templateObjects: 'Software_Component_Password') -> bool:
        """Edit more than one password from a software component."""
        data = self.client.call('SoftLayer_Software_Component_Password', 'editObjects', templateObjects)
        return data

    def getObject(self, identifier: int) -> 'Software_Component_Password':
        """Retrieve a SoftLayer_Software_Component_Password record."""
        data = self.client.call('SoftLayer_Software_Component_Password', 'getObject', id=identifier)
        from SoftLayer.sltypes.Software_Component_Password import Software_Component_Password
        return data

    def getSoftware(self, identifier: int) -> 'Software_Component':
        """"""
        data = self.client.call('SoftLayer_Software_Component_Password', 'getSoftware', id=identifier)
        from SoftLayer.sltypes.Software_Component import Software_Component
        return data

    def getSshKeys(self, identifier: int) -> list['Security_Ssh_Key']:
        """"""
        data = self.client.call('SoftLayer_Software_Component_Password', 'getSshKeys', id=identifier)
        from SoftLayer.sltypes.Security_Ssh_Key import Security_Ssh_Key
        return data
