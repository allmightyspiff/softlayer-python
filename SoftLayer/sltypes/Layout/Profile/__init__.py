from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Layout_Profile(Entity):
    """The SoftLayer_Layout_Profile contains the definition of the layout profile"""
    activeFlag: int
    createDate: datetime
    id_: int
    modifyDate: datetime
    name: str
    userRecordId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Layout_Profile'

    def createObject(self, templateObject: 'Layout_Profile') -> bool:
        """Create a new layout profile"""
        data = self.client.call('SoftLayer_Layout_Profile', 'createObject', templateObject)
        return data

    def deleteObject(self, identifier: int) -> bool:
        """Delete a layout profile"""
        data = self.client.call('SoftLayer_Layout_Profile', 'deleteObject', id=identifier)
        return data

    def editObject(self, identifier: int, templateObject: 'Layout_Profile') -> bool:
        """Edit the layout profile object"""
        data = self.client.call('SoftLayer_Layout_Profile', 'editObject', templateObject, id=identifier)
        return data

    def getObject(self, identifier: int) -> 'Layout_Profile':
        """Retrieve a SoftLayer_Layout_Profile record."""
        data = self.client.call('SoftLayer_Layout_Profile', 'getObject', id=identifier)
        from SoftLayer.sltypes.Layout_Profile import Layout_Profile
        return data

    def modifyPreference(self, identifier: int, templateObject: 'Layout_Profile_Preference') -> 'Layout_Profile_Preference':
        """Modifies an associated layout preference"""
        data = self.client.call('SoftLayer_Layout_Profile', 'modifyPreference', templateObject, id=identifier)
        from SoftLayer.sltypes.Layout_Profile_Preference import Layout_Profile_Preference
        return data

    def modifyPreferences(self, identifier: int, layoutPreferenceObjects: 'Layout_Profile_Preference') -> list['Layout_Profile_Preference']:
        """Modifies a collection of associated preferences"""
        data = self.client.call('SoftLayer_Layout_Profile', 'modifyPreferences', layoutPreferenceObjects, id=identifier)
        from SoftLayer.sltypes.Layout_Profile_Preference import Layout_Profile_Preference
        return data

    def getLayoutContainers(self, identifier: int) -> list['Layout_Container']:
        """"""
        data = self.client.call('SoftLayer_Layout_Profile', 'getLayoutContainers', id=identifier)
        from SoftLayer.sltypes.Layout_Container import Layout_Container
        return data

    def getLayoutPreferences(self, identifier: int) -> list['Layout_Profile_Preference']:
        """"""
        data = self.client.call('SoftLayer_Layout_Profile', 'getLayoutPreferences', id=identifier)
        from SoftLayer.sltypes.Layout_Profile_Preference import Layout_Profile_Preference
        return data
