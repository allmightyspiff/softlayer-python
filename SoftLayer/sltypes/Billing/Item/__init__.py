from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Billing_Item(Entity):
    """Every individual item that a SoftLayer customer is billed for is recorded in the SoftLayer_Billing_Item data
type. Billing items range from server chassis to hard drives to control panels, bandwidth quota upgrades and
port upgrade charges. Softlayer [[SoftLayer_Billing_Invoice|invoices]] are generated from the cost of a
customer's billing items. Billing items are copied from the product catalog as they're ordered by customers
to create a reference between an account and the billable items they own.   Billing items exist in a tree
relationship. Items are associated with each other by parent/child relationships. Component items such as
CPU's, RAM, and software each have a parent billing item for the server chassis they're associated with.
Billing Items with a null parent item do not have an associated parent item."""
    allowCancellationFlag: int
    associatedBillingItemId: str
    cancellationDate: datetime
    categoryCode: str
    createDate: datetime
    currentHourlyCharge: str
    cycleStartDate: datetime
    description: str
    domainName: str
    hostName: str
    hourlyRecurringFee: float
    hoursUsed: str
    id_: int
    laborFee: float
    laborFeeTaxRate: float
    lastBillDate: datetime
    modifyDate: datetime
    nextBillDate: datetime
    notes: str
    oneTimeFee: float
    oneTimeFeeTaxRate: float
    orderItemId: int
    packageId: int
    parentId: int
    recurringFee: float
    recurringFeeTaxRate: float
    recurringMonths: int
    serviceProviderId: int
    setupFee: float
    setupFeeTaxRate: float

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Billing_Item'

    def cancelItem(self, identifier: int, cancelImmediately: bool, cancelAssociatedBillingItems: bool, reason: str, customerNote: str) -> bool:
        """Cancel a service or resource."""
        data = self.client.call('SoftLayer_Billing_Item', 'cancelItem', cancelImmediately, cancelAssociatedBillingItems, reason, customerNote, id=identifier)
        return data

    def cancelService(self, identifier: int) -> bool:
        """Cancel a service or resource immediately. This does not include bare metal servers."""
        data = self.client.call('SoftLayer_Billing_Item', 'cancelService', id=identifier)
        return data

    def cancelServiceOnAnniversaryDate(self, identifier: int) -> bool:
        """Cancel a service or resource on the next bill date"""
        data = self.client.call('SoftLayer_Billing_Item', 'cancelServiceOnAnniversaryDate', id=identifier)
        return data

    def getObject(self, identifier: int) -> 'Billing_Item':
        """Retrieve a SoftLayer_Billing_Item record."""
        data = self.client.call('SoftLayer_Billing_Item', 'getObject', id=identifier)
        return data

    def getServiceBillingItemsByCategory(self, categoryCode: str, includeZeroRecurringFee: bool) -> list['Billing_Item']:
        """Returns billing item in a given category code. Use this method to retrieve service billing items that you
wish to cancel."""
        data = self.client.call('SoftLayer_Billing_Item', 'getServiceBillingItemsByCategory', categoryCode, includeZeroRecurringFee)
        return data

    def removeAssociationId(self, identifier: int) -> bool:
        """Remove an association from an orphan billing item."""
        data = self.client.call('SoftLayer_Billing_Item', 'removeAssociationId', id=identifier)
        return data

    def setAssociationId(self, identifier: int, associatedId: int) -> bool:
        """Set the associated billing item for an orphan billing item."""
        data = self.client.call('SoftLayer_Billing_Item', 'setAssociationId', associatedId, id=identifier)
        return data

    def voidCancelService(self, identifier: int) -> bool:
        """Void a service cancellation that was previously made."""
        data = self.client.call('SoftLayer_Billing_Item', 'voidCancelService', id=identifier)
        return data

    def getAccount(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Billing_Item', 'getAccount', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getActiveAgreement(self, identifier: int) -> 'Account_Agreement':
        """"""
        data = self.client.call('SoftLayer_Billing_Item', 'getActiveAgreement', id=identifier)
        from SoftLayer.sltypes.Account_Agreement import Account_Agreement
        return data

    def getActiveAgreementFlag(self, identifier: int) -> 'Account_Agreement':
        """"""
        data = self.client.call('SoftLayer_Billing_Item', 'getActiveAgreementFlag', id=identifier)
        from SoftLayer.sltypes.Account_Agreement import Account_Agreement
        return data

    def getActiveAssociatedChildren(self, identifier: int) -> list['Billing_Item']:
        """"""
        data = self.client.call('SoftLayer_Billing_Item', 'getActiveAssociatedChildren', id=identifier)
        return data

    def getActiveAssociatedGuestDiskBillingItems(self, identifier: int) -> list['Billing_Item']:
        """"""
        data = self.client.call('SoftLayer_Billing_Item', 'getActiveAssociatedGuestDiskBillingItems', id=identifier)
        return data

    def getActiveBundledItems(self, identifier: int) -> list['Billing_Item']:
        """"""
        data = self.client.call('SoftLayer_Billing_Item', 'getActiveBundledItems', id=identifier)
        return data

    def getActiveCancellationItem(self, identifier: int) -> 'Billing_Item_Cancellation_Request_Item':
        """"""
        data = self.client.call('SoftLayer_Billing_Item', 'getActiveCancellationItem', id=identifier)
        from SoftLayer.sltypes.Billing_Item_Cancellation_Request_Item import Billing_Item_Cancellation_Request_Item
        return data

    def getActiveChildren(self, identifier: int) -> list['Billing_Item']:
        """"""
        data = self.client.call('SoftLayer_Billing_Item', 'getActiveChildren', id=identifier)
        return data

    def getActiveFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Billing_Item', 'getActiveFlag', id=identifier)
        return data

    def getActiveSparePoolAssociatedGuestDiskBillingItems(self, identifier: int) -> list['Billing_Item']:
        """"""
        data = self.client.call('SoftLayer_Billing_Item', 'getActiveSparePoolAssociatedGuestDiskBillingItems', id=identifier)
        return data

    def getActiveSparePoolBundledItems(self, identifier: int) -> list['Billing_Item']:
        """"""
        data = self.client.call('SoftLayer_Billing_Item', 'getActiveSparePoolBundledItems', id=identifier)
        return data

    def getAssociatedBillingItem(self, identifier: int) -> 'Billing_Item':
        """"""
        data = self.client.call('SoftLayer_Billing_Item', 'getAssociatedBillingItem', id=identifier)
        return data

    def getAssociatedBillingItemHistory(self, identifier: int) -> list['Billing_Item_Association_History']:
        """"""
        data = self.client.call('SoftLayer_Billing_Item', 'getAssociatedBillingItemHistory', id=identifier)
        from SoftLayer.sltypes.Billing_Item_Association_History import Billing_Item_Association_History
        return data

    def getAssociatedChildren(self, identifier: int) -> list['Billing_Item']:
        """"""
        data = self.client.call('SoftLayer_Billing_Item', 'getAssociatedChildren', id=identifier)
        return data

    def getAssociatedParent(self, identifier: int) -> list['Billing_Item']:
        """"""
        data = self.client.call('SoftLayer_Billing_Item', 'getAssociatedParent', id=identifier)
        return data

    def getAvailableMatchingVlans(self, identifier: int) -> list['Network_Vlan']:
        """"""
        data = self.client.call('SoftLayer_Billing_Item', 'getAvailableMatchingVlans', id=identifier)
        from SoftLayer.sltypes.Network_Vlan import Network_Vlan
        return data

    def getBandwidthAllocation(self, identifier: int) -> 'Network_Bandwidth_Version1_Allocation':
        """"""
        data = self.client.call('SoftLayer_Billing_Item', 'getBandwidthAllocation', id=identifier)
        from SoftLayer.sltypes.Network_Bandwidth_Version1_Allocation import Network_Bandwidth_Version1_Allocation
        return data

    def getBillableChildren(self, identifier: int) -> list['Billing_Item']:
        """"""
        data = self.client.call('SoftLayer_Billing_Item', 'getBillableChildren', id=identifier)
        return data

    def getBundledItems(self, identifier: int) -> list['Billing_Item']:
        """"""
        data = self.client.call('SoftLayer_Billing_Item', 'getBundledItems', id=identifier)
        return data

    def getCanceledChildren(self, identifier: int) -> list['Billing_Item']:
        """"""
        data = self.client.call('SoftLayer_Billing_Item', 'getCanceledChildren', id=identifier)
        return data

    def getCancellationReason(self, identifier: int) -> 'Billing_Item_Cancellation_Reason':
        """"""
        data = self.client.call('SoftLayer_Billing_Item', 'getCancellationReason', id=identifier)
        from SoftLayer.sltypes.Billing_Item_Cancellation_Reason import Billing_Item_Cancellation_Reason
        return data

    def getCancellationRequests(self, identifier: int) -> list['Billing_Item_Cancellation_Request']:
        """"""
        data = self.client.call('SoftLayer_Billing_Item', 'getCancellationRequests', id=identifier)
        from SoftLayer.sltypes.Billing_Item_Cancellation_Request import Billing_Item_Cancellation_Request
        return data

    def getCategory(self, identifier: int) -> 'Product_Item_Category':
        """"""
        data = self.client.call('SoftLayer_Billing_Item', 'getCategory', id=identifier)
        from SoftLayer.sltypes.Product_Item_Category import Product_Item_Category
        return data

    def getChildren(self, identifier: int) -> list['Billing_Item']:
        """"""
        data = self.client.call('SoftLayer_Billing_Item', 'getChildren', id=identifier)
        return data

    def getChildrenWithActiveAgreement(self, identifier: int) -> list['Billing_Item']:
        """"""
        data = self.client.call('SoftLayer_Billing_Item', 'getChildrenWithActiveAgreement', id=identifier)
        return data

    def getDowngradeItems(self, identifier: int) -> list['Product_Item']:
        """"""
        data = self.client.call('SoftLayer_Billing_Item', 'getDowngradeItems', id=identifier)
        from SoftLayer.sltypes.Product_Item import Product_Item
        return data

    def getFilteredNextInvoiceChildren(self, identifier: int) -> list['Billing_Item']:
        """"""
        data = self.client.call('SoftLayer_Billing_Item', 'getFilteredNextInvoiceChildren', id=identifier)
        return data

    def getHourlyFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Billing_Item', 'getHourlyFlag', id=identifier)
        return data

    def getInvoiceItem(self, identifier: int) -> 'Billing_Invoice_Item':
        """"""
        data = self.client.call('SoftLayer_Billing_Item', 'getInvoiceItem', id=identifier)
        from SoftLayer.sltypes.Billing_Invoice_Item import Billing_Invoice_Item
        return data

    def getInvoiceItems(self, identifier: int) -> list['Billing_Invoice_Item']:
        """"""
        data = self.client.call('SoftLayer_Billing_Item', 'getInvoiceItems', id=identifier)
        from SoftLayer.sltypes.Billing_Invoice_Item import Billing_Invoice_Item
        return data

    def getItem(self, identifier: int) -> 'Product_Item':
        """"""
        data = self.client.call('SoftLayer_Billing_Item', 'getItem', id=identifier)
        from SoftLayer.sltypes.Product_Item import Product_Item
        return data

    def getLocation(self, identifier: int) -> 'Location':
        """"""
        data = self.client.call('SoftLayer_Billing_Item', 'getLocation', id=identifier)
        from SoftLayer.sltypes.Location import Location
        return data

    def getNextInvoiceChildren(self, identifier: int) -> list['Billing_Item']:
        """"""
        data = self.client.call('SoftLayer_Billing_Item', 'getNextInvoiceChildren', id=identifier)
        return data

    def getNextInvoiceTotalOneTimeAmount(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Billing_Item', 'getNextInvoiceTotalOneTimeAmount', id=identifier)
        return data

    def getNextInvoiceTotalOneTimeTaxAmount(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Billing_Item', 'getNextInvoiceTotalOneTimeTaxAmount', id=identifier)
        return data

    def getNextInvoiceTotalRecurringAmount(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Billing_Item', 'getNextInvoiceTotalRecurringAmount', id=identifier)
        return data

    def getNextInvoiceTotalRecurringTaxAmount(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Billing_Item', 'getNextInvoiceTotalRecurringTaxAmount', id=identifier)
        return data

    def getNonZeroNextInvoiceChildren(self, identifier: int) -> list['Billing_Item']:
        """"""
        data = self.client.call('SoftLayer_Billing_Item', 'getNonZeroNextInvoiceChildren', id=identifier)
        return data

    def getOrderItem(self, identifier: int) -> 'Billing_Order_Item':
        """"""
        data = self.client.call('SoftLayer_Billing_Item', 'getOrderItem', id=identifier)
        from SoftLayer.sltypes.Billing_Order_Item import Billing_Order_Item
        return data

    def getOriginalLocation(self, identifier: int) -> 'Location':
        """"""
        data = self.client.call('SoftLayer_Billing_Item', 'getOriginalLocation', id=identifier)
        from SoftLayer.sltypes.Location import Location
        return data

    def getPackage(self, identifier: int) -> 'Product_Package':
        """"""
        data = self.client.call('SoftLayer_Billing_Item', 'getPackage', id=identifier)
        from SoftLayer.sltypes.Product_Package import Product_Package
        return data

    def getParent(self, identifier: int) -> 'Billing_Item':
        """"""
        data = self.client.call('SoftLayer_Billing_Item', 'getParent', id=identifier)
        return data

    def getParentVirtualGuestBillingItem(self, identifier: int) -> 'Billing_Item_Virtual_Guest':
        """"""
        data = self.client.call('SoftLayer_Billing_Item', 'getParentVirtualGuestBillingItem', id=identifier)
        from SoftLayer.sltypes.Billing_Item_Virtual_Guest import Billing_Item_Virtual_Guest
        return data

    def getPendingCancellationFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Billing_Item', 'getPendingCancellationFlag', id=identifier)
        return data

    def getPendingOrderItem(self, identifier: int) -> 'Billing_Order_Item':
        """"""
        data = self.client.call('SoftLayer_Billing_Item', 'getPendingOrderItem', id=identifier)
        from SoftLayer.sltypes.Billing_Order_Item import Billing_Order_Item
        return data

    def getProvisionTransaction(self, identifier: int) -> 'Provisioning_Version1_Transaction':
        """"""
        data = self.client.call('SoftLayer_Billing_Item', 'getProvisionTransaction', id=identifier)
        from SoftLayer.sltypes.Provisioning_Version1_Transaction import Provisioning_Version1_Transaction
        return data

    def getSoftwareDescription(self, identifier: int) -> 'Software_Description':
        """"""
        data = self.client.call('SoftLayer_Billing_Item', 'getSoftwareDescription', id=identifier)
        from SoftLayer.sltypes.Software_Description import Software_Description
        return data

    def getUpgradeItem(self, identifier: int) -> 'Product_Item':
        """"""
        data = self.client.call('SoftLayer_Billing_Item', 'getUpgradeItem', id=identifier)
        from SoftLayer.sltypes.Product_Item import Product_Item
        return data

    def getUpgradeItems(self, identifier: int) -> list['Product_Item']:
        """"""
        data = self.client.call('SoftLayer_Billing_Item', 'getUpgradeItems', id=identifier)
        from SoftLayer.sltypes.Product_Item import Product_Item
        return data
