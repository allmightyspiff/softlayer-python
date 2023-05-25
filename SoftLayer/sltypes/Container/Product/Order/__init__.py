from SoftLayer.sltypes.Virtual.Guest import Virtual_Guest
from SoftLayer.sltypes.Container.Product.Order.Storage.Group import Container_Product_Order_Storage_Group
from SoftLayer.sltypes.Container.Product.Order.SshKeys import Container_Product_Order_SshKeys
from SoftLayer.sltypes.Container.Product.Order.Property import Container_Product_Order_Property
from SoftLayer.sltypes.Sales.Presale.Event import Sales_Presale_Event
from SoftLayer.sltypes.Container.Exception import Container_Exception
from typing import Optional, Self
from SoftLayer.sltypes.Location import Location
from SoftLayer.sltypes.Container.Product.Item.Category.Question.Answer import Container_Product_Item_Category_Question_Answer
from SoftLayer.sltypes.Hardware import Hardware
from SoftLayer.sltypes.Product.Item.Price import Product_Item_Price
from SoftLayer.sltypes.Container.Product.Order.Billing.Information import Container_Product_Order_Billing_Information
from SoftLayer.sltypes.Entity import Entity

class Container_Product_Order(Entity):
    """This is the datatype that needs to be populated and sent to SoftLayer_Product_Order::placeOrder. This
datatype has everything required to place an order with SoftLayer."""
    bigDataOrderFlag: bool
    billingInformation: Container_Product_Order_Billing_Information
    billingOrderItemId: int
    cancelUrl: str
    containerIdentifier: str
    containerSplHash: str
    currencyShortName: str
    deviceFingerprintId: str
    displayLayerSessionId: str
    extendedHardwareTesting: bool
    flexibleCreditProgramPrice: Product_Item_Price
    gdprConsentFlag: bool
    hardware: list[Hardware]
    imageTemplateGlobalIdentifier: str
    imageTemplateId: int
    isManagedOrder: int
    itemCategoryQuestionAnswers: list[Container_Product_Item_Category_Question_Answer]
    location: str
    locationObject: Location
    message: str
    orderContainers: list[Optional[Self]]
    orderHostnames: list[str]
    orderVerificationExceptions: list[Container_Exception]
    packageId: int
    paymentType: str
    postTaxRecurring: float
    postTaxRecurringHourly: float
    postTaxRecurringMonthly: float
    postTaxSetup: float
    preTaxRecurring: float
    preTaxRecurringHourly: float
    preTaxRecurringMonthly: float
    preTaxSetup: float
    presaleEvent: Sales_Presale_Event
    presetId: int
    prices: list[Product_Item_Price]
    primaryDiskPartitionId: int
    priorities: list[str]
    privateCloudOrderFlag: bool
    privateCloudOrderType: str
    promotionCode: str
    properties: list[Container_Product_Order_Property]
    proratedInitialCharge: float
    proratedOrderTotal: float
    provisionScripts: list[str]
    quantity: int
    quoteName: str
    regionalGroup: str
    resourceGroupId: int
    resourceGroupName: str
    resourceGroupTemplateId: int
    returnUrl: str
    sendQuoteEmailFlag: bool
    serverCoreCount: int
    serviceToken: str
    sourceVirtualGuestId: int
    sshKeys: list[Container_Product_Order_SshKeys]
    stepId: int
    storageGroups: list[Container_Product_Order_Storage_Group]
    taxCacheHash: str
    taxCompletedFlag: bool
    techIncubatorItemPrice: Product_Item_Price
    totalRecurringTax: float
    totalSetupTax: float
    usagePrices: list[Product_Item_Price]
    useHourlyPricing: bool
    virtualGuests: list[Virtual_Guest]
