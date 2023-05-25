from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Verify_Api_HttpObj(Entity):
    createDate: datetime
    id_: int
    modifyDate: datetime
    testString: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Verify_Api_HttpObj'

    def createObject(self, templateObject: 'Verify_Api_HttpObj') -> 'Verify_Api_HttpObj':
        data = self.client.call('SoftLayer_Verify_Api_HttpObj', 'createObject', templateObject)
        from SoftLayer.sltypes.Verify_Api_HttpObj import Verify_Api_HttpObj
        return data

    def deleteObject(self, identifier: int) -> bool:
        data = self.client.call('SoftLayer_Verify_Api_HttpObj', 'deleteObject', id=identifier)
        return data

    def getAllObjects(self) -> list['Verify_Api_HttpObj']:
        data = self.client.call('SoftLayer_Verify_Api_HttpObj', 'getAllObjects')
        from SoftLayer.sltypes.Verify_Api_HttpObj import Verify_Api_HttpObj
        return data

    def getObject(self, identifier: int) -> 'Verify_Api_HttpObj':
        """Retrieve a SoftLayer_Verify_Api_HttpObj record."""
        data = self.client.call('SoftLayer_Verify_Api_HttpObj', 'getObject', id=identifier)
        from SoftLayer.sltypes.Verify_Api_HttpObj import Verify_Api_HttpObj
        return data
