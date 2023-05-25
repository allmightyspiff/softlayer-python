from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Security_Ssh_Key(Entity):
    createDate: datetime
    fingerprint: str
    id_: int
    key: str
    label: str
    modifyDate: datetime
    notes: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Security_Ssh_Key'

    def createObject(self, templateObject: 'Security_Ssh_Key') -> 'Security_Ssh_Key':
        data = self.client.call('SoftLayer_Security_Ssh_Key', 'createObject', templateObject)
        return data

    def deleteObject(self, identifier: int) -> bool:
        data = self.client.call('SoftLayer_Security_Ssh_Key', 'deleteObject', id=identifier)
        return data

    def editObject(self, identifier: int, templateObject: 'Security_Ssh_Key') -> bool:
        data = self.client.call('SoftLayer_Security_Ssh_Key', 'editObject', templateObject, id=identifier)
        return data

    def getObject(self, identifier: int) -> 'Security_Ssh_Key':
        """Retrieve a SoftLayer_Security_Ssh_Key record."""
        data = self.client.call('SoftLayer_Security_Ssh_Key', 'getObject', id=identifier)
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Security_Ssh_Key', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getBlockDeviceTemplateGroups(self, identifier: int) -> list['Virtual_Guest_Block_Device_Template_Group']:
        """"""
        data = self.client.call('SoftLayer_Security_Ssh_Key', 'getBlockDeviceTemplateGroups', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest_Block_Device_Template_Group import Virtual_Guest_Block_Device_Template_Group
        return data

    def getSoftwarePasswords(self, identifier: int) -> list['Software_Component_Password']:
        """"""
        data = self.client.call('SoftLayer_Security_Ssh_Key', 'getSoftwarePasswords', id=identifier)
        from SoftLayer.sltypes.Software_Component_Password import Software_Component_Password
        return data
