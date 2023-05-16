# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Account(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Account'
        self.client = client

    def activatePartner(
        self,
        accountId: str,
        hashCode: str,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Account':

        data = self.client.call(
            self.service,
            'activatePartner',
            accountId,
            hashCode,
            mask=objectMask
        )
        from SoftLayer.datatypes.Account import Account
        return Account(data)


    def addAchInformation(
        self,
        achInformation: SoftLayer_Container_Billing_Info_Ach
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'addAchInformation',
            achInformation
        )
        
        return data


    def addReferralPartnerPaymentOption(
        self,
        paymentOption: SoftLayer_Container_Referral_Partner_Payment_Option
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'addReferralPartnerPaymentOption',
            paymentOption
        )
        
        return data


    def areVdrUpdatesBlockedForBilling(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'areVdrUpdatesBlockedForBilling',
            
        )
        
        return data


    def cancelPayPalTransaction(
        self,
        token: str,
        payerId: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'cancelPayPalTransaction',
            token,
            payerId
        )
        
        return data


    def completePayPalTransaction(
        self,
        token: str,
        payerId: str
    ) -> 'string':

        data = self.client.call(
            self.service,
            'completePayPalTransaction',
            token,
            payerId
        )
        
        return data


    def countHourlyInstances(
        self,
        
    ) -> 'int':

        data = self.client.call(
            self.service,
            'countHourlyInstances',
            
        )
        
        return data


    def createUser(
        self,
        templateObject: SoftLayer_User_Customer,
        password: str,
        vpnPassword: str,
        silentlyCreateFlag: boolean,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_User_Customer':

        data = self.client.call(
            self.service,
            'createUser',
            templateObject,
            password,
            vpnPassword,
            silentlyCreateFlag,
            mask=objectMask
        )
        from SoftLayer.datatypes.User.Customer import Customer
        return Customer(data)


    def disableEuSupport(
        self,
        
    ) -> 'void':

        data = self.client.call(
            self.service,
            'disableEuSupport',
            
        )
        
        return data


    def disableVpnConfigRequiresVpnManageAttribute(
        self,
        
    ) -> 'void':

        data = self.client.call(
            self.service,
            'disableVpnConfigRequiresVpnManageAttribute',
            
        )
        
        return data


    def editAccount(
        self,
        modifiedAccountInformation: SoftLayer_Account
    ) -> 'SoftLayer_Container_Account_Update_Response':

        data = self.client.call(
            self.service,
            'editAccount',
            modifiedAccountInformation
        )
        from SoftLayer.datatypes.Container.Account.Update.Response import Response
        return Response(data)


    def enableEuSupport(
        self,
        
    ) -> 'void':

        data = self.client.call(
            self.service,
            'enableEuSupport',
            
        )
        
        return data


    def enableVpnConfigRequiresVpnManageAttribute(
        self,
        
    ) -> 'void':

        data = self.client.call(
            self.service,
            'enableVpnConfigRequiresVpnManageAttribute',
            
        )
        
        return data


    def getAccountBackupHistory(
        self,
        startDate: dateTime,
        endDate: dateTime,
        backupStatus: str
    ) -> 'list[SoftLayer_Container_Network_Storage_Evault_WebCc_JobDetails]':

        data = self.client.call(
            self.service,
            'getAccountBackupHistory',
            startDate,
            endDate,
            backupStatus
        )
        from SoftLayer.datatypes.Container.Network.Storage.Evault.WebCc.JobDetails import JobDetails
        return JobDetails(data)


    def getAccountTraitValue(
        self,
        keyName: str
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getAccountTraitValue',
            keyName
        )
        
        return data


    def getActiveOutletPackages(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Product_Package]':

        data = self.client.call(
            self.service,
            'getActiveOutletPackages',
            mask=objectMask
        )
        from SoftLayer.datatypes.Product.Package import Package
        return Package(data)


    def getActivePackages(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Product_Package]':

        data = self.client.call(
            self.service,
            'getActivePackages',
            mask=objectMask
        )
        from SoftLayer.datatypes.Product.Package import Package
        return Package(data)


    def getActivePackagesByAttribute(
        self,
        attributeKeyName: str,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Product_Package]':

        data = self.client.call(
            self.service,
            'getActivePackagesByAttribute',
            attributeKeyName,
            mask=objectMask
        )
        from SoftLayer.datatypes.Product.Package import Package
        return Package(data)


    def getActivePrivateHostedCloudPackages(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Product_Package]':

        data = self.client.call(
            self.service,
            'getActivePrivateHostedCloudPackages',
            mask=objectMask
        )
        from SoftLayer.datatypes.Product.Package import Package
        return Package(data)


    def getAlternateCreditCardData(
        self,
        
    ) -> 'SoftLayer_Container_Account_Payment_Method_CreditCard':

        data = self.client.call(
            self.service,
            'getAlternateCreditCardData',
            
        )
        from SoftLayer.datatypes.Container.Account.Payment.Method.CreditCard import CreditCard
        return CreditCard(data)


    def getAttributeByType(
        self,
        attributeType: str,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Account_Attribute':

        data = self.client.call(
            self.service,
            'getAttributeByType',
            attributeType,
            mask=objectMask
        )
        from SoftLayer.datatypes.Account.Attribute import Attribute
        return Attribute(data)


    def getAuxiliaryNotifications(
        self,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Container_Utility_Message]':

        data = self.client.call(
            self.service,
            'getAuxiliaryNotifications',
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Container.Utility.Message import Message
        return Message(data)


    def getAverageArchiveUsageMetricDataByDate(
        self,
        startDateTime: dateTime,
        endDateTime: dateTime
    ) -> 'float':

        data = self.client.call(
            self.service,
            'getAverageArchiveUsageMetricDataByDate',
            startDateTime,
            endDateTime
        )
        
        return data


    def getAveragePublicUsageMetricDataByDate(
        self,
        startDateTime: dateTime,
        endDateTime: dateTime
    ) -> 'float':

        data = self.client.call(
            self.service,
            'getAveragePublicUsageMetricDataByDate',
            startDateTime,
            endDateTime
        )
        
        return data


    def getBandwidthList(
        self,
        networkType: str,
        direction: str,
        startDate: str,
        endDate: str,
        serverIds: int
    ) -> 'list[SoftLayer_Container_Bandwidth_Usage]':

        data = self.client.call(
            self.service,
            'getBandwidthList',
            networkType,
            direction,
            startDate,
            endDate,
            serverIds
        )
        from SoftLayer.datatypes.Container.Bandwidth.Usage import Usage
        return Usage(data)


    def getCurrentUser(
        self,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_User_Customer':

        data = self.client.call(
            self.service,
            'getCurrentUser',
            mask=objectMask
        )
        from SoftLayer.datatypes.User.Customer import Customer
        return Customer(data)


    def getDedicatedHostsForImageTemplate(
        self,
        imageTemplateId: int,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Virtual_DedicatedHost]':

        data = self.client.call(
            self.service,
            'getDedicatedHostsForImageTemplate',
            imageTemplateId,
            mask=objectMask
        )
        from SoftLayer.datatypes.Virtual.DedicatedHost import DedicatedHost
        return DedicatedHost(data)


    def getFlexibleCreditProgramInfo(
        self,
        forNextBillCycle: boolean
    ) -> 'SoftLayer_Container_Account_Discount_Program':

        data = self.client.call(
            self.service,
            'getFlexibleCreditProgramInfo',
            forNextBillCycle
        )
        from SoftLayer.datatypes.Container.Account.Discount.Program import Program
        return Program(data)


    def getFlexibleCreditProgramsInfo(
        self,
        nextBillingCycleFlag: boolean
    ) -> 'SoftLayer_Container_Account_Discount_Program_Collection':

        data = self.client.call(
            self.service,
            'getFlexibleCreditProgramsInfo',
            nextBillingCycleFlag
        )
        from SoftLayer.datatypes.Container.Account.Discount.Program.Collection import Collection
        return Collection(data)


    def getHardwarePools(
        self,
        
    ) -> 'list[SoftLayer_Container_Hardware_Pool_Details]':

        data = self.client.call(
            self.service,
            'getHardwarePools',
            
        )
        from SoftLayer.datatypes.Container.Hardware.Pool.Details import Details
        return Details(data)


    def getLargestAllowedSubnetCidr(
        self,
        numberOfHosts: int,
        locationId: int
    ) -> 'int':

        data = self.client.call(
            self.service,
            'getLargestAllowedSubnetCidr',
            numberOfHosts,
            locationId
        )
        
        return data


    def getNetAppActiveAccountLicenseKeys(
        self,
        
    ) -> 'list[string]':

        data = self.client.call(
            self.service,
            'getNetAppActiveAccountLicenseKeys',
            
        )
        
        return data


    def getNextInvoiceExcel(
        self,
        documentCreateDate: dateTime
    ) -> 'base64Binary':

        data = self.client.call(
            self.service,
            'getNextInvoiceExcel',
            documentCreateDate
        )
        
        return data


    def getNextInvoicePdf(
        self,
        documentCreateDate: dateTime
    ) -> 'base64Binary':

        data = self.client.call(
            self.service,
            'getNextInvoicePdf',
            documentCreateDate
        )
        
        return data


    def getNextInvoicePdfDetailed(
        self,
        documentCreateDate: dateTime
    ) -> 'base64Binary':

        data = self.client.call(
            self.service,
            'getNextInvoicePdfDetailed',
            documentCreateDate
        )
        
        return data


    def getNextInvoiceZeroFeeItemCounts(
        self,
        
    ) -> 'list[SoftLayer_Container_Product_Item_Category_ZeroFee_Count]':

        data = self.client.call(
            self.service,
            'getNextInvoiceZeroFeeItemCounts',
            
        )
        from SoftLayer.datatypes.Container.Product.Item.Category.ZeroFee.Count import Count
        return Count(data)


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account import Account
        return Account(data)


    def getPendingCreditCardChangeRequestData(
        self,
        
    ) -> 'list[SoftLayer_Container_Account_Payment_Method_CreditCard]':

        data = self.client.call(
            self.service,
            'getPendingCreditCardChangeRequestData',
            
        )
        from SoftLayer.datatypes.Container.Account.Payment.Method.CreditCard import CreditCard
        return CreditCard(data)


    def getReferralPartnerCommissionForecast(
        self,
        
    ) -> 'list[SoftLayer_Container_Referral_Partner_Commission]':

        data = self.client.call(
            self.service,
            'getReferralPartnerCommissionForecast',
            
        )
        from SoftLayer.datatypes.Container.Referral.Partner.Commission import Commission
        return Commission(data)


    def getReferralPartnerCommissionHistory(
        self,
        
    ) -> 'list[SoftLayer_Container_Referral_Partner_Commission]':

        data = self.client.call(
            self.service,
            'getReferralPartnerCommissionHistory',
            
        )
        from SoftLayer.datatypes.Container.Referral.Partner.Commission import Commission
        return Commission(data)


    def getReferralPartnerCommissionPending(
        self,
        
    ) -> 'list[SoftLayer_Container_Referral_Partner_Commission]':

        data = self.client.call(
            self.service,
            'getReferralPartnerCommissionPending',
            
        )
        from SoftLayer.datatypes.Container.Referral.Partner.Commission import Commission
        return Commission(data)


    def getSharedBlockDeviceTemplateGroups(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest_Block_Device_Template_Group]':

        data = self.client.call(
            self.service,
            'getSharedBlockDeviceTemplateGroups',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest.Block.Device.Template.Group import Group
        return Group(data)


    def getTechIncubatorProgramInfo(
        self,
        forNextBillCycle: boolean
    ) -> 'SoftLayer_Container_Account_Discount_Program':

        data = self.client.call(
            self.service,
            'getTechIncubatorProgramInfo',
            forNextBillCycle
        )
        from SoftLayer.datatypes.Container.Account.Discount.Program import Program
        return Program(data)


    def getThirdPartyPoliciesAcceptanceStatus(
        self,
        
    ) -> 'list[SoftLayer_Container_Policy_Acceptance]':

        data = self.client.call(
            self.service,
            'getThirdPartyPoliciesAcceptanceStatus',
            
        )
        from SoftLayer.datatypes.Container.Policy.Acceptance import Acceptance
        return Acceptance(data)


    def getValidSecurityCertificateEntries(
        self,
        
    ) -> 'list[SoftLayer_Security_Certificate_Entry]':

        data = self.client.call(
            self.service,
            'getValidSecurityCertificateEntries',
            
        )
        from SoftLayer.datatypes.Security.Certificate.Entry import Entry
        return Entry(data)


    def getVmWareActiveAccountLicenseKeys(
        self,
        
    ) -> 'list[string]':

        data = self.client.call(
            self.service,
            'getVmWareActiveAccountLicenseKeys',
            
        )
        
        return data


    def getWindowsUpdateStatus(
        self,
        
    ) -> 'list[SoftLayer_Container_Utility_Microsoft_Windows_UpdateServices_Status]':

        data = self.client.call(
            self.service,
            'getWindowsUpdateStatus',
            
        )
        from SoftLayer.datatypes.Container.Utility.Microsoft.Windows.UpdateServices.Status import Status
        return Status(data)


    def hasAttribute(
        self,
        attributeType: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'hasAttribute',
            attributeType
        )
        
        return data


    def hourlyInstanceLimit(
        self,
        
    ) -> 'int':

        data = self.client.call(
            self.service,
            'hourlyInstanceLimit',
            
        )
        
        return data


    def hourlyServerLimit(
        self,
        
    ) -> 'int':

        data = self.client.call(
            self.service,
            'hourlyServerLimit',
            
        )
        
        return data


    def initiatePayerAuthentication(
        self,
        setupInformation: SoftLayer_Billing_Payment_Card_PayerAuthentication_Setup_Information
    ) -> 'SoftLayer_Billing_Payment_Card_PayerAuthentication_Setup':

        data = self.client.call(
            self.service,
            'initiatePayerAuthentication',
            setupInformation
        )
        from SoftLayer.datatypes.Billing.Payment.Card.PayerAuthentication.Setup import Setup
        return Setup(data)


    def isActiveVmwareCustomer(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'isActiveVmwareCustomer',
            
        )
        
        return data


    def isEligibleForLocalCurrencyProgram(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'isEligibleForLocalCurrencyProgram',
            
        )
        
        return data


    def isEligibleToLinkWithPaas(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'isEligibleToLinkWithPaas',
            
        )
        
        return data


    def linkExternalAccount(
        self,
        externalAccountId: str,
        authorizationToken: str,
        externalServiceProviderKey: str
    ) -> 'void':

        data = self.client.call(
            self.service,
            'linkExternalAccount',
            externalAccountId,
            authorizationToken,
            externalServiceProviderKey
        )
        
        return data


    def removeAlternateCreditCard(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'removeAlternateCreditCard',
            
        )
        
        return data


    def requestCreditCardChange(
        self,
        request: SoftLayer_Billing_Payment_Card_ChangeRequest,
        vatId: str,
        paymentRoleName: str,
        onlyChangeNicknameFlag: boolean,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Billing_Payment_Card_ChangeRequest':

        data = self.client.call(
            self.service,
            'requestCreditCardChange',
            request,
            vatId,
            paymentRoleName,
            onlyChangeNicknameFlag,
            mask=objectMask
        )
        from SoftLayer.datatypes.Billing.Payment.Card.ChangeRequest import ChangeRequest
        return ChangeRequest(data)


    def requestManualPayment(
        self,
        request: SoftLayer_Billing_Payment_Card_ManualPayment,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Billing_Payment_Card_ManualPayment':

        data = self.client.call(
            self.service,
            'requestManualPayment',
            request,
            mask=objectMask
        )
        from SoftLayer.datatypes.Billing.Payment.Card.ManualPayment import ManualPayment
        return ManualPayment(data)


    def requestManualPaymentUsingCreditCardOnFile(
        self,
        amount: str,
        payWithAlternateCardFlag: boolean,
        note: str,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Billing_Payment_Card_ManualPayment':

        data = self.client.call(
            self.service,
            'requestManualPaymentUsingCreditCardOnFile',
            amount,
            payWithAlternateCardFlag,
            note,
            mask=objectMask
        )
        from SoftLayer.datatypes.Billing.Payment.Card.ManualPayment import ManualPayment
        return ManualPayment(data)


    def saveInternalCostRecovery(
        self,
        costRecoveryContainer: SoftLayer_Container_Account_Internal_Ibm_CostRecovery
    ) -> 'void':

        data = self.client.call(
            self.service,
            'saveInternalCostRecovery',
            costRecoveryContainer
        )
        
        return data


    def setAbuseEmails(
        self,
        emails: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'setAbuseEmails',
            emails
        )
        
        return data


    def setManagedPoolQuantity(
        self,
        poolKeyName: str,
        backendRouter: str,
        quantity: int
    ) -> 'int':

        data = self.client.call(
            self.service,
            'setManagedPoolQuantity',
            poolKeyName,
            backendRouter,
            quantity
        )
        
        return data


    def setVlanSpan(
        self,
        enabled: boolean
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'setVlanSpan',
            enabled
        )
        
        return data


    def swapCreditCards(
        self,
        
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'swapCreditCards',
            
        )
        
        return data


    def syncCurrentUserPopulationWithPaas(
        self,
        
    ) -> 'void':

        data = self.client.call(
            self.service,
            'syncCurrentUserPopulationWithPaas',
            
        )
        
        return data


    def updateVpnUsersForResource(
        self,
        objectId: int,
        objectType: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'updateVpnUsersForResource',
            objectId,
            objectType
        )
        
        return data


    def validate(
        self,
        account: SoftLayer_Account
    ) -> 'list[string]':

        data = self.client.call(
            self.service,
            'validate',
            account
        )
        
        return data


    def validateManualPaymentAmount(
        self,
        amount: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'validateManualPaymentAmount',
            amount
        )
        
        return data


    def getAbuseEmail(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getAbuseEmail',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getAbuseEmails(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Account_AbuseEmail]':

        data = self.client.call(
            self.service,
            'getAbuseEmails',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Account.AbuseEmail import AbuseEmail
        return AbuseEmail(data)


    def getAccountContacts(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Account_Contact]':

        data = self.client.call(
            self.service,
            'getAccountContacts',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Account.Contact import Contact
        return Contact(data)


    def getAccountLicenses(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Software_AccountLicense]':

        data = self.client.call(
            self.service,
            'getAccountLicenses',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Software.AccountLicense import AccountLicense
        return AccountLicense(data)


    def getAccountLinks(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Account_Link]':

        data = self.client.call(
            self.service,
            'getAccountLinks',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Account.Link import Link
        return Link(data)


    def getAccountStatus(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_Status':

        data = self.client.call(
            self.service,
            'getAccountStatus',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Status import Status
        return Status(data)


    def getActiveAccountDiscountBillingItem(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Item':

        data = self.client.call(
            self.service,
            'getActiveAccountDiscountBillingItem',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Item import Item
        return Item(data)


    def getActiveAccountLicenses(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Software_AccountLicense]':

        data = self.client.call(
            self.service,
            'getActiveAccountLicenses',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Software.AccountLicense import AccountLicense
        return AccountLicense(data)


    def getActiveAddresses(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Account_Address]':

        data = self.client.call(
            self.service,
            'getActiveAddresses',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Account.Address import Address
        return Address(data)


    def getActiveAgreements(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Account_Agreement]':

        data = self.client.call(
            self.service,
            'getActiveAgreements',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Account.Agreement import Agreement
        return Agreement(data)


    def getActiveBillingAgreements(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Account_Agreement]':

        data = self.client.call(
            self.service,
            'getActiveBillingAgreements',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Account.Agreement import Agreement
        return Agreement(data)


    def getActiveCatalystEnrollment(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Catalyst_Enrollment':

        data = self.client.call(
            self.service,
            'getActiveCatalystEnrollment',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Catalyst.Enrollment import Enrollment
        return Enrollment(data)


    def getActiveColocationContainers(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Item]':

        data = self.client.call(
            self.service,
            'getActiveColocationContainers',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Item import Item
        return Item(data)


    def getActiveFlexibleCreditEnrollment(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_FlexibleCredit_Enrollment':

        data = self.client.call(
            self.service,
            'getActiveFlexibleCreditEnrollment',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.FlexibleCredit.Enrollment import Enrollment
        return Enrollment(data)


    def getActiveFlexibleCreditEnrollments(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_FlexibleCredit_Enrollment]':

        data = self.client.call(
            self.service,
            'getActiveFlexibleCreditEnrollments',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.FlexibleCredit.Enrollment import Enrollment
        return Enrollment(data)


    def getActiveNotificationSubscribers(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Notification_Subscriber]':

        data = self.client.call(
            self.service,
            'getActiveNotificationSubscribers',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Notification.Subscriber import Subscriber
        return Subscriber(data)


    def getActiveQuotes(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Order_Quote]':

        data = self.client.call(
            self.service,
            'getActiveQuotes',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Order.Quote import Quote
        return Quote(data)


    def getActiveReservedCapacityAgreements(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Account_Agreement]':

        data = self.client.call(
            self.service,
            'getActiveReservedCapacityAgreements',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Account.Agreement import Agreement
        return Agreement(data)


    def getActiveVirtualLicenses(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Software_VirtualLicense]':

        data = self.client.call(
            self.service,
            'getActiveVirtualLicenses',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Software.VirtualLicense import VirtualLicense
        return VirtualLicense(data)


    def getAdcLoadBalancers(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress]':

        data = self.client.call(
            self.service,
            'getAdcLoadBalancers',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Application.Delivery.Controller.LoadBalancer.VirtualIpAddress import VirtualIpAddress
        return VirtualIpAddress(data)


    def getAddresses(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Account_Address]':

        data = self.client.call(
            self.service,
            'getAddresses',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Account.Address import Address
        return Address(data)


    def getAffiliateId(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getAffiliateId',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getAllBillingItems(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Item]':

        data = self.client.call(
            self.service,
            'getAllBillingItems',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Item import Item
        return Item(data)


    def getAllCommissionBillingItems(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Item]':

        data = self.client.call(
            self.service,
            'getAllCommissionBillingItems',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Item import Item
        return Item(data)


    def getAllRecurringTopLevelBillingItems(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Item]':

        data = self.client.call(
            self.service,
            'getAllRecurringTopLevelBillingItems',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Item import Item
        return Item(data)


    def getAllRecurringTopLevelBillingItemsUnfiltered(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Item]':

        data = self.client.call(
            self.service,
            'getAllRecurringTopLevelBillingItemsUnfiltered',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Item import Item
        return Item(data)


    def getAllSubnetBillingItems(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Item]':

        data = self.client.call(
            self.service,
            'getAllSubnetBillingItems',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Item import Item
        return Item(data)


    def getAllTopLevelBillingItems(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Item]':

        data = self.client.call(
            self.service,
            'getAllTopLevelBillingItems',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Item import Item
        return Item(data)


    def getAllTopLevelBillingItemsUnfiltered(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Item]':

        data = self.client.call(
            self.service,
            'getAllTopLevelBillingItemsUnfiltered',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Item import Item
        return Item(data)


    def getAllowIbmIdSilentMigrationFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getAllowIbmIdSilentMigrationFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getAllowsBluemixAccountLinkingFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getAllowsBluemixAccountLinkingFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getApplicationDeliveryControllers(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Application_Delivery_Controller]':

        data = self.client.call(
            self.service,
            'getApplicationDeliveryControllers',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Application.Delivery.Controller import Controller
        return Controller(data)


    def getAttributes(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Account_Attribute]':

        data = self.client.call(
            self.service,
            'getAttributes',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Account.Attribute import Attribute
        return Attribute(data)


    def getAvailablePublicNetworkVlans(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Vlan]':

        data = self.client.call(
            self.service,
            'getAvailablePublicNetworkVlans',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Vlan import Vlan
        return Vlan(data)


    def getBalance(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getBalance',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getBandwidthAllotments(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Bandwidth_Version1_Allotment]':

        data = self.client.call(
            self.service,
            'getBandwidthAllotments',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Bandwidth.Version1.Allotment import Allotment
        return Allotment(data)


    def getBandwidthAllotmentsOverAllocation(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Bandwidth_Version1_Allotment]':

        data = self.client.call(
            self.service,
            'getBandwidthAllotmentsOverAllocation',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Bandwidth.Version1.Allotment import Allotment
        return Allotment(data)


    def getBandwidthAllotmentsProjectedOverAllocation(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Bandwidth_Version1_Allotment]':

        data = self.client.call(
            self.service,
            'getBandwidthAllotmentsProjectedOverAllocation',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Bandwidth.Version1.Allotment import Allotment
        return Allotment(data)


    def getBareMetalInstances(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':

        data = self.client.call(
            self.service,
            'getBareMetalInstances',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


    def getBillingAgreements(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Account_Agreement]':

        data = self.client.call(
            self.service,
            'getBillingAgreements',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Account.Agreement import Agreement
        return Agreement(data)


    def getBillingInfo(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Info':

        data = self.client.call(
            self.service,
            'getBillingInfo',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Info import Info
        return Info(data)


    def getBlockDeviceTemplateGroups(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest_Block_Device_Template_Group]':

        data = self.client.call(
            self.service,
            'getBlockDeviceTemplateGroups',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest.Block.Device.Template.Group import Group
        return Group(data)


    def getBluemixAccountId(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getBluemixAccountId',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getBluemixAccountLink(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_Link_Bluemix':

        data = self.client.call(
            self.service,
            'getBluemixAccountLink',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Link.Bluemix import Bluemix
        return Bluemix(data)


    def getBluemixLinkedFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getBluemixLinkedFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getBrand(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Brand':

        data = self.client.call(
            self.service,
            'getBrand',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Brand import Brand
        return Brand(data)


    def getBrandAccountFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getBrandAccountFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getBrandKeyName(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getBrandKeyName',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getBusinessPartner(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_Business_Partner':

        data = self.client.call(
            self.service,
            'getBusinessPartner',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Business.Partner import Partner
        return Partner(data)


    def getCanOrderAdditionalVlansFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getCanOrderAdditionalVlansFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getCarts(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Order_Quote]':

        data = self.client.call(
            self.service,
            'getCarts',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Order.Quote import Quote
        return Quote(data)


    def getCatalystEnrollments(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Catalyst_Enrollment]':

        data = self.client.call(
            self.service,
            'getCatalystEnrollments',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Catalyst.Enrollment import Enrollment
        return Enrollment(data)


    def getClosedTickets(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Ticket]':

        data = self.client.call(
            self.service,
            'getClosedTickets',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Ticket import Ticket
        return Ticket(data)


    def getDatacentersWithSubnetAllocations(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Location]':

        data = self.client.call(
            self.service,
            'getDatacentersWithSubnetAllocations',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Location import Location
        return Location(data)


    def getDedicatedHosts(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_DedicatedHost]':

        data = self.client.call(
            self.service,
            'getDedicatedHosts',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.DedicatedHost import DedicatedHost
        return DedicatedHost(data)


    def getDisablePaymentProcessingFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getDisablePaymentProcessingFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getDisplaySupportRepresentativeAssignments(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Account_Attachment_Employee]':

        data = self.client.call(
            self.service,
            'getDisplaySupportRepresentativeAssignments',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Account.Attachment.Employee import Employee
        return Employee(data)


    def getDomainRegistrations(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Dns_Domain_Registration]':

        data = self.client.call(
            self.service,
            'getDomainRegistrations',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Dns.Domain.Registration import Registration
        return Registration(data)


    def getDomains(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Dns_Domain]':

        data = self.client.call(
            self.service,
            'getDomains',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Dns.Domain import Domain
        return Domain(data)


    def getDomainsWithoutSecondaryDnsRecords(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Dns_Domain]':

        data = self.client.call(
            self.service,
            'getDomainsWithoutSecondaryDnsRecords',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Dns.Domain import Domain
        return Domain(data)


    def getEuSupportedFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getEuSupportedFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getEvaultCapacityGB(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'unsignedInt':

        data = self.client.call(
            self.service,
            'getEvaultCapacityGB',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getEvaultMasterUsers(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Account_Password]':

        data = self.client.call(
            self.service,
            'getEvaultMasterUsers',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Account.Password import Password
        return Password(data)


    def getEvaultNetworkStorage(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage]':

        data = self.client.call(
            self.service,
            'getEvaultNetworkStorage',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage import Storage
        return Storage(data)


    def getExpiredSecurityCertificates(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Security_Certificate]':

        data = self.client.call(
            self.service,
            'getExpiredSecurityCertificates',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Security.Certificate import Certificate
        return Certificate(data)


    def getFacilityLogs(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_Access_Facility_Log]':

        data = self.client.call(
            self.service,
            'getFacilityLogs',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.Access.Facility.Log import Log
        return Log(data)


    def getFileBlockBetaAccessFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getFileBlockBetaAccessFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getFlexibleCreditEnrollments(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_FlexibleCredit_Enrollment]':

        data = self.client.call(
            self.service,
            'getFlexibleCreditEnrollments',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.FlexibleCredit.Enrollment import Enrollment
        return Enrollment(data)


    def getForcePaasAccountLinkDate(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getForcePaasAccountLinkDate',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getGlobalIpRecords(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Subnet_IpAddress_Global]':

        data = self.client.call(
            self.service,
            'getGlobalIpRecords',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Subnet.IpAddress.Global import Global
        return Global(data)


    def getGlobalIpv4Records(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Subnet_IpAddress_Global]':

        data = self.client.call(
            self.service,
            'getGlobalIpv4Records',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Subnet.IpAddress.Global import Global
        return Global(data)


    def getGlobalIpv6Records(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Subnet_IpAddress_Global]':

        data = self.client.call(
            self.service,
            'getGlobalIpv6Records',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Subnet.IpAddress.Global import Global
        return Global(data)


    def getGlobalLoadBalancerAccounts(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_LoadBalancer_Global_Account]':

        data = self.client.call(
            self.service,
            'getGlobalLoadBalancerAccounts',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.LoadBalancer.Global.Account import Account
        return Account(data)


    def getHardware(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':

        data = self.client.call(
            self.service,
            'getHardware',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


    def getHardwareOverBandwidthAllocation(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':

        data = self.client.call(
            self.service,
            'getHardwareOverBandwidthAllocation',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


    def getHardwareProjectedOverBandwidthAllocation(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':

        data = self.client.call(
            self.service,
            'getHardwareProjectedOverBandwidthAllocation',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


    def getHardwareWithCpanel(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':

        data = self.client.call(
            self.service,
            'getHardwareWithCpanel',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


    def getHardwareWithHelm(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':

        data = self.client.call(
            self.service,
            'getHardwareWithHelm',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


    def getHardwareWithMcafee(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':

        data = self.client.call(
            self.service,
            'getHardwareWithMcafee',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


    def getHardwareWithMcafeeAntivirusRedhat(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':

        data = self.client.call(
            self.service,
            'getHardwareWithMcafeeAntivirusRedhat',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


    def getHardwareWithMcafeeAntivirusWindows(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':

        data = self.client.call(
            self.service,
            'getHardwareWithMcafeeAntivirusWindows',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


    def getHardwareWithMcafeeIntrusionDetectionSystem(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':

        data = self.client.call(
            self.service,
            'getHardwareWithMcafeeIntrusionDetectionSystem',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


    def getHardwareWithPlesk(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':

        data = self.client.call(
            self.service,
            'getHardwareWithPlesk',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


    def getHardwareWithQuantastor(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':

        data = self.client.call(
            self.service,
            'getHardwareWithQuantastor',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


    def getHardwareWithUrchin(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':

        data = self.client.call(
            self.service,
            'getHardwareWithUrchin',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


    def getHardwareWithWindows(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':

        data = self.client.call(
            self.service,
            'getHardwareWithWindows',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


    def getHasEvaultBareMetalRestorePluginFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getHasEvaultBareMetalRestorePluginFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getHasIderaBareMetalRestorePluginFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getHasIderaBareMetalRestorePluginFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getHasPendingOrder(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'unsignedInt':

        data = self.client.call(
            self.service,
            'getHasPendingOrder',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getHasR1softBareMetalRestorePluginFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getHasR1softBareMetalRestorePluginFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getHourlyBareMetalInstances(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':

        data = self.client.call(
            self.service,
            'getHourlyBareMetalInstances',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


    def getHourlyServiceBillingItems(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Item]':

        data = self.client.call(
            self.service,
            'getHourlyServiceBillingItems',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Item import Item
        return Item(data)


    def getHourlyVirtualGuests(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest]':

        data = self.client.call(
            self.service,
            'getHourlyVirtualGuests',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest import Guest
        return Guest(data)


    def getHubNetworkStorage(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage]':

        data = self.client.call(
            self.service,
            'getHubNetworkStorage',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage import Storage
        return Storage(data)


    def getIbmCustomerNumber(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getIbmCustomerNumber',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getIbmIdAuthenticationRequiredFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getIbmIdAuthenticationRequiredFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getIbmIdMigrationExpirationTimestamp(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getIbmIdMigrationExpirationTimestamp',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getInProgressExternalAccountSetup(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_External_Setup':

        data = self.client.call(
            self.service,
            'getInProgressExternalAccountSetup',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.External.Setup import Setup
        return Setup(data)


    def getInternalCciHostAccountFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getInternalCciHostAccountFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getInternalImageTemplateCreationFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getInternalImageTemplateCreationFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getInternalNotes(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Account_Note]':

        data = self.client.call(
            self.service,
            'getInternalNotes',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Account.Note import Note
        return Note(data)


    def getInternalRestrictionFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getInternalRestrictionFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getInvoices(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Invoice]':

        data = self.client.call(
            self.service,
            'getInvoices',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Invoice import Invoice
        return Invoice(data)


    def getIpAddresses(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Subnet_IpAddress]':

        data = self.client.call(
            self.service,
            'getIpAddresses',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Subnet.IpAddress import IpAddress
        return IpAddress(data)


    def getIscsiIsolationDisabled(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getIscsiIsolationDisabled',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getIscsiNetworkStorage(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage]':

        data = self.client.call(
            self.service,
            'getIscsiNetworkStorage',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage import Storage
        return Storage(data)


    def getLastCanceledBillingItem(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Item':

        data = self.client.call(
            self.service,
            'getLastCanceledBillingItem',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Item import Item
        return Item(data)


    def getLastCancelledServerBillingItem(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Item':

        data = self.client.call(
            self.service,
            'getLastCancelledServerBillingItem',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Item import Item
        return Item(data)


    def getLastFiveClosedAbuseTickets(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Ticket]':

        data = self.client.call(
            self.service,
            'getLastFiveClosedAbuseTickets',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Ticket import Ticket
        return Ticket(data)


    def getLastFiveClosedAccountingTickets(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Ticket]':

        data = self.client.call(
            self.service,
            'getLastFiveClosedAccountingTickets',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Ticket import Ticket
        return Ticket(data)


    def getLastFiveClosedOtherTickets(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Ticket]':

        data = self.client.call(
            self.service,
            'getLastFiveClosedOtherTickets',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Ticket import Ticket
        return Ticket(data)


    def getLastFiveClosedSalesTickets(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Ticket]':

        data = self.client.call(
            self.service,
            'getLastFiveClosedSalesTickets',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Ticket import Ticket
        return Ticket(data)


    def getLastFiveClosedSupportTickets(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Ticket]':

        data = self.client.call(
            self.service,
            'getLastFiveClosedSupportTickets',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Ticket import Ticket
        return Ticket(data)


    def getLastFiveClosedTickets(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Ticket]':

        data = self.client.call(
            self.service,
            'getLastFiveClosedTickets',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Ticket import Ticket
        return Ticket(data)


    def getLatestBillDate(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'dateTime':

        data = self.client.call(
            self.service,
            'getLatestBillDate',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getLatestRecurringInvoice(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Invoice':

        data = self.client.call(
            self.service,
            'getLatestRecurringInvoice',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Invoice import Invoice
        return Invoice(data)


    def getLatestRecurringPendingInvoice(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Invoice':

        data = self.client.call(
            self.service,
            'getLatestRecurringPendingInvoice',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Invoice import Invoice
        return Invoice(data)


    def getLegacyBandwidthAllotments(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Bandwidth_Version1_Allotment]':

        data = self.client.call(
            self.service,
            'getLegacyBandwidthAllotments',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Bandwidth.Version1.Allotment import Allotment
        return Allotment(data)


    def getLegacyIscsiCapacityGB(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'unsignedInt':

        data = self.client.call(
            self.service,
            'getLegacyIscsiCapacityGB',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getLoadBalancers(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_LoadBalancer_VirtualIpAddress]':

        data = self.client.call(
            self.service,
            'getLoadBalancers',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.LoadBalancer.VirtualIpAddress import VirtualIpAddress
        return VirtualIpAddress(data)


    def getLockboxCapacityGB(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'unsignedInt':

        data = self.client.call(
            self.service,
            'getLockboxCapacityGB',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getLockboxNetworkStorage(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage]':

        data = self.client.call(
            self.service,
            'getLockboxNetworkStorage',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage import Storage
        return Storage(data)


    def getManualPaymentsUnderReview(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Payment_Card_ManualPayment]':

        data = self.client.call(
            self.service,
            'getManualPaymentsUnderReview',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Payment.Card.ManualPayment import ManualPayment
        return ManualPayment(data)


    def getMasterUser(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_User_Customer':

        data = self.client.call(
            self.service,
            'getMasterUser',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.User.Customer import Customer
        return Customer(data)


    def getMediaDataTransferRequests(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Account_Media_Data_Transfer_Request]':

        data = self.client.call(
            self.service,
            'getMediaDataTransferRequests',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Account.Media.Data.Transfer.Request import Request
        return Request(data)


    def getMetricTrackingObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Metric_Tracking_Object':

        data = self.client.call(
            self.service,
            'getMetricTrackingObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Metric.Tracking.Object import Object
        return Object(data)


    def getMigratedToIbmCloudPortalFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getMigratedToIbmCloudPortalFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getMonthlyBareMetalInstances(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':

        data = self.client.call(
            self.service,
            'getMonthlyBareMetalInstances',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


    def getMonthlyVirtualGuests(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest]':

        data = self.client.call(
            self.service,
            'getMonthlyVirtualGuests',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest import Guest
        return Guest(data)


    def getNasNetworkStorage(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage]':

        data = self.client.call(
            self.service,
            'getNasNetworkStorage',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage import Storage
        return Storage(data)


    def getNetworkCreationFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getNetworkCreationFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getNetworkGateways(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Gateway]':

        data = self.client.call(
            self.service,
            'getNetworkGateways',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Gateway import Gateway
        return Gateway(data)


    def getNetworkHardware(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':

        data = self.client.call(
            self.service,
            'getNetworkHardware',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


    def getNetworkMessageDeliveryAccounts(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Message_Delivery]':

        data = self.client.call(
            self.service,
            'getNetworkMessageDeliveryAccounts',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Message.Delivery import Delivery
        return Delivery(data)


    def getNetworkMonitorDownHardware(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':

        data = self.client.call(
            self.service,
            'getNetworkMonitorDownHardware',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


    def getNetworkMonitorDownVirtualGuests(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest]':

        data = self.client.call(
            self.service,
            'getNetworkMonitorDownVirtualGuests',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest import Guest
        return Guest(data)


    def getNetworkMonitorRecoveringHardware(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':

        data = self.client.call(
            self.service,
            'getNetworkMonitorRecoveringHardware',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


    def getNetworkMonitorRecoveringVirtualGuests(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest]':

        data = self.client.call(
            self.service,
            'getNetworkMonitorRecoveringVirtualGuests',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest import Guest
        return Guest(data)


    def getNetworkMonitorUpHardware(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':

        data = self.client.call(
            self.service,
            'getNetworkMonitorUpHardware',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


    def getNetworkMonitorUpVirtualGuests(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest]':

        data = self.client.call(
            self.service,
            'getNetworkMonitorUpVirtualGuests',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest import Guest
        return Guest(data)


    def getNetworkStorage(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage]':

        data = self.client.call(
            self.service,
            'getNetworkStorage',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage import Storage
        return Storage(data)


    def getNetworkStorageGroups(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage_Group]':

        data = self.client.call(
            self.service,
            'getNetworkStorageGroups',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage.Group import Group
        return Group(data)


    def getNetworkTunnelContexts(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Tunnel_Module_Context]':

        data = self.client.call(
            self.service,
            'getNetworkTunnelContexts',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Tunnel.Module.Context import Context
        return Context(data)


    def getNetworkVlanSpan(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_Network_Vlan_Span':

        data = self.client.call(
            self.service,
            'getNetworkVlanSpan',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Network.Vlan.Span import Span
        return Span(data)


    def getNetworkVlans(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Vlan]':

        data = self.client.call(
            self.service,
            'getNetworkVlans',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Vlan import Vlan
        return Vlan(data)


    def getNextBillingPublicAllotmentHardwareBandwidthDetails(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Bandwidth_Version1_Allotment]':

        data = self.client.call(
            self.service,
            'getNextBillingPublicAllotmentHardwareBandwidthDetails',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Bandwidth.Version1.Allotment import Allotment
        return Allotment(data)


    def getNextInvoiceIncubatorExemptTotal(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getNextInvoiceIncubatorExemptTotal',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getNextInvoiceRecurringAmountEligibleForAccountDiscount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getNextInvoiceRecurringAmountEligibleForAccountDiscount',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getNextInvoiceTopLevelBillingItems(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Item]':

        data = self.client.call(
            self.service,
            'getNextInvoiceTopLevelBillingItems',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Item import Item
        return Item(data)


    def getNextInvoiceTotalAmount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'float':

        data = self.client.call(
            self.service,
            'getNextInvoiceTotalAmount',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getNextInvoiceTotalOneTimeAmount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getNextInvoiceTotalOneTimeAmount',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getNextInvoiceTotalOneTimeTaxAmount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getNextInvoiceTotalOneTimeTaxAmount',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getNextInvoiceTotalRecurringAmount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getNextInvoiceTotalRecurringAmount',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getNextInvoiceTotalRecurringAmountBeforeAccountDiscount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getNextInvoiceTotalRecurringAmountBeforeAccountDiscount',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getNextInvoiceTotalRecurringTaxAmount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'float':

        data = self.client.call(
            self.service,
            'getNextInvoiceTotalRecurringTaxAmount',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getNextInvoiceTotalTaxableRecurringAmount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getNextInvoiceTotalTaxableRecurringAmount',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getNotificationSubscribers(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Notification_Subscriber]':

        data = self.client.call(
            self.service,
            'getNotificationSubscribers',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Notification.Subscriber import Subscriber
        return Subscriber(data)


    def getOpenAbuseTickets(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Ticket]':

        data = self.client.call(
            self.service,
            'getOpenAbuseTickets',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Ticket import Ticket
        return Ticket(data)


    def getOpenAccountingTickets(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Ticket]':

        data = self.client.call(
            self.service,
            'getOpenAccountingTickets',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Ticket import Ticket
        return Ticket(data)


    def getOpenBillingTickets(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Ticket]':

        data = self.client.call(
            self.service,
            'getOpenBillingTickets',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Ticket import Ticket
        return Ticket(data)


    def getOpenCancellationRequests(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Item_Cancellation_Request]':

        data = self.client.call(
            self.service,
            'getOpenCancellationRequests',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Item.Cancellation.Request import Request
        return Request(data)


    def getOpenOtherTickets(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Ticket]':

        data = self.client.call(
            self.service,
            'getOpenOtherTickets',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Ticket import Ticket
        return Ticket(data)


    def getOpenRecurringInvoices(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Invoice]':

        data = self.client.call(
            self.service,
            'getOpenRecurringInvoices',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Invoice import Invoice
        return Invoice(data)


    def getOpenSalesTickets(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Ticket]':

        data = self.client.call(
            self.service,
            'getOpenSalesTickets',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Ticket import Ticket
        return Ticket(data)


    def getOpenStackAccountLinks(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Account_Link]':

        data = self.client.call(
            self.service,
            'getOpenStackAccountLinks',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Account.Link import Link
        return Link(data)


    def getOpenStackObjectStorage(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage]':

        data = self.client.call(
            self.service,
            'getOpenStackObjectStorage',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage import Storage
        return Storage(data)


    def getOpenSupportTickets(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Ticket]':

        data = self.client.call(
            self.service,
            'getOpenSupportTickets',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Ticket import Ticket
        return Ticket(data)


    def getOpenTickets(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Ticket]':

        data = self.client.call(
            self.service,
            'getOpenTickets',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Ticket import Ticket
        return Ticket(data)


    def getOpenTicketsWaitingOnCustomer(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Ticket]':

        data = self.client.call(
            self.service,
            'getOpenTicketsWaitingOnCustomer',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Ticket import Ticket
        return Ticket(data)


    def getOrders(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Order]':

        data = self.client.call(
            self.service,
            'getOrders',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Order import Order
        return Order(data)


    def getOrphanBillingItems(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Item]':

        data = self.client.call(
            self.service,
            'getOrphanBillingItems',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Item import Item
        return Item(data)


    def getOwnedBrands(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Brand]':

        data = self.client.call(
            self.service,
            'getOwnedBrands',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Brand import Brand
        return Brand(data)


    def getOwnedHardwareGenericComponentModels(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware_Component_Model_Generic]':

        data = self.client.call(
            self.service,
            'getOwnedHardwareGenericComponentModels',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware.Component.Model.Generic import Generic
        return Generic(data)


    def getPaymentProcessors(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Payment_Processor]':

        data = self.client.call(
            self.service,
            'getPaymentProcessors',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Payment.Processor import Processor
        return Processor(data)


    def getPendingEvents(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Notification_Occurrence_Event]':

        data = self.client.call(
            self.service,
            'getPendingEvents',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Notification.Occurrence.Event import Event
        return Event(data)


    def getPendingInvoice(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Invoice':

        data = self.client.call(
            self.service,
            'getPendingInvoice',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Invoice import Invoice
        return Invoice(data)


    def getPendingInvoiceTopLevelItems(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Invoice_Item]':

        data = self.client.call(
            self.service,
            'getPendingInvoiceTopLevelItems',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Invoice.Item import Item
        return Item(data)


    def getPendingInvoiceTotalAmount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getPendingInvoiceTotalAmount',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getPendingInvoiceTotalOneTimeAmount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getPendingInvoiceTotalOneTimeAmount',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getPendingInvoiceTotalOneTimeTaxAmount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getPendingInvoiceTotalOneTimeTaxAmount',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getPendingInvoiceTotalRecurringAmount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getPendingInvoiceTotalRecurringAmount',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getPendingInvoiceTotalRecurringTaxAmount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getPendingInvoiceTotalRecurringTaxAmount',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getPermissionGroups(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_Permission_Group]':

        data = self.client.call(
            self.service,
            'getPermissionGroups',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.Permission.Group import Group
        return Group(data)


    def getPermissionRoles(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_Permission_Role]':

        data = self.client.call(
            self.service,
            'getPermissionRoles',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.Permission.Role import Role
        return Role(data)


    def getPlacementGroups(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_PlacementGroup]':

        data = self.client.call(
            self.service,
            'getPlacementGroups',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.PlacementGroup import PlacementGroup
        return PlacementGroup(data)


    def getPortableStorageVolumes(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Disk_Image]':

        data = self.client.call(
            self.service,
            'getPortableStorageVolumes',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Disk.Image import Image
        return Image(data)


    def getPostProvisioningHooks(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Provisioning_Hook]':

        data = self.client.call(
            self.service,
            'getPostProvisioningHooks',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Provisioning.Hook import Hook
        return Hook(data)


    def getPptpVpnAllowedFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getPptpVpnAllowedFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getPptpVpnUsers(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_Customer]':

        data = self.client.call(
            self.service,
            'getPptpVpnUsers',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.Customer import Customer
        return Customer(data)


    def getPreviousRecurringRevenue(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'decimal':

        data = self.client.call(
            self.service,
            'getPreviousRecurringRevenue',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getPriceRestrictions(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Product_Item_Price_Account_Restriction]':

        data = self.client.call(
            self.service,
            'getPriceRestrictions',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Product.Item.Price.Account.Restriction import Restriction
        return Restriction(data)


    def getPriorityOneTickets(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Ticket]':

        data = self.client.call(
            self.service,
            'getPriorityOneTickets',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Ticket import Ticket
        return Ticket(data)


    def getPrivateAllotmentHardwareBandwidthDetails(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Bandwidth_Version1_Allotment]':

        data = self.client.call(
            self.service,
            'getPrivateAllotmentHardwareBandwidthDetails',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Bandwidth.Version1.Allotment import Allotment
        return Allotment(data)


    def getPrivateBlockDeviceTemplateGroups(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest_Block_Device_Template_Group]':

        data = self.client.call(
            self.service,
            'getPrivateBlockDeviceTemplateGroups',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest.Block.Device.Template.Group import Group
        return Group(data)


    def getPrivateIpAddresses(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Subnet_IpAddress]':

        data = self.client.call(
            self.service,
            'getPrivateIpAddresses',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Subnet.IpAddress import IpAddress
        return IpAddress(data)


    def getPrivateNetworkVlans(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Vlan]':

        data = self.client.call(
            self.service,
            'getPrivateNetworkVlans',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Vlan import Vlan
        return Vlan(data)


    def getPrivateSubnets(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Subnet]':

        data = self.client.call(
            self.service,
            'getPrivateSubnets',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Subnet import Subnet
        return Subnet(data)


    def getProofOfConceptAccountFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getProofOfConceptAccountFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getPublicAllotmentHardwareBandwidthDetails(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Bandwidth_Version1_Allotment]':

        data = self.client.call(
            self.service,
            'getPublicAllotmentHardwareBandwidthDetails',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Bandwidth.Version1.Allotment import Allotment
        return Allotment(data)


    def getPublicIpAddresses(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Subnet_IpAddress]':

        data = self.client.call(
            self.service,
            'getPublicIpAddresses',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Subnet.IpAddress import IpAddress
        return IpAddress(data)


    def getPublicNetworkVlans(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Vlan]':

        data = self.client.call(
            self.service,
            'getPublicNetworkVlans',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Vlan import Vlan
        return Vlan(data)


    def getPublicSubnets(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Subnet]':

        data = self.client.call(
            self.service,
            'getPublicSubnets',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Subnet import Subnet
        return Subnet(data)


    def getQuotes(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Order_Quote]':

        data = self.client.call(
            self.service,
            'getQuotes',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Order.Quote import Quote
        return Quote(data)


    def getRecentEvents(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Notification_Occurrence_Event]':

        data = self.client.call(
            self.service,
            'getRecentEvents',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Notification.Occurrence.Event import Event
        return Event(data)


    def getReferralPartner(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account':

        data = self.client.call(
            self.service,
            'getReferralPartner',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account import Account
        return Account(data)


    def getReferredAccountFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getReferredAccountFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getReferredAccounts(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Account]':

        data = self.client.call(
            self.service,
            'getReferredAccounts',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Account import Account
        return Account(data)


    def getRegulatedWorkloads(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Legal_RegulatedWorkload]':

        data = self.client.call(
            self.service,
            'getRegulatedWorkloads',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Legal.RegulatedWorkload import RegulatedWorkload
        return RegulatedWorkload(data)


    def getRemoteManagementCommandRequests(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware_Component_RemoteManagement_Command_Request]':

        data = self.client.call(
            self.service,
            'getRemoteManagementCommandRequests',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware.Component.RemoteManagement.Command.Request import Request
        return Request(data)


    def getReplicationEvents(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Storage_Event]':

        data = self.client.call(
            self.service,
            'getReplicationEvents',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Storage.Event import Event
        return Event(data)


    def getRequireSilentIBMidUserCreation(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getRequireSilentIBMidUserCreation',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getReservedCapacityAgreements(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Account_Agreement]':

        data = self.client.call(
            self.service,
            'getReservedCapacityAgreements',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Account.Agreement import Agreement
        return Agreement(data)


    def getReservedCapacityGroups(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_ReservedCapacityGroup]':

        data = self.client.call(
            self.service,
            'getReservedCapacityGroups',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.ReservedCapacityGroup import ReservedCapacityGroup
        return ReservedCapacityGroup(data)


    def getRouters(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Hardware]':

        data = self.client.call(
            self.service,
            'getRouters',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


    def getRwhoisData(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Subnet_Rwhois_Data]':

        data = self.client.call(
            self.service,
            'getRwhoisData',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Subnet.Rwhois.Data import Data
        return Data(data)


    def getSamlAuthentication(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_Authentication_Saml':

        data = self.client.call(
            self.service,
            'getSamlAuthentication',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Authentication.Saml import Saml
        return Saml(data)


    def getSecondaryDomains(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Dns_Secondary]':

        data = self.client.call(
            self.service,
            'getSecondaryDomains',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Dns.Secondary import Secondary
        return Secondary(data)


    def getSecurityCertificates(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Security_Certificate]':

        data = self.client.call(
            self.service,
            'getSecurityCertificates',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Security.Certificate import Certificate
        return Certificate(data)


    def getSecurityGroups(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_SecurityGroup]':

        data = self.client.call(
            self.service,
            'getSecurityGroups',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.SecurityGroup import SecurityGroup
        return SecurityGroup(data)


    def getSecurityLevel(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Security_Level':

        data = self.client.call(
            self.service,
            'getSecurityLevel',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Security.Level import Level
        return Level(data)


    def getSecurityScanRequests(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Security_Scanner_Request]':

        data = self.client.call(
            self.service,
            'getSecurityScanRequests',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Security.Scanner.Request import Request
        return Request(data)


    def getServiceBillingItems(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Item]':

        data = self.client.call(
            self.service,
            'getServiceBillingItems',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Item import Item
        return Item(data)


    def getShipments(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Account_Shipment]':

        data = self.client.call(
            self.service,
            'getShipments',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Account.Shipment import Shipment
        return Shipment(data)


    def getSshKeys(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Security_Ssh_Key]':

        data = self.client.call(
            self.service,
            'getSshKeys',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Security.Ssh.Key import Key
        return Key(data)


    def getSslVpnUsers(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_Customer]':

        data = self.client.call(
            self.service,
            'getSslVpnUsers',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.Customer import Customer
        return Customer(data)


    def getStandardPoolVirtualGuests(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest]':

        data = self.client.call(
            self.service,
            'getStandardPoolVirtualGuests',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest import Guest
        return Guest(data)


    def getSubnetRegistrationDetails(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Account_Regional_Registry_Detail]':

        data = self.client.call(
            self.service,
            'getSubnetRegistrationDetails',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Account.Regional.Registry.Detail import Detail
        return Detail(data)


    def getSubnetRegistrations(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Subnet_Registration]':

        data = self.client.call(
            self.service,
            'getSubnetRegistrations',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Subnet.Registration import Registration
        return Registration(data)


    def getSubnets(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Subnet]':

        data = self.client.call(
            self.service,
            'getSubnets',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Subnet import Subnet
        return Subnet(data)


    def getSupportRepresentatives(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_Employee]':

        data = self.client.call(
            self.service,
            'getSupportRepresentatives',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.Employee import Employee
        return Employee(data)


    def getSupportSubscriptions(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Billing_Item]':

        data = self.client.call(
            self.service,
            'getSupportSubscriptions',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Billing.Item import Item
        return Item(data)


    def getSupportTier(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getSupportTier',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getSuppressInvoicesFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getSuppressInvoicesFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getTags(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Tag]':

        data = self.client.call(
            self.service,
            'getTags',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Tag import Tag
        return Tag(data)


    def getTestAccountAttributeFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getTestAccountAttributeFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getTickets(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Ticket]':

        data = self.client.call(
            self.service,
            'getTickets',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Ticket import Ticket
        return Ticket(data)


    def getTicketsClosedInTheLastThreeDays(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Ticket]':

        data = self.client.call(
            self.service,
            'getTicketsClosedInTheLastThreeDays',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Ticket import Ticket
        return Ticket(data)


    def getTicketsClosedToday(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Ticket]':

        data = self.client.call(
            self.service,
            'getTicketsClosedToday',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Ticket import Ticket
        return Ticket(data)


    def getTranscodeAccounts(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Media_Transcode_Account]':

        data = self.client.call(
            self.service,
            'getTranscodeAccounts',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Media.Transcode.Account import Account
        return Account(data)


    def getUpgradeRequests(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Product_Upgrade_Request]':

        data = self.client.call(
            self.service,
            'getUpgradeRequests',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Product.Upgrade.Request import Request
        return Request(data)


    def getUsers(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_User_Customer]':

        data = self.client.call(
            self.service,
            'getUsers',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.User.Customer import Customer
        return Customer(data)


    def getValidSecurityCertificates(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Security_Certificate]':

        data = self.client.call(
            self.service,
            'getValidSecurityCertificates',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Security.Certificate import Certificate
        return Certificate(data)


    def getVdrUpdatesInProgressFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getVdrUpdatesInProgressFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getVirtualDedicatedRacks(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Bandwidth_Version1_Allotment]':

        data = self.client.call(
            self.service,
            'getVirtualDedicatedRacks',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Bandwidth.Version1.Allotment import Allotment
        return Allotment(data)


    def getVirtualDiskImages(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Disk_Image]':

        data = self.client.call(
            self.service,
            'getVirtualDiskImages',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Disk.Image import Image
        return Image(data)


    def getVirtualGuests(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest]':

        data = self.client.call(
            self.service,
            'getVirtualGuests',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest import Guest
        return Guest(data)


    def getVirtualGuestsOverBandwidthAllocation(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest]':

        data = self.client.call(
            self.service,
            'getVirtualGuestsOverBandwidthAllocation',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest import Guest
        return Guest(data)


    def getVirtualGuestsProjectedOverBandwidthAllocation(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest]':

        data = self.client.call(
            self.service,
            'getVirtualGuestsProjectedOverBandwidthAllocation',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest import Guest
        return Guest(data)


    def getVirtualGuestsWithCpanel(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest]':

        data = self.client.call(
            self.service,
            'getVirtualGuestsWithCpanel',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest import Guest
        return Guest(data)


    def getVirtualGuestsWithMcafee(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest]':

        data = self.client.call(
            self.service,
            'getVirtualGuestsWithMcafee',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest import Guest
        return Guest(data)


    def getVirtualGuestsWithMcafeeAntivirusRedhat(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest]':

        data = self.client.call(
            self.service,
            'getVirtualGuestsWithMcafeeAntivirusRedhat',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest import Guest
        return Guest(data)


    def getVirtualGuestsWithMcafeeAntivirusWindows(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest]':

        data = self.client.call(
            self.service,
            'getVirtualGuestsWithMcafeeAntivirusWindows',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest import Guest
        return Guest(data)


    def getVirtualGuestsWithMcafeeIntrusionDetectionSystem(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest]':

        data = self.client.call(
            self.service,
            'getVirtualGuestsWithMcafeeIntrusionDetectionSystem',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest import Guest
        return Guest(data)


    def getVirtualGuestsWithPlesk(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest]':

        data = self.client.call(
            self.service,
            'getVirtualGuestsWithPlesk',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest import Guest
        return Guest(data)


    def getVirtualGuestsWithQuantastor(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest]':

        data = self.client.call(
            self.service,
            'getVirtualGuestsWithQuantastor',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest import Guest
        return Guest(data)


    def getVirtualGuestsWithUrchin(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest]':

        data = self.client.call(
            self.service,
            'getVirtualGuestsWithUrchin',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest import Guest
        return Guest(data)


    def getVirtualPrivateRack(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Bandwidth_Version1_Allotment':

        data = self.client.call(
            self.service,
            'getVirtualPrivateRack',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Bandwidth.Version1.Allotment import Allotment
        return Allotment(data)


    def getVirtualStorageArchiveRepositories(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Storage_Repository]':

        data = self.client.call(
            self.service,
            'getVirtualStorageArchiveRepositories',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Storage.Repository import Repository
        return Repository(data)


    def getVirtualStoragePublicRepositories(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Storage_Repository]':

        data = self.client.call(
            self.service,
            'getVirtualStoragePublicRepositories',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Storage.Repository import Repository
        return Repository(data)


    def getVpcVirtualGuests(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Virtual_Guest]':

        data = self.client.call(
            self.service,
            'getVpcVirtualGuests',
            mask=objectMask,
            filter=objectFilter,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Virtual.Guest import Guest
        return Guest(data)


    def getVpnConfigRequiresVPNManageFlag(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'getVpnConfigRequiresVPNManageFlag',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


