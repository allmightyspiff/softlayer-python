from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Subnet_Registration_Status(Entity):
    """Subnet Registration Status objects describe the current status of a subnet registration.   The standard
values for these objects are as follows: <ul> <li><strong>OPEN</strong> - Indicates that the registration
object is new and has yet to be submitted to the RIR</li> <li><strong>PENDING</strong> - Indicates that the
registration object has been submitted to the RIR and is awaiting response</li> <li><strong>COMPLETE</strong>
- Indicates that the RIR action has completed</li> <li><strong>DELETED</strong> - Indicates that the
registration object has been gracefully removed is no longer valid</li> <li><strong>CANCELLED</strong> -
Indicates that the registration object has been abruptly removed is no longer valid</li> </ul>"""
    createDate: datetime
    id_: int
    keyName: str
    modifyDate: datetime
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Subnet_Registration_Status'

    def getAllObjects(self) -> list['Network_Subnet_Registration_Status']:
        data = self.client.call('SoftLayer_Network_Subnet_Registration_Status', 'getAllObjects')
        from SoftLayer.sltypes.Network_Subnet_Registration_Status import Network_Subnet_Registration_Status
        return data

    def getObject(self, identifier: int) -> 'Network_Subnet_Registration_Status':
        """Retrieve a SoftLayer_Network_Subnet_Registration_Status record."""
        data = self.client.call('SoftLayer_Network_Subnet_Registration_Status', 'getObject', id=identifier)
        from SoftLayer.sltypes.Network_Subnet_Registration_Status import Network_Subnet_Registration_Status
        return data
