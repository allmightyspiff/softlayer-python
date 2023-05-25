from SoftLayer.sltypes.Location.Group import Location_Group
from SoftLayer.sltypes.Location_Group import Location_Group
from SoftLayer import BaseClient

class Location_Group_Regional(Location_Group):
    pass

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Location_Group_Regional'

    def getAllObjects(self) -> list['Location_Group']:
        """Get all regional groups."""
        data = self.client.call('SoftLayer_Location_Group_Regional', 'getAllObjects')
        from SoftLayer.sltypes.Location_Group import Location_Group
        return data

    def getObject(self, identifier: int) -> 'Location_Group_Regional':
        """Retrieve a SoftLayer_Location_Group_Regional record."""
        data = self.client.call('SoftLayer_Location_Group_Regional', 'getObject', id=identifier)
        from SoftLayer.sltypes.Location_Group_Regional import Location_Group_Regional
        return data

    def getDatacenters(self, identifier: int) -> list['Location']:
        """"""
        data = self.client.call('SoftLayer_Location_Group_Regional', 'getDatacenters', id=identifier)
        from SoftLayer.sltypes.Location import Location
        return data

    def getPreferredDatacenter(self, identifier: int) -> 'Location_Datacenter':
        """"""
        data = self.client.call('SoftLayer_Location_Group_Regional', 'getPreferredDatacenter', id=identifier)
        from SoftLayer.sltypes.Location_Datacenter import Location_Datacenter
        return data
