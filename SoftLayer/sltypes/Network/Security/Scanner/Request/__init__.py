from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Security_Scanner_Request(Entity):
    """The SoftLayer_Network_Security_Scanner_Request data type represents a single vulnerability scan request. It
provides information on when the scan was created, last updated, and the current status. The status messages
are as follows:  *Scan Pending *Scan Processing *Scan Complete *Scan Cancelled *Generating Report."""
    accountId: int
    createDate: datetime
    guestId: int
    hardwareId: int
    hostId: int
    id_: int
    ipAddress: str
    modifyDate: datetime
    statusId: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Security_Scanner_Request'

    def createObject(self, templateObject: 'Network_Security_Scanner_Request') -> 'Network_Security_Scanner_Request':
        """Create a new vulnerability scan request."""
        data = self.client.call('SoftLayer_Network_Security_Scanner_Request', 'createObject', templateObject)
        from SoftLayer.sltypes.Network_Security_Scanner_Request import Network_Security_Scanner_Request
        return data

    def getObject(self, identifier: int) -> 'Network_Security_Scanner_Request':
        """Retrieve a SoftLayer_Network_Security_Scanner_Request record."""
        data = self.client.call('SoftLayer_Network_Security_Scanner_Request', 'getObject', id=identifier)
        from SoftLayer.sltypes.Network_Security_Scanner_Request import Network_Security_Scanner_Request
        return data

    def getReport(self, identifier: int) -> str:
        """Get the vulnerability report for a scan request."""
        data = self.client.call('SoftLayer_Network_Security_Scanner_Request', 'getReport', id=identifier)
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Network_Security_Scanner_Request', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getGuest(self, identifier: int) -> 'Virtual_Guest':
        """"""
        data = self.client.call('SoftLayer_Network_Security_Scanner_Request', 'getGuest', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest import Virtual_Guest
        return data

    def getHardware(self, identifier: int) -> 'Hardware':
        """"""
        data = self.client.call('SoftLayer_Network_Security_Scanner_Request', 'getHardware', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getRequestorOwnedFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Network_Security_Scanner_Request', 'getRequestorOwnedFlag', id=identifier)
        return data

    def getStatus(self, identifier: int) -> 'Network_Security_Scanner_Request_Status':
        """"""
        data = self.client.call('SoftLayer_Network_Security_Scanner_Request', 'getStatus', id=identifier)
        from SoftLayer.sltypes.Network_Security_Scanner_Request_Status import Network_Security_Scanner_Request_Status
        return data
