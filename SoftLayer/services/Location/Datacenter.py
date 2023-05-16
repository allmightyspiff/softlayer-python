# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Location_Datacenter(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Location_Datacenter'
        self.client = client

    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Location_Datacenter':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Location.Datacenter import Datacenter
        return Datacenter(data)


    def getStatisticsGraphImage(
        self,
        
    ) -> 'base64Binary':

        data = self.client.call(
            self.service,
            'getStatisticsGraphImage',
            
        )
        
        return data


    def getAvailableObjectStorageDatacenters(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Location]':

        data = self.client.call(
            self.service,
            'getAvailableObjectStorageDatacenters',
            mask=objectMask
        )
        from SoftLayer.datatypes.Location import Location
        return Location(data)


    def getDatacenters(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'list[SoftLayer_Location]':

        data = self.client.call(
            self.service,
            'getDatacenters',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Location import Location
        return Location(data)


    def getDatacentersWithVirtualImageStoreServiceResourceRecord(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Location]':

        data = self.client.call(
            self.service,
            'getDatacentersWithVirtualImageStoreServiceResourceRecord',
            mask=objectMask
        )
        from SoftLayer.datatypes.Location import Location
        return Location(data)


    def getViewableDatacenters(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Location]':

        data = self.client.call(
            self.service,
            'getViewableDatacenters',
            mask=objectMask
        )
        from SoftLayer.datatypes.Location import Location
        return Location(data)


    def getViewablePopsAndDataCenters(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Location]':

        data = self.client.call(
            self.service,
            'getViewablePopsAndDataCenters',
            mask=objectMask
        )
        from SoftLayer.datatypes.Location import Location
        return Location(data)


    def getViewablepointOfPresence(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Location]':

        data = self.client.call(
            self.service,
            'getViewablepointOfPresence',
            mask=objectMask
        )
        from SoftLayer.datatypes.Location import Location
        return Location(data)


    def getpointOfPresence(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Location]':

        data = self.client.call(
            self.service,
            'getpointOfPresence',
            mask=objectMask
        )
        from SoftLayer.datatypes.Location import Location
        return Location(data)


    def getActiveItemPresaleEvents(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Sales_Presale_Event]':

        data = self.client.call(
            self.service,
            'getActiveItemPresaleEvents',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Sales.Presale.Event import Event
        return Event(data)


    def getBackendHardwareRouters(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':

        data = self.client.call(
            self.service,
            'getBackendHardwareRouters',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


    def getBoundSubnets(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Subnet]':

        data = self.client.call(
            self.service,
            'getBoundSubnets',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Subnet import Subnet
        return Subnet(data)


    def getBrandCountryRestrictions(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Brand_Restriction_Location_CustomerCountry]':

        data = self.client.call(
            self.service,
            'getBrandCountryRestrictions',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Brand.Restriction.Location.CustomerCountry import CustomerCountry
        return CustomerCountry(data)


    def getFrontendHardwareRouters(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':

        data = self.client.call(
            self.service,
            'getFrontendHardwareRouters',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


    def getHardwareRouters(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':

        data = self.client.call(
            self.service,
            'getHardwareRouters',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


    def getPresaleEvents(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Sales_Presale_Event]':

        data = self.client.call(
            self.service,
            'getPresaleEvents',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Sales.Presale.Event import Event
        return Event(data)


    def getRegionalGroup(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Location_Group_Regional':

        data = self.client.call(
            self.service,
            'getRegionalGroup',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Location.Group.Regional import Regional
        return Regional(data)


    def getRegionalInternetRegistry(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Regional_Internet_Registry':

        data = self.client.call(
            self.service,
            'getRegionalInternetRegistry',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Regional.Internet.Registry import Registry
        return Registry(data)


    def getRoutableBoundSubnets(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Subnet]':

        data = self.client.call(
            self.service,
            'getRoutableBoundSubnets',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Subnet import Subnet
        return Subnet(data)


    def getActivePresaleEvents(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Sales_Presale_Event]':

        data = self.client.call(
            self.service,
            'getActivePresaleEvents',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Sales.Presale.Event import Event
        return Event(data)


    def getBackboneDependents(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Backbone_Location_Dependent]':

        data = self.client.call(
            self.service,
            'getBackboneDependents',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Backbone.Location.Dependent import Dependent
        return Dependent(data)


    def getBnppCompliantFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getBnppCompliantFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getEuCompliantFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getEuCompliantFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getGroups(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Location_Group]':

        data = self.client.call(
            self.service,
            'getGroups',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Location.Group import Group
        return Group(data)


    def getHardwareFirewalls(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':

        data = self.client.call(
            self.service,
            'getHardwareFirewalls',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


    def getLocationAddress(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_Address':

        data = self.client.call(
            self.service,
            'getLocationAddress',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Address import Address
        return Address(data)


    def getLocationAddresses(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Account_Address]':

        data = self.client.call(
            self.service,
            'getLocationAddresses',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Account.Address import Address
        return Address(data)


    def getLocationReservationMember(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Location_Reservation_Rack_Member':

        data = self.client.call(
            self.service,
            'getLocationReservationMember',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Location.Reservation.Rack.Member import Member
        return Member(data)


    def getLocationStatus(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Location_Status':

        data = self.client.call(
            self.service,
            'getLocationStatus',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Location.Status import Status
        return Status(data)


    def getNetworkConfigurationAttribute(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Hardware_Attribute':

        data = self.client.call(
            self.service,
            'getNetworkConfigurationAttribute',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Hardware.Attribute import Attribute
        return Attribute(data)


    def getOnlineSslVpnUserCount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getOnlineSslVpnUserCount',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getPathString(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getPathString',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getPriceGroups(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Location_Group]':

        data = self.client.call(
            self.service,
            'getPriceGroups',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Location.Group import Group
        return Group(data)


    def getRegions(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Location_Region]':

        data = self.client.call(
            self.service,
            'getRegions',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Location.Region import Region
        return Region(data)


    def getTimezone(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Locale_Timezone':

        data = self.client.call(
            self.service,
            'getTimezone',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Locale.Timezone import Timezone
        return Timezone(data)


    def getVdrGroup(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Location_Group_Location_CrossReference':

        data = self.client.call(
            self.service,
            'getVdrGroup',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Location.Group.Location.CrossReference import CrossReference
        return CrossReference(data)


