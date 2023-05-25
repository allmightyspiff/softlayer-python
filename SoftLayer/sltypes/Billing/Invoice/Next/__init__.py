from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Billing_Invoice_Next(Entity):
    pass

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Billing_Invoice_Next'

    def getExcel(self, identifier: int, documentCreateDate: datetime) -> str:
        """Retrieve the next billing period's invoice as an Excel."""
        data = self.client.call('SoftLayer_Billing_Invoice_Next', 'getExcel', documentCreateDate, id=identifier)
        return data

    def getPdf(self, identifier: int, documentCreateDate: datetime) -> str:
        """Retrieve the next billing period's invoice as a PDF."""
        data = self.client.call('SoftLayer_Billing_Invoice_Next', 'getPdf', documentCreateDate, id=identifier)
        return data

    def getPdfDetailed(self, identifier: int, documentCreateDate: datetime) -> str:
        """Retrieve the next billing period's detailed invoice as a PDF."""
        data = self.client.call('SoftLayer_Billing_Invoice_Next', 'getPdfDetailed', documentCreateDate, id=identifier)
        return data
