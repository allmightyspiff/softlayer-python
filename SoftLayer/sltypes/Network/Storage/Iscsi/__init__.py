from SoftLayer.sltypes.Network.Storage import Network_Storage
from SoftLayer.sltypes.Network_Storage import Network_Storage
from SoftLayer import BaseClient

class Network_Storage_Iscsi(Network_Storage):
    """The iscsi data type provides access to additional information about an iscsi volume such as the snapshot
capacity limit and replication partners."""

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Storage_Iscsi'

    def allowAccessFromHardware(self, identifier: int, hardwareObjectTemplate: 'Hardware') -> bool:
        """Allow access to this volume from a specified SoftLayer_Hardware object."""
        data = self.client.call('SoftLayer_Network_Storage_Iscsi', 'allowAccessFromHardware', hardwareObjectTemplate, id=identifier)
        return data

    def allowAccessFromIpAddress(self, identifier: int, ipAddressObjectTemplate: 'Network_Subnet_IpAddress') -> bool:
        data = self.client.call('SoftLayer_Network_Storage_Iscsi', 'allowAccessFromIpAddress', ipAddressObjectTemplate, id=identifier)
        return data

    def allowAccessFromVirtualGuest(self, identifier: int, virtualGuestObjectTemplate: 'Virtual_Guest') -> bool:
        """Allow access to this volume from a specified SoftLayer_Virtual_Guest object."""
        data = self.client.call('SoftLayer_Network_Storage_Iscsi', 'allowAccessFromVirtualGuest', virtualGuestObjectTemplate, id=identifier)
        return data

    def allowAccessToReplicantFromHardwareList(self, identifier: int, hardwareObjectTemplates: 'Hardware') -> bool:
        """allow access to this replica volume from multiple SoftLayer_Hardware objects."""
        data = self.client.call('SoftLayer_Network_Storage_Iscsi', 'allowAccessToReplicantFromHardwareList', hardwareObjectTemplates, id=identifier)
        return data

    def allowAccessToReplicantFromIpAddressList(self, identifier: int, ipAddressObjectTemplates: 'Network_Subnet_IpAddress') -> bool:
        """allow access to this volume from multiple SoftLayer_Network_Subnet_IpAddress objects."""
        data = self.client.call('SoftLayer_Network_Storage_Iscsi', 'allowAccessToReplicantFromIpAddressList', ipAddressObjectTemplates, id=identifier)
        return data

    def allowAccessToReplicantFromVirtualGuestList(self, identifier: int, virtualGuestObjectTemplates: 'Virtual_Guest') -> bool:
        """allow access to this volume from multiple SoftLayer_Virtual_Guest objects."""
        data = self.client.call('SoftLayer_Network_Storage_Iscsi', 'allowAccessToReplicantFromVirtualGuestList', virtualGuestObjectTemplates, id=identifier)
        return data

    def createOrUpdateLunId(self, identifier: int, lunId: int) -> 'Network_Storage_Property':
        """Creates or updates the LUN ID property on a volume."""
        data = self.client.call('SoftLayer_Network_Storage_Iscsi', 'createOrUpdateLunId', lunId, id=identifier)
        from SoftLayer.sltypes.Network_Storage_Property import Network_Storage_Property
        return data

    def getMaximumExpansionSize(self, identifier: int) -> int:
        """Returns the maximum volume expansion size in GB."""
        data = self.client.call('SoftLayer_Network_Storage_Iscsi', 'getMaximumExpansionSize', id=identifier)
        return data

    def getObject(self, identifier: int) -> 'Network_Storage_Iscsi':
        """Retrieve a SoftLayer_Network_Storage_Iscsi record."""
        data = self.client.call('SoftLayer_Network_Storage_Iscsi', 'getObject', id=identifier)
        from SoftLayer.sltypes.Network_Storage_Iscsi import Network_Storage_Iscsi
        return data

    def getSnapshotsForVolume(self, identifier: int) -> list['Network_Storage']:
        """Retrieves a list of snapshots for a given volume."""
        data = self.client.call('SoftLayer_Network_Storage_Iscsi', 'getSnapshotsForVolume', id=identifier)
        from SoftLayer.sltypes.Network_Storage import Network_Storage
        return data

    def removeAccessFromHardware(self, identifier: int, hardwareObjectTemplate: 'Hardware') -> bool:
        """Remove access to this volume from a specified SoftLayer_Hardware object."""
        data = self.client.call('SoftLayer_Network_Storage_Iscsi', 'removeAccessFromHardware', hardwareObjectTemplate, id=identifier)
        return data

    def removeAccessFromIpAddress(self, identifier: int, ipAddressObjectTemplate: 'Network_Subnet_IpAddress') -> bool:
        data = self.client.call('SoftLayer_Network_Storage_Iscsi', 'removeAccessFromIpAddress', ipAddressObjectTemplate, id=identifier)
        return data

    def removeAccessFromVirtualGuest(self, identifier: int, virtualGuestObjectTemplate: 'Virtual_Guest') -> bool:
        """Remove access to this volume from a specified SoftLayer_Virtual_Guest object."""
        data = self.client.call('SoftLayer_Network_Storage_Iscsi', 'removeAccessFromVirtualGuest', virtualGuestObjectTemplate, id=identifier)
        return data

    def removeAccessToReplicantFromHardwareList(self, identifier: int, hardwareObjectTemplates: 'Hardware') -> bool:
        """Remove access to this volume from multiple SoftLayer_Hardware objects."""
        data = self.client.call('SoftLayer_Network_Storage_Iscsi', 'removeAccessToReplicantFromHardwareList', hardwareObjectTemplates, id=identifier)
        return data

    def removeAccessToReplicantFromIpAddressList(self, identifier: int, ipAddressObjectTemplates: 'Network_Subnet_IpAddress') -> bool:
        """Remove access to this replica volume from multiple SoftLayer_Network_Subnet_IpAddress objects."""
        data = self.client.call('SoftLayer_Network_Storage_Iscsi', 'removeAccessToReplicantFromIpAddressList', ipAddressObjectTemplates, id=identifier)
        return data

    def removeAccessToReplicantFromVirtualGuestList(self, identifier: int, virtualGuestObjectTemplates: 'Virtual_Guest') -> bool:
        """Remove access to this replica volume from multiple SoftLayer_Virtual_Guest objects."""
        data = self.client.call('SoftLayer_Network_Storage_Iscsi', 'removeAccessToReplicantFromVirtualGuestList', virtualGuestObjectTemplates, id=identifier)
        return data
