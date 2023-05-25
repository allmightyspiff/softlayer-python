from SoftLayer.sltypes.Location import Location
from SoftLayer import BaseClient

class Location_Datacenter(Location):
    """SoftLayer_Location_Datacenter extends the [[SoftLayer_Location]] data type to include datacenter-specific
properties."""

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Location_Datacenter'

    def getObject(self, identifier: int) -> 'Location_Datacenter':
        """Retrieve a SoftLayer_Location_Datacenter record."""
        data = self.client.call('SoftLayer_Location_Datacenter', 'getObject', id=identifier)
        from SoftLayer.sltypes.Location_Datacenter import Location_Datacenter
        return data

    def getStatisticsGraphImage(self, identifier: int) -> str:
        """Retrieve a graph of a SoftLayer datacenter's last 48 hours of network activity."""
        data = self.client.call('SoftLayer_Location_Datacenter', 'getStatisticsGraphImage', id=identifier)
        return data

    def getActiveItemPresaleEvents(self, identifier: int) -> list['Sales_Presale_Event']:
        """"""
        data = self.client.call('SoftLayer_Location_Datacenter', 'getActiveItemPresaleEvents', id=identifier)
        from SoftLayer.sltypes.Sales_Presale_Event import Sales_Presale_Event
        return data

    def getBackendHardwareRouters(self, identifier: int) -> list['Hardware']:
        """"""
        data = self.client.call('SoftLayer_Location_Datacenter', 'getBackendHardwareRouters', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getBoundSubnets(self, identifier: int) -> list['Network_Subnet']:
        """"""
        data = self.client.call('SoftLayer_Location_Datacenter', 'getBoundSubnets', id=identifier)
        from SoftLayer.sltypes.Network_Subnet import Network_Subnet
        return data

    def getBrandCountryRestrictions(self, identifier: int) -> list['Brand_Restriction_Location_CustomerCountry']:
        """"""
        data = self.client.call('SoftLayer_Location_Datacenter', 'getBrandCountryRestrictions', id=identifier)
        from SoftLayer.sltypes.Brand_Restriction_Location_CustomerCountry import Brand_Restriction_Location_CustomerCountry
        return data

    def getFrontendHardwareRouters(self, identifier: int) -> list['Hardware']:
        """"""
        data = self.client.call('SoftLayer_Location_Datacenter', 'getFrontendHardwareRouters', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getHardwareRouters(self, identifier: int) -> list['Hardware']:
        """"""
        data = self.client.call('SoftLayer_Location_Datacenter', 'getHardwareRouters', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getPresaleEvents(self, identifier: int) -> list['Sales_Presale_Event']:
        """"""
        data = self.client.call('SoftLayer_Location_Datacenter', 'getPresaleEvents', id=identifier)
        from SoftLayer.sltypes.Sales_Presale_Event import Sales_Presale_Event
        return data

    def getRegionalGroup(self, identifier: int) -> 'Location_Group_Regional':
        """"""
        data = self.client.call('SoftLayer_Location_Datacenter', 'getRegionalGroup', id=identifier)
        from SoftLayer.sltypes.Location_Group_Regional import Location_Group_Regional
        return data

    def getRegionalInternetRegistry(self, identifier: int) -> 'Network_Regional_Internet_Registry':
        """"""
        data = self.client.call('SoftLayer_Location_Datacenter', 'getRegionalInternetRegistry', id=identifier)
        from SoftLayer.sltypes.Network_Regional_Internet_Registry import Network_Regional_Internet_Registry
        return data

    def getRoutableBoundSubnets(self, identifier: int) -> list['Network_Subnet']:
        """"""
        data = self.client.call('SoftLayer_Location_Datacenter', 'getRoutableBoundSubnets', id=identifier)
        from SoftLayer.sltypes.Network_Subnet import Network_Subnet
        return data
