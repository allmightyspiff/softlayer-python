from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Billing_Invoice_Tax_Type(Entity):
    """The invoice tax type data type models a single strategy for handling tax calculations."""
    id_: int
    keyName: str
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Billing_Invoice_Tax_Type'

    def getAllObjects(self) -> list['Billing_Invoice_Tax_Type']:
        data = self.client.call('SoftLayer_Billing_Invoice_Tax_Type', 'getAllObjects')
        return data

    def getObject(self, identifier: int) -> 'Billing_Invoice_Tax_Type':
        """Retrieve a SoftLayer_Billing_Invoice_Tax_Type record."""
        data = self.client.call('SoftLayer_Billing_Invoice_Tax_Type', 'getObject', id=identifier)
        return data
