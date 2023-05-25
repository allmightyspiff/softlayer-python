from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Layout_Profile_Preference(Entity):
    """The SoftLayer_Layout_Profile_Preference contains definitions for layout preferences"""
    createDate: datetime
    defaultValueFlag: int
    layoutContainerId: int
    layoutItemId: int
    layoutPreferenceId: int
    layoutProfileId: int
    modifyDate: datetime
    value: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Layout_Profile_Preference'

    def getObject(self, identifier: int) -> 'Layout_Profile_Preference':
        """Retrieve a SoftLayer_Layout_Profile_Preference record."""
        data = self.client.call('SoftLayer_Layout_Profile_Preference', 'getObject', id=identifier)
        return data

    def getLayoutContainer(self, identifier: int) -> 'Layout_Container':
        """"""
        data = self.client.call('SoftLayer_Layout_Profile_Preference', 'getLayoutContainer', id=identifier)
        from SoftLayer.sltypes.Layout_Container import Layout_Container
        return data

    def getLayoutItem(self, identifier: int) -> 'Layout_Item':
        """"""
        data = self.client.call('SoftLayer_Layout_Profile_Preference', 'getLayoutItem', id=identifier)
        from SoftLayer.sltypes.Layout_Item import Layout_Item
        return data

    def getLayoutPreference(self, identifier: int) -> 'Layout_Preference':
        """"""
        data = self.client.call('SoftLayer_Layout_Profile_Preference', 'getLayoutPreference', id=identifier)
        from SoftLayer.sltypes.Layout_Preference import Layout_Preference
        return data

    def getLayoutProfile(self, identifier: int) -> 'Layout_Profile':
        """"""
        data = self.client.call('SoftLayer_Layout_Profile_Preference', 'getLayoutProfile', id=identifier)
        from SoftLayer.sltypes.Layout_Profile import Layout_Profile
        return data
