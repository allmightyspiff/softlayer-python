from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Verify_Api_HttpsObj(Entity):
    createDate: datetime
    id_: int
    modifyDate: datetime
    testString: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Verify_Api_HttpsObj'

    def createObject(self, templateObject: 'Verify_Api_HttpsObj') -> 'Verify_Api_HttpsObj':
        data = self.client.call('SoftLayer_Verify_Api_HttpsObj', 'createObject', templateObject)
        from SoftLayer.sltypes.Verify_Api_HttpsObj import Verify_Api_HttpsObj
        return data

    def deleteObject(self, identifier: int) -> bool:
        data = self.client.call('SoftLayer_Verify_Api_HttpsObj', 'deleteObject', id=identifier)
        return data

    def getAllObjects(self) -> list['Verify_Api_HttpsObj']:
        data = self.client.call('SoftLayer_Verify_Api_HttpsObj', 'getAllObjects')
        from SoftLayer.sltypes.Verify_Api_HttpsObj import Verify_Api_HttpsObj
        return data

    def getObject(self, identifier: int) -> 'Verify_Api_HttpsObj':
        """Retrieve a SoftLayer_Verify_Api_HttpsObj record."""
        data = self.client.call('SoftLayer_Verify_Api_HttpsObj', 'getObject', id=identifier)
        from SoftLayer.sltypes.Verify_Api_HttpsObj import Verify_Api_HttpsObj
        return data
