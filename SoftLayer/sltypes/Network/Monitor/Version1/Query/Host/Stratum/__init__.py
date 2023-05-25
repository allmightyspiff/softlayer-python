from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Monitor_Version1_Query_Host_Stratum(Entity):
    """The monitoring stratum type stores the maximum level of the various components of the monitoring system that
a particular hardware object has access to.  This object cannot be accessed by ID, and cannot be modified.
The user can access this object through Hardware_Server->availableMonitoring.   There are two values on this
object that are important:  # monitorLevel determines the highest level of
SoftLayer_Network_Monitor_Version1_Query_Type object that can be placed in a monitoring instance on this
server # responseLevel determines the highest level of SoftLayer_Network_Monitor_Version1_Query_ResponseType
object that can be placed in a monitoring instance on this server   Also note that the query type and
response types are available through getAllQueryTypes and getAllResponseTypes, respectively."""
    monitorLevel: int
    responseLevel: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Monitor_Version1_Query_Host_Stratum'

    def getAllQueryTypes(self) -> list['Network_Monitor_Version1_Query_Type']:
        """Return all Query_Type objects."""
        data = self.client.call('SoftLayer_Network_Monitor_Version1_Query_Host_Stratum', 'getAllQueryTypes')
        from SoftLayer.sltypes.Network_Monitor_Version1_Query_Type import Network_Monitor_Version1_Query_Type
        return data

    def getAllResponseTypes(self) -> list['Network_Monitor_Version1_Query_ResponseType']:
        """Return all ResponseType objects."""
        data = self.client.call('SoftLayer_Network_Monitor_Version1_Query_Host_Stratum', 'getAllResponseTypes')
        from SoftLayer.sltypes.Network_Monitor_Version1_Query_ResponseType import Network_Monitor_Version1_Query_ResponseType
        return data

    def getObject(self, identifier: int) -> 'Network_Monitor_Version1_Query_Host_Stratum':
        """Retrieve a SoftLayer_Network_Monitor_Version1_Query_Host_Stratum record."""
        data = self.client.call('SoftLayer_Network_Monitor_Version1_Query_Host_Stratum', 'getObject', id=identifier)
        from SoftLayer.sltypes.Network_Monitor_Version1_Query_Host_Stratum import Network_Monitor_Version1_Query_Host_Stratum
        return data

    def getHardware(self, identifier: int) -> 'Hardware':
        """"""
        data = self.client.call('SoftLayer_Network_Monitor_Version1_Query_Host_Stratum', 'getHardware', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data
