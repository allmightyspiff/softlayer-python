from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Location(Entity):
    """Every piece of hardware and network connection owned by SoftLayer is tracked physically by location and
stored in the SoftLayer_Location data type. SoftLayer locations exist in parent/child relationships, a
convenient way to track equipment from it's city, datacenter, server room, rack, then slot. Network backbones
are tied to datacenters only, not to a room, rack, or slot."""
    id_: int
    longName: str
    name: str
    statusId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Location'

    def getAvailableObjectStorageDatacenters(self) -> list['Location']:
        """Get the datacenters where object storage is available"""
        data = self.client.call('SoftLayer_Location', 'getAvailableObjectStorageDatacenters')
        from SoftLayer.sltypes.Location import Location
        return data

    def getDatacenters(self) -> list['Location']:
        """Retrieve all datacenter locations"""
        data = self.client.call('SoftLayer_Location', 'getDatacenters')
        from SoftLayer.sltypes.Location import Location
        return data

    def getDatacentersWithVirtualImageStoreServiceResourceRecord(self) -> list['Location']:
        data = self.client.call('SoftLayer_Location', 'getDatacentersWithVirtualImageStoreServiceResourceRecord')
        from SoftLayer.sltypes.Location import Location
        return data

    def getObject(self, identifier: int) -> 'Location':
        """Retrieve a SoftLayer_Location record."""
        data = self.client.call('SoftLayer_Location', 'getObject', id=identifier)
        from SoftLayer.sltypes.Location import Location
        return data

    def getViewableDatacenters(self) -> list['Location']:
        """Retrieve all datacenter locations"""
        data = self.client.call('SoftLayer_Location', 'getViewableDatacenters')
        from SoftLayer.sltypes.Location import Location
        return data

    def getViewablePopsAndDataCenters(self) -> list['Location']:
        """Retrieve viewable pops and datacenters in a combined list."""
        data = self.client.call('SoftLayer_Location', 'getViewablePopsAndDataCenters')
        from SoftLayer.sltypes.Location import Location
        return data

    def getViewablepointOfPresence(self) -> list['Location']:
        """Retrieve viewable network locations"""
        data = self.client.call('SoftLayer_Location', 'getViewablepointOfPresence')
        from SoftLayer.sltypes.Location import Location
        return data

    def getpointOfPresence(self) -> list['Location']:
        """Retrieve all points of presence locations"""
        data = self.client.call('SoftLayer_Location', 'getpointOfPresence')
        from SoftLayer.sltypes.Location import Location
        return data

    def getActivePresaleEvents(self, identifier: int) -> list['Sales_Presale_Event']:
        """"""
        data = self.client.call('SoftLayer_Location', 'getActivePresaleEvents', id=identifier)
        from SoftLayer.sltypes.Sales_Presale_Event import Sales_Presale_Event
        return data

    def getBackboneDependents(self, identifier: int) -> list['Network_Backbone_Location_Dependent']:
        """"""
        data = self.client.call('SoftLayer_Location', 'getBackboneDependents', id=identifier)
        from SoftLayer.sltypes.Network_Backbone_Location_Dependent import Network_Backbone_Location_Dependent
        return data

    def getBnppCompliantFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Location', 'getBnppCompliantFlag', id=identifier)
        return data

    def getEuCompliantFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Location', 'getEuCompliantFlag', id=identifier)
        return data

    def getGroups(self, identifier: int) -> list['Location_Group']:
        """"""
        data = self.client.call('SoftLayer_Location', 'getGroups', id=identifier)
        from SoftLayer.sltypes.Location_Group import Location_Group
        return data

    def getHardwareFirewalls(self, identifier: int) -> list['Hardware']:
        """"""
        data = self.client.call('SoftLayer_Location', 'getHardwareFirewalls', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getLocationAddress(self, identifier: int) -> 'Account_Address':
        """"""
        data = self.client.call('SoftLayer_Location', 'getLocationAddress', id=identifier)
        from SoftLayer.sltypes.Account_Address import Account_Address
        return data

    def getLocationAddresses(self, identifier: int) -> list['Account_Address']:
        """"""
        data = self.client.call('SoftLayer_Location', 'getLocationAddresses', id=identifier)
        from SoftLayer.sltypes.Account_Address import Account_Address
        return data

    def getLocationReservationMember(self, identifier: int) -> 'Location_Reservation_Rack_Member':
        """"""
        data = self.client.call('SoftLayer_Location', 'getLocationReservationMember', id=identifier)
        from SoftLayer.sltypes.Location_Reservation_Rack_Member import Location_Reservation_Rack_Member
        return data

    def getLocationStatus(self, identifier: int) -> 'Location_Status':
        """"""
        data = self.client.call('SoftLayer_Location', 'getLocationStatus', id=identifier)
        from SoftLayer.sltypes.Location_Status import Location_Status
        return data

    def getNetworkConfigurationAttribute(self, identifier: int) -> 'Hardware_Attribute':
        """"""
        data = self.client.call('SoftLayer_Location', 'getNetworkConfigurationAttribute', id=identifier)
        from SoftLayer.sltypes.Hardware_Attribute import Hardware_Attribute
        return data

    def getOnlineSslVpnUserCount(self, identifier: int) -> int:
        """"""
        data = self.client.call('SoftLayer_Location', 'getOnlineSslVpnUserCount', id=identifier)
        return data

    def getPathString(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Location', 'getPathString', id=identifier)
        return data

    def getPriceGroups(self, identifier: int) -> list['Location_Group']:
        """"""
        data = self.client.call('SoftLayer_Location', 'getPriceGroups', id=identifier)
        from SoftLayer.sltypes.Location_Group import Location_Group
        return data

    def getRegions(self, identifier: int) -> list['Location_Region']:
        """"""
        data = self.client.call('SoftLayer_Location', 'getRegions', id=identifier)
        from SoftLayer.sltypes.Location_Region import Location_Region
        return data

    def getTimezone(self, identifier: int) -> 'Locale_Timezone':
        """"""
        data = self.client.call('SoftLayer_Location', 'getTimezone', id=identifier)
        from SoftLayer.sltypes.Locale_Timezone import Locale_Timezone
        return data

    def getVdrGroup(self, identifier: int) -> 'Location_Group_Location_CrossReference':
        """"""
        data = self.client.call('SoftLayer_Location', 'getVdrGroup', id=identifier)
        from SoftLayer.sltypes.Location_Group_Location_CrossReference import Location_Group_Location_CrossReference
        return data
