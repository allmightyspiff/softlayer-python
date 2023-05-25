from SoftLayer.sltypes.Location import Location
from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Billing_Item_Chronicle(Entity):
    accountId: int
    associatedBillingItemId: int
    associatedChildrenCount: int
    cancellationDate: datetime
    categoryCode: str
    createDate: datetime
    currentHourlyCharge: float
    cycleStartDate: datetime
    dPart: str
    description: str
    domainName: str
    externalAccountId: str
    hostName: str
    hourlyFlag: bool
    hourlyRecurringFee: float
    hoursUsed: int
    id_: int
    itemId: int
    laborFee: float
    lastBillDate: datetime
    location: Location
    modifyDate: datetime
    nextBillDate: datetime
    oneTimeFee: float
    packageId: int
    parentId: int
    recurringFee: float
    recurringMonths: int
    resourceTableId: int
    resourceTableName: str
    setupFee: float
    topLevelProductGroupName: str
    usageChargeFlag: bool

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Billing_Item_Chronicle'

    def getObject(self, identifier: int) -> 'Billing_Item_Chronicle':
        """Retrieve a SoftLayer_Billing_Item_Chronicle record."""
        data = self.client.call('SoftLayer_Billing_Item_Chronicle', 'getObject', id=identifier)
        return data

    def getAssociatedChildren(self, identifier: int) -> list['Billing_Item_Chronicle']:
        """"""
        data = self.client.call('SoftLayer_Billing_Item_Chronicle', 'getAssociatedChildren', id=identifier)
        return data

    def getProduct(self, identifier: int) -> 'Product_Item':
        """"""
        data = self.client.call('SoftLayer_Billing_Item_Chronicle', 'getProduct', id=identifier)
        from SoftLayer.sltypes.Product_Item import Product_Item
        return data
