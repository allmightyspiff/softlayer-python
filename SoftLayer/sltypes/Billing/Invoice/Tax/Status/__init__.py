from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Billing_Invoice_Tax_Status(Entity):
    """The invoice tax status data type models a single status or state that an invoice can reflect in regard to an
integration with a third-party tax calculation service."""
    createDate: datetime
    id_: int
    keyName: str
    modifyDate: datetime
    name: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Billing_Invoice_Tax_Status'

    def getAllObjects(self) -> list['Billing_Invoice_Tax_Status']:
        data = self.client.call('SoftLayer_Billing_Invoice_Tax_Status', 'getAllObjects')
        from SoftLayer.sltypes.Billing_Invoice_Tax_Status import Billing_Invoice_Tax_Status
        return data

    def getObject(self, identifier: int) -> 'Billing_Invoice_Tax_Status':
        """Retrieve a SoftLayer_Billing_Invoice_Tax_Status record."""
        data = self.client.call('SoftLayer_Billing_Invoice_Tax_Status', 'getObject', id=identifier)
        from SoftLayer.sltypes.Billing_Invoice_Tax_Status import Billing_Invoice_Tax_Status
        return data
