from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Configuration_Template(Entity):
    """The SoftLayer_Configuration_Template data type contains general information of an arbitrary resource."""
    accountId: int
    createDate: datetime
    description: str
    id_: int
    itemId: int
    modifyDate: datetime
    name: str
    parentId: int
    userRecordId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Configuration_Template'

    def copyTemplate(self, identifier: int, templateObject: 'Configuration_Template') -> 'Configuration_Template':
        """Copy a configuration template and returns a newly created template copy"""
        data = self.client.call('SoftLayer_Configuration_Template', 'copyTemplate', templateObject, id=identifier)
        from SoftLayer.sltypes.Configuration_Template import Configuration_Template
        return data

    def deleteObject(self, identifier: int) -> bool:
        """Deletes a customer configuration template."""
        data = self.client.call('SoftLayer_Configuration_Template', 'deleteObject', id=identifier)
        return data

    def editObject(self, identifier: int, templateObject: 'Configuration_Template') -> bool:
        """Edit the object by passing in a modified instance of the object"""
        data = self.client.call('SoftLayer_Configuration_Template', 'editObject', templateObject, id=identifier)
        return data

    def getAllObjects(self) -> list['Configuration_Template']:
        """Retrieves all available configuration templates."""
        data = self.client.call('SoftLayer_Configuration_Template', 'getAllObjects')
        from SoftLayer.sltypes.Configuration_Template import Configuration_Template
        return data

    def getObject(self, identifier: int) -> 'Configuration_Template':
        """Retrieve a SoftLayer_Configuration_Template record."""
        data = self.client.call('SoftLayer_Configuration_Template', 'getObject', id=identifier)
        from SoftLayer.sltypes.Configuration_Template import Configuration_Template
        return data

    def updateDefaultValues(self, identifier: int, configurationValues: 'Configuration_Template_Section_Definition_Value') -> bool:
        """Updates default configuration values."""
        data = self.client.call('SoftLayer_Configuration_Template', 'updateDefaultValues', configurationValues, id=identifier)
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Configuration_Template', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getConfigurationSections(self, identifier: int) -> list['Configuration_Template_Section']:
        """"""
        data = self.client.call('SoftLayer_Configuration_Template', 'getConfigurationSections', id=identifier)
        from SoftLayer.sltypes.Configuration_Template_Section import Configuration_Template_Section
        return data

    def getDefaultValues(self, identifier: int) -> list['Configuration_Template_Section_Definition_Value']:
        """"""
        data = self.client.call('SoftLayer_Configuration_Template', 'getDefaultValues', id=identifier)
        from SoftLayer.sltypes.Configuration_Template_Section_Definition_Value import Configuration_Template_Section_Definition_Value
        return data

    def getDefinitions(self, identifier: int) -> list['Configuration_Template_Section_Definition']:
        """"""
        data = self.client.call('SoftLayer_Configuration_Template', 'getDefinitions', id=identifier)
        from SoftLayer.sltypes.Configuration_Template_Section_Definition import Configuration_Template_Section_Definition
        return data

    def getItem(self, identifier: int) -> 'Product_Item':
        """"""
        data = self.client.call('SoftLayer_Configuration_Template', 'getItem', id=identifier)
        from SoftLayer.sltypes.Product_Item import Product_Item
        return data

    def getLinkedSectionReferences(self, identifier: int) -> 'Configuration_Template_Section_Reference':
        """"""
        data = self.client.call('SoftLayer_Configuration_Template', 'getLinkedSectionReferences', id=identifier)
        from SoftLayer.sltypes.Configuration_Template_Section_Reference import Configuration_Template_Section_Reference
        return data

    def getParent(self, identifier: int) -> 'Configuration_Template':
        """"""
        data = self.client.call('SoftLayer_Configuration_Template', 'getParent', id=identifier)
        from SoftLayer.sltypes.Configuration_Template import Configuration_Template
        return data

    def getUser(self, identifier: int) -> 'User_Customer':
        """"""
        data = self.client.call('SoftLayer_Configuration_Template', 'getUser', id=identifier)
        from SoftLayer.sltypes.User_Customer import User_Customer
        return data
