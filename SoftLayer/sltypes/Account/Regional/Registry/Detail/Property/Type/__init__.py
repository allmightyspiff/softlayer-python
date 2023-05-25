from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Account_Regional_Registry_Detail_Property_Type(Entity):
    """Subnet Registration Detail Property Type objects describe the nature of a
[[SoftLayer_Account_Regional_Registry_Detail_Property]] object. These types use
[http://php.net/pcre.pattern.php Perl-Compatible Regular Expressions] to validate the value of a property
object."""
    createDate: datetime
    id_: int
    keyName: str
    modifyDate: datetime
    name: str
    valueExpression: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Account_Regional_Registry_Detail_Property_Type'

    def getAllObjects(self) -> list['Account_Regional_Registry_Detail_Property_Type']:
        data = self.client.call('SoftLayer_Account_Regional_Registry_Detail_Property_Type', 'getAllObjects')
        from SoftLayer.sltypes.Account_Regional_Registry_Detail_Property_Type import Account_Regional_Registry_Detail_Property_Type
        return data

    def getObject(self, identifier: int) -> 'Account_Regional_Registry_Detail_Property_Type':
        """Retrieve a SoftLayer_Account_Regional_Registry_Detail_Property_Type record."""
        data = self.client.call('SoftLayer_Account_Regional_Registry_Detail_Property_Type', 'getObject', id=identifier)
        from SoftLayer.sltypes.Account_Regional_Registry_Detail_Property_Type import Account_Regional_Registry_Detail_Property_Type
        return data
