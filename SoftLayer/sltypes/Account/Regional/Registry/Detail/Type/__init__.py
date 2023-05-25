from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Account_Regional_Registry_Detail_Type(Entity):
    """Subnet Registration Detail Type objects describe the nature of a
[[SoftLayer_Account_Regional_Registry_Detail]] object.   The standard values for these objects are as
follows: <ul> <li><strong>NETWORK</strong> - The detail object represents the information for a
[[SoftLayer_Network_Subnet|subnet]]</li> <li><strong>NETWORK6</strong> - The detail object represents the
information for an [[SoftLayer_Network_Subnet_Version6|IPv6 subnet]]</li> <li><strong>PERSON</strong> - The
detail object represents the information for a customer with the RIR</li> </ul>"""
    createDate: datetime
    id_: int
    keyName: str
    modifyDate: datetime
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Account_Regional_Registry_Detail_Type'

    def getAllObjects(self) -> list['Account_Regional_Registry_Detail_Type']:
        data = self.client.call('SoftLayer_Account_Regional_Registry_Detail_Type', 'getAllObjects')
        from SoftLayer.sltypes.Account_Regional_Registry_Detail_Type import Account_Regional_Registry_Detail_Type
        return data

    def getObject(self, identifier: int) -> 'Account_Regional_Registry_Detail_Type':
        """Retrieve a SoftLayer_Account_Regional_Registry_Detail_Type record."""
        data = self.client.call('SoftLayer_Account_Regional_Registry_Detail_Type', 'getObject', id=identifier)
        from SoftLayer.sltypes.Account_Regional_Registry_Detail_Type import Account_Regional_Registry_Detail_Type
        return data
