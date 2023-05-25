from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Monitor_Version1_Query_Host(Entity):
    """The Monitoring_Query_Host type represents a monitoring instance.  It consists of a hardware ID to monitor, an
IP address attached to that hardware ID, a method of monitoring, and what to do in the instance that the
monitor ever fails."""
    arg1Value: str
    guestId: int
    hardwareId: int
    hostId: int
    id_: int
    ipAddress: str
    queryTypeId: int
    responseActionId: int
    status: str
    waitCycles: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Monitor_Version1_Query_Host'

    def createObject(self, templateObject: 'Network_Monitor_Version1_Query_Host') -> 'Network_Monitor_Version1_Query_Host':
        """Create a monitoring entry"""
        data = self.client.call('SoftLayer_Network_Monitor_Version1_Query_Host', 'createObject', templateObject)
        return data

    def createObjects(self, templateObjects: 'Network_Monitor_Version1_Query_Host') -> list['Network_Monitor_Version1_Query_Host']:
        """Create multiple monitoring entries at once"""
        data = self.client.call('SoftLayer_Network_Monitor_Version1_Query_Host', 'createObjects', templateObjects)
        return data

    def deleteObject(self, identifier: int) -> bool:
        """Delete a Query_Host object by passing in a version of it"""
        data = self.client.call('SoftLayer_Network_Monitor_Version1_Query_Host', 'deleteObject', id=identifier)
        return data

    def deleteObjects(self, templateObjects: 'Network_Monitor_Version1_Query_Host') -> bool:
        """Delete a group of Query_Host objects by passing in a collection of them"""
        data = self.client.call('SoftLayer_Network_Monitor_Version1_Query_Host', 'deleteObjects', templateObjects)
        return data

    def editObject(self, identifier: int, templateObject: 'Network_Monitor_Version1_Query_Host') -> bool:
        """Edit the object by passing in a modified instance of the object"""
        data = self.client.call('SoftLayer_Network_Monitor_Version1_Query_Host', 'editObject', templateObject, id=identifier)
        return data

    def editObjects(self, templateObjects: 'Network_Monitor_Version1_Query_Host') -> bool:
        """Edit a group of Query_Host objects by passing in a collection of them."""
        data = self.client.call('SoftLayer_Network_Monitor_Version1_Query_Host', 'editObjects', templateObjects)
        return data

    def findByHardwareId(self, hardwareId: int) -> list['Network_Monitor_Version1_Query_Host']:
        """Return all monitoring instances associated with the passed hardware ID"""
        data = self.client.call('SoftLayer_Network_Monitor_Version1_Query_Host', 'findByHardwareId', hardwareId)
        return data

    def getObject(self, identifier: int) -> 'Network_Monitor_Version1_Query_Host':
        """Retrieve a SoftLayer_Network_Monitor_Version1_Query_Host record."""
        data = self.client.call('SoftLayer_Network_Monitor_Version1_Query_Host', 'getObject', id=identifier)
        return data

    def getHardware(self, identifier: int) -> 'Hardware':
        """"""
        data = self.client.call('SoftLayer_Network_Monitor_Version1_Query_Host', 'getHardware', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getLastResult(self, identifier: int) -> 'Network_Monitor_Version1_Query_Result':
        """"""
        data = self.client.call('SoftLayer_Network_Monitor_Version1_Query_Host', 'getLastResult', id=identifier)
        from SoftLayer.sltypes.Network_Monitor_Version1_Query_Result import Network_Monitor_Version1_Query_Result
        return data

    def getQueryType(self, identifier: int) -> 'Network_Monitor_Version1_Query_Type':
        """"""
        data = self.client.call('SoftLayer_Network_Monitor_Version1_Query_Host', 'getQueryType', id=identifier)
        from SoftLayer.sltypes.Network_Monitor_Version1_Query_Type import Network_Monitor_Version1_Query_Type
        return data

    def getResponseAction(self, identifier: int) -> 'Network_Monitor_Version1_Query_ResponseType':
        """"""
        data = self.client.call('SoftLayer_Network_Monitor_Version1_Query_Host', 'getResponseAction', id=identifier)
        from SoftLayer.sltypes.Network_Monitor_Version1_Query_ResponseType import Network_Monitor_Version1_Query_ResponseType
        return data
