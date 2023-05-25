from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Layout_Profile_Containers(Entity):
    createDate: datetime
    id_: int
    layoutContainerId: int
    layoutProfileId: int
    modifyDate: datetime

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Layout_Profile_Containers'

    def createObject(self, templateObject: 'Layout_Profile_Containers') -> 'Layout_Profile_Containers':
        """Associate a layout container with a profile"""
        data = self.client.call('SoftLayer_Layout_Profile_Containers', 'createObject', templateObject)
        from SoftLayer.sltypes.Layout_Profile_Containers import Layout_Profile_Containers
        return data

    def editObject(self, identifier: int, templateObject: 'Layout_Profile_Containers') -> bool:
        """Edit the object by passing in a modified instance of the object"""
        data = self.client.call('SoftLayer_Layout_Profile_Containers', 'editObject', templateObject, id=identifier)
        return data

    def getObject(self, identifier: int) -> 'Layout_Profile_Containers':
        """Retrieve a SoftLayer_Layout_Profile_Containers record."""
        data = self.client.call('SoftLayer_Layout_Profile_Containers', 'getObject', id=identifier)
        from SoftLayer.sltypes.Layout_Profile_Containers import Layout_Profile_Containers
        return data

    def getLayoutContainerType(self, identifier: int) -> 'Layout_Container':
        """"""
        data = self.client.call('SoftLayer_Layout_Profile_Containers', 'getLayoutContainerType', id=identifier)
        from SoftLayer.sltypes.Layout_Container import Layout_Container
        return data

    def getLayoutProfile(self, identifier: int) -> 'Layout_Profile':
        """"""
        data = self.client.call('SoftLayer_Layout_Profile_Containers', 'getLayoutProfile', id=identifier)
        from SoftLayer.sltypes.Layout_Profile import Layout_Profile
        return data
