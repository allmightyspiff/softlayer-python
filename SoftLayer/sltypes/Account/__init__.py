from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Account(Entity):
    """The SoftLayer_Account data type contains general information relating to a single SoftLayer customer account.
Personal information in this type such as names, addresses, and phone numbers are assigned to the account
only and not to users belonging to the account. The SoftLayer_Account data type contains a number of
relational properties that are used by the SoftLayer customer portal to quickly present a variety of account
related services to it's users.   SoftLayer customers are unable to change their company account information
in the portal or the API. If you need to change this information please open a sales ticket in our customer
portal and our account management staff will assist you."""
    accountManagedResourcesFlag: bool
    accountStatusId: int
    address1: str
    address2: str
    allowedPptpVpnQuantity: int
    alternatePhone: str
    brandId: int
    city: str
    claimedTaxExemptTxFlag: bool
    companyName: str
    country: str
    createDate: datetime
    deviceFingerprintId: str
    email: str
    faxPhone: str
    firstName: str
    id_: int
    isReseller: int
    lastName: str
    lateFeeProtectionFlag: bool
    modifyDate: datetime
    officePhone: str
    postalCode: str
    resellerLevel: int
    state: str
    statusDate: datetime

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Account'

    def activatePartner(self, accountId: str, hashCode: str) -> 'Account':
        """This service enables a partner account that has been created but is currently inactive. This restricted
service is only available for certain accounts. Please contact support for questions."""
        data = self.client.call('SoftLayer_Account', 'activatePartner', accountId, hashCode)
        from SoftLayer.sltypes.Account import Account
        return data

    def addAchInformation(self, achInformation: 'Container_Billing_Info_Ach') -> bool:
        data = self.client.call('SoftLayer_Account', 'addAchInformation', achInformation)
        return data

    def addReferralPartnerPaymentOption(self, paymentOption: 'Container_Referral_Partner_Payment_Option') -> bool:
        data = self.client.call('SoftLayer_Account', 'addReferralPartnerPaymentOption', paymentOption)
        return data

    def areVdrUpdatesBlockedForBilling(self) -> bool:
        """This method returns true if Bandwidth Pooling updates are blocked so billing can run for this account."""
        data = self.client.call('SoftLayer_Account', 'areVdrUpdatesBlockedForBilling')
        return data

    def cancelPayPalTransaction(self, token: str, payerId: str) -> bool:
        """Cancel the PayPal Payment Request process."""
        data = self.client.call('SoftLayer_Account', 'cancelPayPalTransaction', token, payerId)
        return data

    def completePayPalTransaction(self, token: str, payerId: str) -> str:
        """Complete the PayPal Payment Request process and receive confirmation message."""
        data = self.client.call('SoftLayer_Account', 'completePayPalTransaction', token, payerId)
        return data

    def countHourlyInstances(self) -> int:
        """Retrieve the number of hourly services on an account that are active, plus any pending orders with hourly
services attached."""
        data = self.client.call('SoftLayer_Account', 'countHourlyInstances')
        return data

    def createUser(self, templateObject: 'User_Customer', password: str, vpnPassword: str, silentlyCreateFlag: bool) -> 'User_Customer':
        """Create a new user record, optionally skipping the IBMid email ("silently")."""
        data = self.client.call('SoftLayer_Account', 'createUser', templateObject, password, vpnPassword, silentlyCreateFlag)
        from SoftLayer.sltypes.User_Customer import User_Customer
        return data

    def disableEuSupport(self) -> None:
        """Turn off the EU Supported account flag."""
        data = self.client.call('SoftLayer_Account', 'disableEuSupport')
        return data

    def disableVpnConfigRequiresVpnManageAttribute(self) -> None:
        """Disable the VPN Config Requires VPN Manage attribute, creating it if necessary."""
        data = self.client.call('SoftLayer_Account', 'disableVpnConfigRequiresVpnManageAttribute')
        return data

    def editAccount(self, modifiedAccountInformation: 'Account') -> 'Container_Account_Update_Response':
        """Edit an account's information."""
        data = self.client.call('SoftLayer_Account', 'editAccount', modifiedAccountInformation)
        from SoftLayer.sltypes.Container_Account_Update_Response import Container_Account_Update_Response
        return data

    def enableEuSupport(self) -> None:
        """Turn on the EU Supported account flag."""
        data = self.client.call('SoftLayer_Account', 'enableEuSupport')
        return data

    def enableVpnConfigRequiresVpnManageAttribute(self) -> None:
        """Enable the VPN Config Requires VPN Manage attribute, creating it if necessary."""
        data = self.client.call('SoftLayer_Account', 'enableVpnConfigRequiresVpnManageAttribute')
        return data

    def getAccountBackupHistory(self, startDate: datetime, endDate: datetime, backupStatus: str) -> list['Container_Network_Storage_Evault_WebCc_JobDetails']:
        """This method provides a history of account backups."""
        data = self.client.call('SoftLayer_Account', 'getAccountBackupHistory', startDate, endDate, backupStatus)
        from SoftLayer.sltypes.Container_Network_Storage_Evault_WebCc_JobDetails import Container_Network_Storage_Evault_WebCc_JobDetails
        return data

    def getAccountTraitValue(self, keyName: str) -> str:
        """Get the specific trait by its key"""
        data = self.client.call('SoftLayer_Account', 'getAccountTraitValue', keyName)
        return data

    def getActiveOutletPackages(self) -> list['Product_Package']:
        """DEPRECATED. This method will return nothing."""
        data = self.client.call('SoftLayer_Account', 'getActiveOutletPackages')
        from SoftLayer.sltypes.Product_Package import Product_Package
        return data

    def getActivePackages(self) -> list['Product_Package']:
        """Retrieve the active [[SoftLayer_Product_Package]] objects from which you can order a server, service or
software."""
        data = self.client.call('SoftLayer_Account', 'getActivePackages')
        from SoftLayer.sltypes.Product_Package import Product_Package
        return data

    def getActivePackagesByAttribute(self, attributeKeyName: str) -> list['Product_Package']:
        """[<strong>DEPRECATED</strong>] Retrieve the active [[SoftLayer_Product_Package]] objects from which you can
order a server, service or software filtered by an attribute type
([[SoftLayer_Product_Package_Attribute_Type]]) on the package."""
        data = self.client.call('SoftLayer_Account', 'getActivePackagesByAttribute', attributeKeyName)
        from SoftLayer.sltypes.Product_Package import Product_Package
        return data

    def getActivePrivateHostedCloudPackages(self) -> list['Product_Package']:
        data = self.client.call('SoftLayer_Account', 'getActivePrivateHostedCloudPackages')
        from SoftLayer.sltypes.Product_Package import Product_Package
        return data

    def getAlternateCreditCardData(self) -> 'Container_Account_Payment_Method_CreditCard':
        data = self.client.call('SoftLayer_Account', 'getAlternateCreditCardData')
        from SoftLayer.sltypes.Container_Account_Payment_Method_CreditCard import Container_Account_Payment_Method_CreditCard
        return data

    def getAttributeByType(self, attributeType: str) -> 'Account_Attribute':
        """Retrieve an account attribute by type key name."""
        data = self.client.call('SoftLayer_Account', 'getAttributeByType', attributeType)
        from SoftLayer.sltypes.Account_Attribute import Account_Attribute
        return data

    def getAuxiliaryNotifications(self) -> list['Container_Utility_Message']:
        data = self.client.call('SoftLayer_Account', 'getAuxiliaryNotifications')
        from SoftLayer.sltypes.Container_Utility_Message import Container_Utility_Message
        return data

    def getAverageArchiveUsageMetricDataByDate(self, startDateTime: datetime, endDateTime: datetime) -> float:
        """Returns the average disk usage for all archive repositories for the timeframe based on the parameters
provided."""
        data = self.client.call('SoftLayer_Account', 'getAverageArchiveUsageMetricDataByDate', startDateTime, endDateTime)
        return data

    def getAveragePublicUsageMetricDataByDate(self, startDateTime: datetime, endDateTime: datetime) -> float:
        """Returns the average disk usage for all public repositories for the timeframe based on the parameters
provided."""
        data = self.client.call('SoftLayer_Account', 'getAveragePublicUsageMetricDataByDate', startDateTime, endDateTime)
        return data

    def getBandwidthList(self, networkType: str, direction: str, startDate: str, endDate: str, serverIds: int) -> list['Container_Bandwidth_Usage']:
        data = self.client.call('SoftLayer_Account', 'getBandwidthList', networkType, direction, startDate, endDate, serverIds)
        from SoftLayer.sltypes.Container_Bandwidth_Usage import Container_Bandwidth_Usage
        return data

    def getCurrentUser(self) -> 'User_Customer':
        """Retrieve the current API user's record."""
        data = self.client.call('SoftLayer_Account', 'getCurrentUser')
        from SoftLayer.sltypes.User_Customer import User_Customer
        return data

    def getDedicatedHostsForImageTemplate(self, imageTemplateId: int) -> list['Virtual_DedicatedHost']:
        """Get a collection of dedicated hosts that are valid for a given image template."""
        data = self.client.call('SoftLayer_Account', 'getDedicatedHostsForImageTemplate', imageTemplateId)
        from SoftLayer.sltypes.Virtual_DedicatedHost import Virtual_DedicatedHost
        return data

    def getFlexibleCreditProgramInfo(self, forNextBillCycle: bool) -> 'Container_Account_Discount_Program':
        """[DEPRECATED] Please use SoftLayer_Account::getFlexibleCreditProgramsInfo. This is no longer an accurate
representation of discounts."""
        data = self.client.call('SoftLayer_Account', 'getFlexibleCreditProgramInfo', forNextBillCycle)
        from SoftLayer.sltypes.Container_Account_Discount_Program import Container_Account_Discount_Program
        return data

    def getFlexibleCreditProgramsInfo(self, nextBillingCycleFlag: bool) -> 'Container_Account_Discount_Program_Collection':
        """This method retrieves information on all of your Flexible Credit Program enrollments for your account."""
        data = self.client.call('SoftLayer_Account', 'getFlexibleCreditProgramsInfo', nextBillingCycleFlag)
        from SoftLayer.sltypes.Container_Account_Discount_Program_Collection import Container_Account_Discount_Program_Collection
        return data

    def getHardwarePools(self) -> list['Container_Hardware_Pool_Details']:
        """Get a collection of managed hardware pools."""
        data = self.client.call('SoftLayer_Account', 'getHardwarePools')
        from SoftLayer.sltypes.Container_Hardware_Pool_Details import Container_Hardware_Pool_Details
        return data

    def getLargestAllowedSubnetCidr(self, numberOfHosts: int, locationId: int) -> int:
        """Computes the number of available public secondary IP addresses, augmented by the provided number of hosts,
before overflow of the allowed host to IP address ratio occurs. The result is aligned to the nearest subnet
size that could be accommodated in full.   0 is returned if an overflow is detected.   The use of $locationId
has been deprecated."""
        data = self.client.call('SoftLayer_Account', 'getLargestAllowedSubnetCidr', numberOfHosts, locationId)
        return data

    def getNetAppActiveAccountLicenseKeys(self) -> list[str]:
        """Get a collection of active NetApp software account license keys."""
        data = self.client.call('SoftLayer_Account', 'getNetAppActiveAccountLicenseKeys')
        return data

    def getNextInvoiceExcel(self, documentCreateDate: datetime) -> str:
        """Retrieve the next billing period's invoice. Note, this should be considered preliminary as you may add,
remove, change billing items on your account."""
        data = self.client.call('SoftLayer_Account', 'getNextInvoiceExcel', documentCreateDate)
        return data

    def getNextInvoicePdf(self, documentCreateDate: datetime) -> str:
        """Retrieve the next billing period's invoice. Note, this should be considered preliminary as you may add,
remove, change billing items on your account."""
        data = self.client.call('SoftLayer_Account', 'getNextInvoicePdf', documentCreateDate)
        return data

    def getNextInvoicePdfDetailed(self, documentCreateDate: datetime) -> str:
        """Retrieve the next billing period's detailed invoice. Note, this should be considered preliminary as you may
add, remove, change billing items on your account."""
        data = self.client.call('SoftLayer_Account', 'getNextInvoicePdfDetailed', documentCreateDate)
        return data

    def getNextInvoiceZeroFeeItemCounts(self) -> list['Container_Product_Item_Category_ZeroFee_Count']:
        data = self.client.call('SoftLayer_Account', 'getNextInvoiceZeroFeeItemCounts')
        from SoftLayer.sltypes.Container_Product_Item_Category_ZeroFee_Count import Container_Product_Item_Category_ZeroFee_Count
        return data

    def getObject(self) -> 'Account':
        """Retrieve a SoftLayer_Account record."""
        data = self.client.call('SoftLayer_Account', 'getObject')
        from SoftLayer.sltypes.Account import Account
        return data

    def getPendingCreditCardChangeRequestData(self) -> list['Container_Account_Payment_Method_CreditCard']:
        """Retrieve details of all credit card change requests which have not been processed by a SoftLayer agent."""
        data = self.client.call('SoftLayer_Account', 'getPendingCreditCardChangeRequestData')
        from SoftLayer.sltypes.Container_Account_Payment_Method_CreditCard import Container_Account_Payment_Method_CreditCard
        return data

    def getReferralPartnerCommissionForecast(self) -> list['Container_Referral_Partner_Commission']:
        data = self.client.call('SoftLayer_Account', 'getReferralPartnerCommissionForecast')
        from SoftLayer.sltypes.Container_Referral_Partner_Commission import Container_Referral_Partner_Commission
        return data

    def getReferralPartnerCommissionHistory(self) -> list['Container_Referral_Partner_Commission']:
        data = self.client.call('SoftLayer_Account', 'getReferralPartnerCommissionHistory')
        from SoftLayer.sltypes.Container_Referral_Partner_Commission import Container_Referral_Partner_Commission
        return data

    def getReferralPartnerCommissionPending(self) -> list['Container_Referral_Partner_Commission']:
        data = self.client.call('SoftLayer_Account', 'getReferralPartnerCommissionPending')
        from SoftLayer.sltypes.Container_Referral_Partner_Commission import Container_Referral_Partner_Commission
        return data

    def getSharedBlockDeviceTemplateGroups(self) -> list['Virtual_Guest_Block_Device_Template_Group']:
        """Get the collection of template group objects that have been shared with this account."""
        data = self.client.call('SoftLayer_Account', 'getSharedBlockDeviceTemplateGroups')
        from SoftLayer.sltypes.Virtual_Guest_Block_Device_Template_Group import Virtual_Guest_Block_Device_Template_Group
        return data

    def getTechIncubatorProgramInfo(self, forNextBillCycle: bool) -> 'Container_Account_Discount_Program':
        """This method retrieves the Technology Incubator Program information for your account."""
        data = self.client.call('SoftLayer_Account', 'getTechIncubatorProgramInfo', forNextBillCycle)
        from SoftLayer.sltypes.Container_Account_Discount_Program import Container_Account_Discount_Program
        return data

    def getThirdPartyPoliciesAcceptanceStatus(self) -> list['Container_Policy_Acceptance']:
        """Get the acceptance status of the applicable third-party policies."""
        data = self.client.call('SoftLayer_Account', 'getThirdPartyPoliciesAcceptanceStatus')
        from SoftLayer.sltypes.Container_Policy_Acceptance import Container_Policy_Acceptance
        return data

    def getValidSecurityCertificateEntries(self) -> list['Security_Certificate_Entry']:
        data = self.client.call('SoftLayer_Account', 'getValidSecurityCertificateEntries')
        from SoftLayer.sltypes.Security_Certificate_Entry import Security_Certificate_Entry
        return data

    def getVmWareActiveAccountLicenseKeys(self) -> list[str]:
        """Get a collection of active VMware software account license keys."""
        data = self.client.call('SoftLayer_Account', 'getVmWareActiveAccountLicenseKeys')
        return data

    def getWindowsUpdateStatus(self) -> list['Container_Utility_Microsoft_Windows_UpdateServices_Status']:
        """Retrieve a list of an account's hardware's Windows Update status."""
        data = self.client.call('SoftLayer_Account', 'getWindowsUpdateStatus')
        from SoftLayer.sltypes.Container_Utility_Microsoft_Windows_UpdateServices_Status import Container_Utility_Microsoft_Windows_UpdateServices_Status
        return data

    def hasAttribute(self, attributeType: str) -> bool:
        """Determine if an account has a given attribute."""
        data = self.client.call('SoftLayer_Account', 'hasAttribute', attributeType)
        return data

    def hourlyInstanceLimit(self) -> int:
        """Retrieve the number of hourly services that an account is allowed to have"""
        data = self.client.call('SoftLayer_Account', 'hourlyInstanceLimit')
        return data

    def hourlyServerLimit(self) -> int:
        """Retrieve the number of hourly bare metal servers that an account is allowed to have"""
        data = self.client.call('SoftLayer_Account', 'hourlyServerLimit')
        return data

    def initiatePayerAuthentication(self, setupInformation: 'Billing_Payment_Card_PayerAuthentication_Setup_Information') -> 'Billing_Payment_Card_PayerAuthentication_Setup':
        """Initiate Payer Authentication"""
        data = self.client.call('SoftLayer_Account', 'initiatePayerAuthentication', setupInformation)
        from SoftLayer.sltypes.Billing_Payment_Card_PayerAuthentication_Setup import Billing_Payment_Card_PayerAuthentication_Setup
        return data

    def isActiveVmwareCustomer(self) -> bool:
        """Determines if the account is considered an active VMware customer and as such eligible to order VMware
restricted products. This result is cached for up to 60 seconds."""
        data = self.client.call('SoftLayer_Account', 'isActiveVmwareCustomer')
        return data

    def isEligibleForLocalCurrencyProgram(self) -> bool:
        data = self.client.call('SoftLayer_Account', 'isEligibleForLocalCurrencyProgram')
        return data

    def isEligibleToLinkWithPaas(self) -> bool:
        """Returns true if this account is eligible to link with PaaS. False otherwise."""
        data = self.client.call('SoftLayer_Account', 'isEligibleToLinkWithPaas')
        return data

    def linkExternalAccount(self, externalAccountId: str, authorizationToken: str, externalServiceProviderKey: str) -> None:
        """This method will link this SoftLayer account with the provided external account."""
        data = self.client.call('SoftLayer_Account', 'linkExternalAccount', externalAccountId, authorizationToken, externalServiceProviderKey)
        return data

    def removeAlternateCreditCard(self) -> bool:
        data = self.client.call('SoftLayer_Account', 'removeAlternateCreditCard')
        return data

    def requestCreditCardChange(self, request: 'Billing_Payment_Card_ChangeRequest', vatId: str, paymentRoleName: str, onlyChangeNicknameFlag: bool) -> 'Billing_Payment_Card_ChangeRequest':
        """Retrieve the record data associated with the submission of a Credit Card Change Request."""
        data = self.client.call('SoftLayer_Account', 'requestCreditCardChange', request, vatId, paymentRoleName, onlyChangeNicknameFlag)
        from SoftLayer.sltypes.Billing_Payment_Card_ChangeRequest import Billing_Payment_Card_ChangeRequest
        return data

    def requestManualPayment(self, request: 'Billing_Payment_Card_ManualPayment') -> 'Billing_Payment_Card_ManualPayment':
        """Retrieve the record data associated with the submission of a Manual Payment Request."""
        data = self.client.call('SoftLayer_Account', 'requestManualPayment', request)
        from SoftLayer.sltypes.Billing_Payment_Card_ManualPayment import Billing_Payment_Card_ManualPayment
        return data

    def requestManualPaymentUsingCreditCardOnFile(self, amount: str, payWithAlternateCardFlag: bool, note: str) -> 'Billing_Payment_Card_ManualPayment':
        """Retrieve the record data associated with the submission of a Manual Payment Request which charges the manual
payment to a credit card already on file."""
        data = self.client.call('SoftLayer_Account', 'requestManualPaymentUsingCreditCardOnFile', amount, payWithAlternateCardFlag, note)
        from SoftLayer.sltypes.Billing_Payment_Card_ManualPayment import Billing_Payment_Card_ManualPayment
        return data

    def saveInternalCostRecovery(self, costRecoveryContainer: 'Container_Account_Internal_Ibm_CostRecovery') -> None:
        data = self.client.call('SoftLayer_Account', 'saveInternalCostRecovery', costRecoveryContainer)
        return data

    def setAbuseEmails(self, emails: str) -> bool:
        """Set this account's abuse emails."""
        data = self.client.call('SoftLayer_Account', 'setAbuseEmails', emails)
        return data

    def setManagedPoolQuantity(self, poolKeyName: str, backendRouter: str, quantity: int) -> int:
        """Set the number of desired servers in the pool"""
        data = self.client.call('SoftLayer_Account', 'setManagedPoolQuantity', poolKeyName, backendRouter, quantity)
        return data

    def setVlanSpan(self, enabled: bool) -> bool:
        """Set the flag that enables or disables automatic private network VLAN spanning for a SoftLayer customer
account."""
        data = self.client.call('SoftLayer_Account', 'setVlanSpan', enabled)
        return data

    def swapCreditCards(self) -> bool:
        data = self.client.call('SoftLayer_Account', 'swapCreditCards')
        return data

    def syncCurrentUserPopulationWithPaas(self) -> None:
        """This method manually starts a synchronize operation for the current IBMid-authenticated user population of a
linked account pair. "Manually" means "independent of an account link operation"."""
        data = self.client.call('SoftLayer_Account', 'syncCurrentUserPopulationWithPaas')
        return data

    def updateVpnUsersForResource(self, objectId: int, objectType: str) -> bool:
        """[DEPRECATED] Creates or updates a user VPN access privileges for a server on account."""
        data = self.client.call('SoftLayer_Account', 'updateVpnUsersForResource', objectId, objectType)
        return data

    def validate(self, account: 'Account') -> list[str]:
        """Validates SoftLayer account information. Will return an error if any field is not valid."""
        data = self.client.call('SoftLayer_Account', 'validate', account)
        return data

    def validateManualPaymentAmount(self, amount: str) -> bool:
        """Ensure the amount requested for a manual payment is valid."""
        data = self.client.call('SoftLayer_Account', 'validateManualPaymentAmount', amount)
        return data

    def getAbuseEmail(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Account', 'getAbuseEmail', id=identifier)
        return data

    def getAbuseEmails(self, identifier: int) -> list['Account_AbuseEmail']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getAbuseEmails', id=identifier)
        from SoftLayer.sltypes.Account_AbuseEmail import Account_AbuseEmail
        return data

    def getAccountContacts(self, identifier: int) -> list['Account_Contact']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getAccountContacts', id=identifier)
        from SoftLayer.sltypes.Account_Contact import Account_Contact
        return data

    def getAccountLicenses(self, identifier: int) -> list['Software_AccountLicense']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getAccountLicenses', id=identifier)
        from SoftLayer.sltypes.Software_AccountLicense import Software_AccountLicense
        return data

    def getAccountLinks(self, identifier: int) -> list['Account_Link']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getAccountLinks', id=identifier)
        from SoftLayer.sltypes.Account_Link import Account_Link
        return data

    def getAccountStatus(self, identifier: int) -> 'Account_Status':
        """"""
        data = self.client.call('SoftLayer_Account', 'getAccountStatus', id=identifier)
        from SoftLayer.sltypes.Account_Status import Account_Status
        return data

    def getActiveAccountDiscountBillingItem(self, identifier: int) -> 'Billing_Item':
        """"""
        data = self.client.call('SoftLayer_Account', 'getActiveAccountDiscountBillingItem', id=identifier)
        from SoftLayer.sltypes.Billing_Item import Billing_Item
        return data

    def getActiveAccountLicenses(self, identifier: int) -> list['Software_AccountLicense']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getActiveAccountLicenses', id=identifier)
        from SoftLayer.sltypes.Software_AccountLicense import Software_AccountLicense
        return data

    def getActiveAddresses(self, identifier: int) -> list['Account_Address']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getActiveAddresses', id=identifier)
        from SoftLayer.sltypes.Account_Address import Account_Address
        return data

    def getActiveAgreements(self, identifier: int) -> list['Account_Agreement']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getActiveAgreements', id=identifier)
        from SoftLayer.sltypes.Account_Agreement import Account_Agreement
        return data

    def getActiveBillingAgreements(self, identifier: int) -> list['Account_Agreement']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getActiveBillingAgreements', id=identifier)
        from SoftLayer.sltypes.Account_Agreement import Account_Agreement
        return data

    def getActiveCatalystEnrollment(self, identifier: int) -> 'Catalyst_Enrollment':
        """"""
        data = self.client.call('SoftLayer_Account', 'getActiveCatalystEnrollment', id=identifier)
        from SoftLayer.sltypes.Catalyst_Enrollment import Catalyst_Enrollment
        return data

    def getActiveColocationContainers(self, identifier: int) -> list['Billing_Item']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getActiveColocationContainers', id=identifier)
        from SoftLayer.sltypes.Billing_Item import Billing_Item
        return data

    def getActiveFlexibleCreditEnrollment(self, identifier: int) -> 'FlexibleCredit_Enrollment':
        """"""
        data = self.client.call('SoftLayer_Account', 'getActiveFlexibleCreditEnrollment', id=identifier)
        from SoftLayer.sltypes.FlexibleCredit_Enrollment import FlexibleCredit_Enrollment
        return data

    def getActiveFlexibleCreditEnrollments(self, identifier: int) -> list['FlexibleCredit_Enrollment']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getActiveFlexibleCreditEnrollments', id=identifier)
        from SoftLayer.sltypes.FlexibleCredit_Enrollment import FlexibleCredit_Enrollment
        return data

    def getActiveNotificationSubscribers(self, identifier: int) -> list['Notification_Subscriber']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getActiveNotificationSubscribers', id=identifier)
        from SoftLayer.sltypes.Notification_Subscriber import Notification_Subscriber
        return data

    def getActiveQuotes(self, identifier: int) -> list['Billing_Order_Quote']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getActiveQuotes', id=identifier)
        from SoftLayer.sltypes.Billing_Order_Quote import Billing_Order_Quote
        return data

    def getActiveReservedCapacityAgreements(self, identifier: int) -> list['Account_Agreement']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getActiveReservedCapacityAgreements', id=identifier)
        from SoftLayer.sltypes.Account_Agreement import Account_Agreement
        return data

    def getActiveVirtualLicenses(self, identifier: int) -> list['Software_VirtualLicense']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getActiveVirtualLicenses', id=identifier)
        from SoftLayer.sltypes.Software_VirtualLicense import Software_VirtualLicense
        return data

    def getAdcLoadBalancers(self, identifier: int) -> list['Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getAdcLoadBalancers', id=identifier)
        from SoftLayer.sltypes.Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress import Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress
        return data

    def getAddresses(self, identifier: int) -> list['Account_Address']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getAddresses', id=identifier)
        from SoftLayer.sltypes.Account_Address import Account_Address
        return data

    def getAffiliateId(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Account', 'getAffiliateId', id=identifier)
        return data

    def getAllBillingItems(self, identifier: int) -> list['Billing_Item']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getAllBillingItems', id=identifier)
        from SoftLayer.sltypes.Billing_Item import Billing_Item
        return data

    def getAllCommissionBillingItems(self, identifier: int) -> list['Billing_Item']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getAllCommissionBillingItems', id=identifier)
        from SoftLayer.sltypes.Billing_Item import Billing_Item
        return data

    def getAllRecurringTopLevelBillingItems(self, identifier: int) -> list['Billing_Item']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getAllRecurringTopLevelBillingItems', id=identifier)
        from SoftLayer.sltypes.Billing_Item import Billing_Item
        return data

    def getAllRecurringTopLevelBillingItemsUnfiltered(self, identifier: int) -> list['Billing_Item']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getAllRecurringTopLevelBillingItemsUnfiltered', id=identifier)
        from SoftLayer.sltypes.Billing_Item import Billing_Item
        return data

    def getAllSubnetBillingItems(self, identifier: int) -> list['Billing_Item']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getAllSubnetBillingItems', id=identifier)
        from SoftLayer.sltypes.Billing_Item import Billing_Item
        return data

    def getAllTopLevelBillingItems(self, identifier: int) -> list['Billing_Item']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getAllTopLevelBillingItems', id=identifier)
        from SoftLayer.sltypes.Billing_Item import Billing_Item
        return data

    def getAllTopLevelBillingItemsUnfiltered(self, identifier: int) -> list['Billing_Item']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getAllTopLevelBillingItemsUnfiltered', id=identifier)
        from SoftLayer.sltypes.Billing_Item import Billing_Item
        return data

    def getAllowIbmIdSilentMigrationFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Account', 'getAllowIbmIdSilentMigrationFlag', id=identifier)
        return data

    def getAllowsBluemixAccountLinkingFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Account', 'getAllowsBluemixAccountLinkingFlag', id=identifier)
        return data

    def getApplicationDeliveryControllers(self, identifier: int) -> list['Network_Application_Delivery_Controller']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getApplicationDeliveryControllers', id=identifier)
        from SoftLayer.sltypes.Network_Application_Delivery_Controller import Network_Application_Delivery_Controller
        return data

    def getAttributes(self, identifier: int) -> list['Account_Attribute']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getAttributes', id=identifier)
        from SoftLayer.sltypes.Account_Attribute import Account_Attribute
        return data

    def getAvailablePublicNetworkVlans(self, identifier: int) -> list['Network_Vlan']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getAvailablePublicNetworkVlans', id=identifier)
        from SoftLayer.sltypes.Network_Vlan import Network_Vlan
        return data

    def getBalance(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Account', 'getBalance', id=identifier)
        return data

    def getBandwidthAllotments(self, identifier: int) -> list['Network_Bandwidth_Version1_Allotment']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getBandwidthAllotments', id=identifier)
        from SoftLayer.sltypes.Network_Bandwidth_Version1_Allotment import Network_Bandwidth_Version1_Allotment
        return data

    def getBandwidthAllotmentsOverAllocation(self, identifier: int) -> list['Network_Bandwidth_Version1_Allotment']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getBandwidthAllotmentsOverAllocation', id=identifier)
        from SoftLayer.sltypes.Network_Bandwidth_Version1_Allotment import Network_Bandwidth_Version1_Allotment
        return data

    def getBandwidthAllotmentsProjectedOverAllocation(self, identifier: int) -> list['Network_Bandwidth_Version1_Allotment']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getBandwidthAllotmentsProjectedOverAllocation', id=identifier)
        from SoftLayer.sltypes.Network_Bandwidth_Version1_Allotment import Network_Bandwidth_Version1_Allotment
        return data

    def getBareMetalInstances(self, identifier: int) -> list['Hardware']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getBareMetalInstances', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getBillingAgreements(self, identifier: int) -> list['Account_Agreement']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getBillingAgreements', id=identifier)
        from SoftLayer.sltypes.Account_Agreement import Account_Agreement
        return data

    def getBillingInfo(self, identifier: int) -> 'Billing_Info':
        """"""
        data = self.client.call('SoftLayer_Account', 'getBillingInfo', id=identifier)
        from SoftLayer.sltypes.Billing_Info import Billing_Info
        return data

    def getBlockDeviceTemplateGroups(self, identifier: int) -> list['Virtual_Guest_Block_Device_Template_Group']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getBlockDeviceTemplateGroups', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest_Block_Device_Template_Group import Virtual_Guest_Block_Device_Template_Group
        return data

    def getBluemixAccountId(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Account', 'getBluemixAccountId', id=identifier)
        return data

    def getBluemixAccountLink(self, identifier: int) -> 'Account_Link_Bluemix':
        """"""
        data = self.client.call('SoftLayer_Account', 'getBluemixAccountLink', id=identifier)
        from SoftLayer.sltypes.Account_Link_Bluemix import Account_Link_Bluemix
        return data

    def getBluemixLinkedFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Account', 'getBluemixLinkedFlag', id=identifier)
        return data

    def getBrand(self, identifier: int) -> 'Brand':
        """"""
        data = self.client.call('SoftLayer_Account', 'getBrand', id=identifier)
        from SoftLayer.sltypes.Brand import Brand
        return data

    def getBrandAccountFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Account', 'getBrandAccountFlag', id=identifier)
        return data

    def getBrandKeyName(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Account', 'getBrandKeyName', id=identifier)
        return data

    def getBusinessPartner(self, identifier: int) -> 'Account_Business_Partner':
        """"""
        data = self.client.call('SoftLayer_Account', 'getBusinessPartner', id=identifier)
        from SoftLayer.sltypes.Account_Business_Partner import Account_Business_Partner
        return data

    def getCanOrderAdditionalVlansFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Account', 'getCanOrderAdditionalVlansFlag', id=identifier)
        return data

    def getCarts(self, identifier: int) -> list['Billing_Order_Quote']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getCarts', id=identifier)
        from SoftLayer.sltypes.Billing_Order_Quote import Billing_Order_Quote
        return data

    def getCatalystEnrollments(self, identifier: int) -> list['Catalyst_Enrollment']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getCatalystEnrollments', id=identifier)
        from SoftLayer.sltypes.Catalyst_Enrollment import Catalyst_Enrollment
        return data

    def getClosedTickets(self, identifier: int) -> list['Ticket']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getClosedTickets', id=identifier)
        from SoftLayer.sltypes.Ticket import Ticket
        return data

    def getDatacentersWithSubnetAllocations(self, identifier: int) -> list['Location']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getDatacentersWithSubnetAllocations', id=identifier)
        from SoftLayer.sltypes.Location import Location
        return data

    def getDedicatedHosts(self, identifier: int) -> list['Virtual_DedicatedHost']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getDedicatedHosts', id=identifier)
        from SoftLayer.sltypes.Virtual_DedicatedHost import Virtual_DedicatedHost
        return data

    def getDisablePaymentProcessingFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Account', 'getDisablePaymentProcessingFlag', id=identifier)
        return data

    def getDisplaySupportRepresentativeAssignments(self, identifier: int) -> list['Account_Attachment_Employee']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getDisplaySupportRepresentativeAssignments', id=identifier)
        from SoftLayer.sltypes.Account_Attachment_Employee import Account_Attachment_Employee
        return data

    def getDomainRegistrations(self, identifier: int) -> list['Dns_Domain_Registration']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getDomainRegistrations', id=identifier)
        from SoftLayer.sltypes.Dns_Domain_Registration import Dns_Domain_Registration
        return data

    def getDomains(self, identifier: int) -> list['Dns_Domain']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getDomains', id=identifier)
        from SoftLayer.sltypes.Dns_Domain import Dns_Domain
        return data

    def getDomainsWithoutSecondaryDnsRecords(self, identifier: int) -> list['Dns_Domain']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getDomainsWithoutSecondaryDnsRecords', id=identifier)
        from SoftLayer.sltypes.Dns_Domain import Dns_Domain
        return data

    def getEuSupportedFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Account', 'getEuSupportedFlag', id=identifier)
        return data

    def getEvaultCapacityGB(self, identifier: int) -> int:
        """"""
        data = self.client.call('SoftLayer_Account', 'getEvaultCapacityGB', id=identifier)
        return data

    def getEvaultMasterUsers(self, identifier: int) -> list['Account_Password']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getEvaultMasterUsers', id=identifier)
        from SoftLayer.sltypes.Account_Password import Account_Password
        return data

    def getEvaultNetworkStorage(self, identifier: int) -> list['Network_Storage']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getEvaultNetworkStorage', id=identifier)
        from SoftLayer.sltypes.Network_Storage import Network_Storage
        return data

    def getExpiredSecurityCertificates(self, identifier: int) -> list['Security_Certificate']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getExpiredSecurityCertificates', id=identifier)
        from SoftLayer.sltypes.Security_Certificate import Security_Certificate
        return data

    def getFacilityLogs(self, identifier: int) -> list['User_Access_Facility_Log']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getFacilityLogs', id=identifier)
        from SoftLayer.sltypes.User_Access_Facility_Log import User_Access_Facility_Log
        return data

    def getFileBlockBetaAccessFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Account', 'getFileBlockBetaAccessFlag', id=identifier)
        return data

    def getFlexibleCreditEnrollments(self, identifier: int) -> list['FlexibleCredit_Enrollment']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getFlexibleCreditEnrollments', id=identifier)
        from SoftLayer.sltypes.FlexibleCredit_Enrollment import FlexibleCredit_Enrollment
        return data

    def getForcePaasAccountLinkDate(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Account', 'getForcePaasAccountLinkDate', id=identifier)
        return data

    def getGlobalIpRecords(self, identifier: int) -> list['Network_Subnet_IpAddress_Global']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getGlobalIpRecords', id=identifier)
        from SoftLayer.sltypes.Network_Subnet_IpAddress_Global import Network_Subnet_IpAddress_Global
        return data

    def getGlobalIpv4Records(self, identifier: int) -> list['Network_Subnet_IpAddress_Global']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getGlobalIpv4Records', id=identifier)
        from SoftLayer.sltypes.Network_Subnet_IpAddress_Global import Network_Subnet_IpAddress_Global
        return data

    def getGlobalIpv6Records(self, identifier: int) -> list['Network_Subnet_IpAddress_Global']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getGlobalIpv6Records', id=identifier)
        from SoftLayer.sltypes.Network_Subnet_IpAddress_Global import Network_Subnet_IpAddress_Global
        return data

    def getGlobalLoadBalancerAccounts(self, identifier: int) -> list['Network_LoadBalancer_Global_Account']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getGlobalLoadBalancerAccounts', id=identifier)
        from SoftLayer.sltypes.Network_LoadBalancer_Global_Account import Network_LoadBalancer_Global_Account
        return data

    def getHardware(self, identifier: int) -> list['Hardware']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getHardware', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getHardwareOverBandwidthAllocation(self, identifier: int) -> list['Hardware']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getHardwareOverBandwidthAllocation', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getHardwareProjectedOverBandwidthAllocation(self, identifier: int) -> list['Hardware']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getHardwareProjectedOverBandwidthAllocation', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getHardwareWithCpanel(self, identifier: int) -> list['Hardware']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getHardwareWithCpanel', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getHardwareWithHelm(self, identifier: int) -> list['Hardware']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getHardwareWithHelm', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getHardwareWithMcafee(self, identifier: int) -> list['Hardware']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getHardwareWithMcafee', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getHardwareWithMcafeeAntivirusRedhat(self, identifier: int) -> list['Hardware']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getHardwareWithMcafeeAntivirusRedhat', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getHardwareWithMcafeeAntivirusWindows(self, identifier: int) -> list['Hardware']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getHardwareWithMcafeeAntivirusWindows', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getHardwareWithMcafeeIntrusionDetectionSystem(self, identifier: int) -> list['Hardware']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getHardwareWithMcafeeIntrusionDetectionSystem', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getHardwareWithPlesk(self, identifier: int) -> list['Hardware']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getHardwareWithPlesk', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getHardwareWithQuantastor(self, identifier: int) -> list['Hardware']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getHardwareWithQuantastor', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getHardwareWithUrchin(self, identifier: int) -> list['Hardware']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getHardwareWithUrchin', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getHardwareWithWindows(self, identifier: int) -> list['Hardware']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getHardwareWithWindows', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getHasEvaultBareMetalRestorePluginFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Account', 'getHasEvaultBareMetalRestorePluginFlag', id=identifier)
        return data

    def getHasIderaBareMetalRestorePluginFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Account', 'getHasIderaBareMetalRestorePluginFlag', id=identifier)
        return data

    def getHasPendingOrder(self, identifier: int) -> int:
        """"""
        data = self.client.call('SoftLayer_Account', 'getHasPendingOrder', id=identifier)
        return data

    def getHasR1softBareMetalRestorePluginFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Account', 'getHasR1softBareMetalRestorePluginFlag', id=identifier)
        return data

    def getHourlyBareMetalInstances(self, identifier: int) -> list['Hardware']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getHourlyBareMetalInstances', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getHourlyServiceBillingItems(self, identifier: int) -> list['Billing_Item']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getHourlyServiceBillingItems', id=identifier)
        from SoftLayer.sltypes.Billing_Item import Billing_Item
        return data

    def getHourlyVirtualGuests(self, identifier: int) -> list['Virtual_Guest']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getHourlyVirtualGuests', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest import Virtual_Guest
        return data

    def getHubNetworkStorage(self, identifier: int) -> list['Network_Storage']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getHubNetworkStorage', id=identifier)
        from SoftLayer.sltypes.Network_Storage import Network_Storage
        return data

    def getIbmCustomerNumber(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Account', 'getIbmCustomerNumber', id=identifier)
        return data

    def getIbmIdAuthenticationRequiredFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Account', 'getIbmIdAuthenticationRequiredFlag', id=identifier)
        return data

    def getIbmIdMigrationExpirationTimestamp(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Account', 'getIbmIdMigrationExpirationTimestamp', id=identifier)
        return data

    def getInProgressExternalAccountSetup(self, identifier: int) -> 'Account_External_Setup':
        """"""
        data = self.client.call('SoftLayer_Account', 'getInProgressExternalAccountSetup', id=identifier)
        from SoftLayer.sltypes.Account_External_Setup import Account_External_Setup
        return data

    def getInternalCciHostAccountFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Account', 'getInternalCciHostAccountFlag', id=identifier)
        return data

    def getInternalImageTemplateCreationFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Account', 'getInternalImageTemplateCreationFlag', id=identifier)
        return data

    def getInternalNotes(self, identifier: int) -> list['Account_Note']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getInternalNotes', id=identifier)
        from SoftLayer.sltypes.Account_Note import Account_Note
        return data

    def getInternalRestrictionFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Account', 'getInternalRestrictionFlag', id=identifier)
        return data

    def getInvoices(self, identifier: int) -> list['Billing_Invoice']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getInvoices', id=identifier)
        from SoftLayer.sltypes.Billing_Invoice import Billing_Invoice
        return data

    def getIpAddresses(self, identifier: int) -> list['Network_Subnet_IpAddress']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getIpAddresses', id=identifier)
        from SoftLayer.sltypes.Network_Subnet_IpAddress import Network_Subnet_IpAddress
        return data

    def getIscsiIsolationDisabled(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Account', 'getIscsiIsolationDisabled', id=identifier)
        return data

    def getIscsiNetworkStorage(self, identifier: int) -> list['Network_Storage']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getIscsiNetworkStorage', id=identifier)
        from SoftLayer.sltypes.Network_Storage import Network_Storage
        return data

    def getLastCanceledBillingItem(self, identifier: int) -> 'Billing_Item':
        """"""
        data = self.client.call('SoftLayer_Account', 'getLastCanceledBillingItem', id=identifier)
        from SoftLayer.sltypes.Billing_Item import Billing_Item
        return data

    def getLastCancelledServerBillingItem(self, identifier: int) -> 'Billing_Item':
        """"""
        data = self.client.call('SoftLayer_Account', 'getLastCancelledServerBillingItem', id=identifier)
        from SoftLayer.sltypes.Billing_Item import Billing_Item
        return data

    def getLastFiveClosedAbuseTickets(self, identifier: int) -> list['Ticket']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getLastFiveClosedAbuseTickets', id=identifier)
        from SoftLayer.sltypes.Ticket import Ticket
        return data

    def getLastFiveClosedAccountingTickets(self, identifier: int) -> list['Ticket']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getLastFiveClosedAccountingTickets', id=identifier)
        from SoftLayer.sltypes.Ticket import Ticket
        return data

    def getLastFiveClosedOtherTickets(self, identifier: int) -> list['Ticket']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getLastFiveClosedOtherTickets', id=identifier)
        from SoftLayer.sltypes.Ticket import Ticket
        return data

    def getLastFiveClosedSalesTickets(self, identifier: int) -> list['Ticket']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getLastFiveClosedSalesTickets', id=identifier)
        from SoftLayer.sltypes.Ticket import Ticket
        return data

    def getLastFiveClosedSupportTickets(self, identifier: int) -> list['Ticket']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getLastFiveClosedSupportTickets', id=identifier)
        from SoftLayer.sltypes.Ticket import Ticket
        return data

    def getLastFiveClosedTickets(self, identifier: int) -> list['Ticket']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getLastFiveClosedTickets', id=identifier)
        from SoftLayer.sltypes.Ticket import Ticket
        return data

    def getLatestBillDate(self, identifier: int) -> datetime:
        """"""
        data = self.client.call('SoftLayer_Account', 'getLatestBillDate', id=identifier)
        return data

    def getLatestRecurringInvoice(self, identifier: int) -> 'Billing_Invoice':
        """"""
        data = self.client.call('SoftLayer_Account', 'getLatestRecurringInvoice', id=identifier)
        from SoftLayer.sltypes.Billing_Invoice import Billing_Invoice
        return data

    def getLatestRecurringPendingInvoice(self, identifier: int) -> 'Billing_Invoice':
        """"""
        data = self.client.call('SoftLayer_Account', 'getLatestRecurringPendingInvoice', id=identifier)
        from SoftLayer.sltypes.Billing_Invoice import Billing_Invoice
        return data

    def getLegacyBandwidthAllotments(self, identifier: int) -> list['Network_Bandwidth_Version1_Allotment']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getLegacyBandwidthAllotments', id=identifier)
        from SoftLayer.sltypes.Network_Bandwidth_Version1_Allotment import Network_Bandwidth_Version1_Allotment
        return data

    def getLegacyIscsiCapacityGB(self, identifier: int) -> int:
        """"""
        data = self.client.call('SoftLayer_Account', 'getLegacyIscsiCapacityGB', id=identifier)
        return data

    def getLoadBalancers(self, identifier: int) -> list['Network_LoadBalancer_VirtualIpAddress']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getLoadBalancers', id=identifier)
        from SoftLayer.sltypes.Network_LoadBalancer_VirtualIpAddress import Network_LoadBalancer_VirtualIpAddress
        return data

    def getLockboxCapacityGB(self, identifier: int) -> int:
        """"""
        data = self.client.call('SoftLayer_Account', 'getLockboxCapacityGB', id=identifier)
        return data

    def getLockboxNetworkStorage(self, identifier: int) -> list['Network_Storage']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getLockboxNetworkStorage', id=identifier)
        from SoftLayer.sltypes.Network_Storage import Network_Storage
        return data

    def getManualPaymentsUnderReview(self, identifier: int) -> list['Billing_Payment_Card_ManualPayment']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getManualPaymentsUnderReview', id=identifier)
        from SoftLayer.sltypes.Billing_Payment_Card_ManualPayment import Billing_Payment_Card_ManualPayment
        return data

    def getMasterUser(self, identifier: int) -> 'User_Customer':
        """"""
        data = self.client.call('SoftLayer_Account', 'getMasterUser', id=identifier)
        from SoftLayer.sltypes.User_Customer import User_Customer
        return data

    def getMediaDataTransferRequests(self, identifier: int) -> list['Account_Media_Data_Transfer_Request']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getMediaDataTransferRequests', id=identifier)
        from SoftLayer.sltypes.Account_Media_Data_Transfer_Request import Account_Media_Data_Transfer_Request
        return data

    def getMetricTrackingObject(self, identifier: int) -> 'Metric_Tracking_Object':
        """"""
        data = self.client.call('SoftLayer_Account', 'getMetricTrackingObject', id=identifier)
        from SoftLayer.sltypes.Metric_Tracking_Object import Metric_Tracking_Object
        return data

    def getMigratedToIbmCloudPortalFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Account', 'getMigratedToIbmCloudPortalFlag', id=identifier)
        return data

    def getMonthlyBareMetalInstances(self, identifier: int) -> list['Hardware']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getMonthlyBareMetalInstances', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getMonthlyVirtualGuests(self, identifier: int) -> list['Virtual_Guest']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getMonthlyVirtualGuests', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest import Virtual_Guest
        return data

    def getNasNetworkStorage(self, identifier: int) -> list['Network_Storage']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getNasNetworkStorage', id=identifier)
        from SoftLayer.sltypes.Network_Storage import Network_Storage
        return data

    def getNetworkCreationFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Account', 'getNetworkCreationFlag', id=identifier)
        return data

    def getNetworkGateways(self, identifier: int) -> list['Network_Gateway']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getNetworkGateways', id=identifier)
        from SoftLayer.sltypes.Network_Gateway import Network_Gateway
        return data

    def getNetworkHardware(self, identifier: int) -> list['Hardware']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getNetworkHardware', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getNetworkMessageDeliveryAccounts(self, identifier: int) -> list['Network_Message_Delivery']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getNetworkMessageDeliveryAccounts', id=identifier)
        from SoftLayer.sltypes.Network_Message_Delivery import Network_Message_Delivery
        return data

    def getNetworkMonitorDownHardware(self, identifier: int) -> list['Hardware']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getNetworkMonitorDownHardware', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getNetworkMonitorDownVirtualGuests(self, identifier: int) -> list['Virtual_Guest']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getNetworkMonitorDownVirtualGuests', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest import Virtual_Guest
        return data

    def getNetworkMonitorRecoveringHardware(self, identifier: int) -> list['Hardware']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getNetworkMonitorRecoveringHardware', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getNetworkMonitorRecoveringVirtualGuests(self, identifier: int) -> list['Virtual_Guest']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getNetworkMonitorRecoveringVirtualGuests', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest import Virtual_Guest
        return data

    def getNetworkMonitorUpHardware(self, identifier: int) -> list['Hardware']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getNetworkMonitorUpHardware', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getNetworkMonitorUpVirtualGuests(self, identifier: int) -> list['Virtual_Guest']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getNetworkMonitorUpVirtualGuests', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest import Virtual_Guest
        return data

    def getNetworkStorage(self, identifier: int) -> list['Network_Storage']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getNetworkStorage', id=identifier)
        from SoftLayer.sltypes.Network_Storage import Network_Storage
        return data

    def getNetworkStorageGroups(self, identifier: int) -> list['Network_Storage_Group']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getNetworkStorageGroups', id=identifier)
        from SoftLayer.sltypes.Network_Storage_Group import Network_Storage_Group
        return data

    def getNetworkTunnelContexts(self, identifier: int) -> list['Network_Tunnel_Module_Context']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getNetworkTunnelContexts', id=identifier)
        from SoftLayer.sltypes.Network_Tunnel_Module_Context import Network_Tunnel_Module_Context
        return data

    def getNetworkVlanSpan(self, identifier: int) -> 'Account_Network_Vlan_Span':
        """"""
        data = self.client.call('SoftLayer_Account', 'getNetworkVlanSpan', id=identifier)
        from SoftLayer.sltypes.Account_Network_Vlan_Span import Account_Network_Vlan_Span
        return data

    def getNetworkVlans(self, identifier: int) -> list['Network_Vlan']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getNetworkVlans', id=identifier)
        from SoftLayer.sltypes.Network_Vlan import Network_Vlan
        return data

    def getNextBillingPublicAllotmentHardwareBandwidthDetails(self, identifier: int) -> list['Network_Bandwidth_Version1_Allotment']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getNextBillingPublicAllotmentHardwareBandwidthDetails', id=identifier)
        from SoftLayer.sltypes.Network_Bandwidth_Version1_Allotment import Network_Bandwidth_Version1_Allotment
        return data

    def getNextInvoiceIncubatorExemptTotal(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Account', 'getNextInvoiceIncubatorExemptTotal', id=identifier)
        return data

    def getNextInvoiceRecurringAmountEligibleForAccountDiscount(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Account', 'getNextInvoiceRecurringAmountEligibleForAccountDiscount', id=identifier)
        return data

    def getNextInvoiceTopLevelBillingItems(self, identifier: int) -> list['Billing_Item']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getNextInvoiceTopLevelBillingItems', id=identifier)
        from SoftLayer.sltypes.Billing_Item import Billing_Item
        return data

    def getNextInvoiceTotalAmount(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Account', 'getNextInvoiceTotalAmount', id=identifier)
        return data

    def getNextInvoiceTotalOneTimeAmount(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Account', 'getNextInvoiceTotalOneTimeAmount', id=identifier)
        return data

    def getNextInvoiceTotalOneTimeTaxAmount(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Account', 'getNextInvoiceTotalOneTimeTaxAmount', id=identifier)
        return data

    def getNextInvoiceTotalRecurringAmount(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Account', 'getNextInvoiceTotalRecurringAmount', id=identifier)
        return data

    def getNextInvoiceTotalRecurringAmountBeforeAccountDiscount(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Account', 'getNextInvoiceTotalRecurringAmountBeforeAccountDiscount', id=identifier)
        return data

    def getNextInvoiceTotalRecurringTaxAmount(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Account', 'getNextInvoiceTotalRecurringTaxAmount', id=identifier)
        return data

    def getNextInvoiceTotalTaxableRecurringAmount(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Account', 'getNextInvoiceTotalTaxableRecurringAmount', id=identifier)
        return data

    def getNotificationSubscribers(self, identifier: int) -> list['Notification_Subscriber']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getNotificationSubscribers', id=identifier)
        from SoftLayer.sltypes.Notification_Subscriber import Notification_Subscriber
        return data

    def getOpenAbuseTickets(self, identifier: int) -> list['Ticket']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getOpenAbuseTickets', id=identifier)
        from SoftLayer.sltypes.Ticket import Ticket
        return data

    def getOpenAccountingTickets(self, identifier: int) -> list['Ticket']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getOpenAccountingTickets', id=identifier)
        from SoftLayer.sltypes.Ticket import Ticket
        return data

    def getOpenBillingTickets(self, identifier: int) -> list['Ticket']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getOpenBillingTickets', id=identifier)
        from SoftLayer.sltypes.Ticket import Ticket
        return data

    def getOpenCancellationRequests(self, identifier: int) -> list['Billing_Item_Cancellation_Request']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getOpenCancellationRequests', id=identifier)
        from SoftLayer.sltypes.Billing_Item_Cancellation_Request import Billing_Item_Cancellation_Request
        return data

    def getOpenOtherTickets(self, identifier: int) -> list['Ticket']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getOpenOtherTickets', id=identifier)
        from SoftLayer.sltypes.Ticket import Ticket
        return data

    def getOpenRecurringInvoices(self, identifier: int) -> list['Billing_Invoice']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getOpenRecurringInvoices', id=identifier)
        from SoftLayer.sltypes.Billing_Invoice import Billing_Invoice
        return data

    def getOpenSalesTickets(self, identifier: int) -> list['Ticket']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getOpenSalesTickets', id=identifier)
        from SoftLayer.sltypes.Ticket import Ticket
        return data

    def getOpenStackAccountLinks(self, identifier: int) -> list['Account_Link']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getOpenStackAccountLinks', id=identifier)
        from SoftLayer.sltypes.Account_Link import Account_Link
        return data

    def getOpenStackObjectStorage(self, identifier: int) -> list['Network_Storage']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getOpenStackObjectStorage', id=identifier)
        from SoftLayer.sltypes.Network_Storage import Network_Storage
        return data

    def getOpenSupportTickets(self, identifier: int) -> list['Ticket']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getOpenSupportTickets', id=identifier)
        from SoftLayer.sltypes.Ticket import Ticket
        return data

    def getOpenTickets(self, identifier: int) -> list['Ticket']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getOpenTickets', id=identifier)
        from SoftLayer.sltypes.Ticket import Ticket
        return data

    def getOpenTicketsWaitingOnCustomer(self, identifier: int) -> list['Ticket']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getOpenTicketsWaitingOnCustomer', id=identifier)
        from SoftLayer.sltypes.Ticket import Ticket
        return data

    def getOrders(self, identifier: int) -> list['Billing_Order']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getOrders', id=identifier)
        from SoftLayer.sltypes.Billing_Order import Billing_Order
        return data

    def getOrphanBillingItems(self, identifier: int) -> list['Billing_Item']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getOrphanBillingItems', id=identifier)
        from SoftLayer.sltypes.Billing_Item import Billing_Item
        return data

    def getOwnedBrands(self, identifier: int) -> list['Brand']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getOwnedBrands', id=identifier)
        from SoftLayer.sltypes.Brand import Brand
        return data

    def getOwnedHardwareGenericComponentModels(self, identifier: int) -> list['Hardware_Component_Model_Generic']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getOwnedHardwareGenericComponentModels', id=identifier)
        from SoftLayer.sltypes.Hardware_Component_Model_Generic import Hardware_Component_Model_Generic
        return data

    def getPaymentProcessors(self, identifier: int) -> list['Billing_Payment_Processor']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getPaymentProcessors', id=identifier)
        from SoftLayer.sltypes.Billing_Payment_Processor import Billing_Payment_Processor
        return data

    def getPendingEvents(self, identifier: int) -> list['Notification_Occurrence_Event']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getPendingEvents', id=identifier)
        from SoftLayer.sltypes.Notification_Occurrence_Event import Notification_Occurrence_Event
        return data

    def getPendingInvoice(self, identifier: int) -> 'Billing_Invoice':
        """"""
        data = self.client.call('SoftLayer_Account', 'getPendingInvoice', id=identifier)
        from SoftLayer.sltypes.Billing_Invoice import Billing_Invoice
        return data

    def getPendingInvoiceTopLevelItems(self, identifier: int) -> list['Billing_Invoice_Item']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getPendingInvoiceTopLevelItems', id=identifier)
        from SoftLayer.sltypes.Billing_Invoice_Item import Billing_Invoice_Item
        return data

    def getPendingInvoiceTotalAmount(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Account', 'getPendingInvoiceTotalAmount', id=identifier)
        return data

    def getPendingInvoiceTotalOneTimeAmount(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Account', 'getPendingInvoiceTotalOneTimeAmount', id=identifier)
        return data

    def getPendingInvoiceTotalOneTimeTaxAmount(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Account', 'getPendingInvoiceTotalOneTimeTaxAmount', id=identifier)
        return data

    def getPendingInvoiceTotalRecurringAmount(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Account', 'getPendingInvoiceTotalRecurringAmount', id=identifier)
        return data

    def getPendingInvoiceTotalRecurringTaxAmount(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Account', 'getPendingInvoiceTotalRecurringTaxAmount', id=identifier)
        return data

    def getPermissionGroups(self, identifier: int) -> list['User_Permission_Group']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getPermissionGroups', id=identifier)
        from SoftLayer.sltypes.User_Permission_Group import User_Permission_Group
        return data

    def getPermissionRoles(self, identifier: int) -> list['User_Permission_Role']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getPermissionRoles', id=identifier)
        from SoftLayer.sltypes.User_Permission_Role import User_Permission_Role
        return data

    def getPlacementGroups(self, identifier: int) -> list['Virtual_PlacementGroup']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getPlacementGroups', id=identifier)
        from SoftLayer.sltypes.Virtual_PlacementGroup import Virtual_PlacementGroup
        return data

    def getPortableStorageVolumes(self, identifier: int) -> list['Virtual_Disk_Image']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getPortableStorageVolumes', id=identifier)
        from SoftLayer.sltypes.Virtual_Disk_Image import Virtual_Disk_Image
        return data

    def getPostProvisioningHooks(self, identifier: int) -> list['Provisioning_Hook']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getPostProvisioningHooks', id=identifier)
        from SoftLayer.sltypes.Provisioning_Hook import Provisioning_Hook
        return data

    def getPptpVpnAllowedFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Account', 'getPptpVpnAllowedFlag', id=identifier)
        return data

    def getPptpVpnUsers(self, identifier: int) -> list['User_Customer']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getPptpVpnUsers', id=identifier)
        from SoftLayer.sltypes.User_Customer import User_Customer
        return data

    def getPreviousRecurringRevenue(self, identifier: int) -> float:
        """"""
        data = self.client.call('SoftLayer_Account', 'getPreviousRecurringRevenue', id=identifier)
        return data

    def getPriceRestrictions(self, identifier: int) -> list['Product_Item_Price_Account_Restriction']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getPriceRestrictions', id=identifier)
        from SoftLayer.sltypes.Product_Item_Price_Account_Restriction import Product_Item_Price_Account_Restriction
        return data

    def getPriorityOneTickets(self, identifier: int) -> list['Ticket']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getPriorityOneTickets', id=identifier)
        from SoftLayer.sltypes.Ticket import Ticket
        return data

    def getPrivateAllotmentHardwareBandwidthDetails(self, identifier: int) -> list['Network_Bandwidth_Version1_Allotment']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getPrivateAllotmentHardwareBandwidthDetails', id=identifier)
        from SoftLayer.sltypes.Network_Bandwidth_Version1_Allotment import Network_Bandwidth_Version1_Allotment
        return data

    def getPrivateBlockDeviceTemplateGroups(self, identifier: int) -> list['Virtual_Guest_Block_Device_Template_Group']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getPrivateBlockDeviceTemplateGroups', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest_Block_Device_Template_Group import Virtual_Guest_Block_Device_Template_Group
        return data

    def getPrivateIpAddresses(self, identifier: int) -> list['Network_Subnet_IpAddress']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getPrivateIpAddresses', id=identifier)
        from SoftLayer.sltypes.Network_Subnet_IpAddress import Network_Subnet_IpAddress
        return data

    def getPrivateNetworkVlans(self, identifier: int) -> list['Network_Vlan']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getPrivateNetworkVlans', id=identifier)
        from SoftLayer.sltypes.Network_Vlan import Network_Vlan
        return data

    def getPrivateSubnets(self, identifier: int) -> list['Network_Subnet']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getPrivateSubnets', id=identifier)
        from SoftLayer.sltypes.Network_Subnet import Network_Subnet
        return data

    def getProofOfConceptAccountFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Account', 'getProofOfConceptAccountFlag', id=identifier)
        return data

    def getPublicAllotmentHardwareBandwidthDetails(self, identifier: int) -> list['Network_Bandwidth_Version1_Allotment']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getPublicAllotmentHardwareBandwidthDetails', id=identifier)
        from SoftLayer.sltypes.Network_Bandwidth_Version1_Allotment import Network_Bandwidth_Version1_Allotment
        return data

    def getPublicIpAddresses(self, identifier: int) -> list['Network_Subnet_IpAddress']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getPublicIpAddresses', id=identifier)
        from SoftLayer.sltypes.Network_Subnet_IpAddress import Network_Subnet_IpAddress
        return data

    def getPublicNetworkVlans(self, identifier: int) -> list['Network_Vlan']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getPublicNetworkVlans', id=identifier)
        from SoftLayer.sltypes.Network_Vlan import Network_Vlan
        return data

    def getPublicSubnets(self, identifier: int) -> list['Network_Subnet']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getPublicSubnets', id=identifier)
        from SoftLayer.sltypes.Network_Subnet import Network_Subnet
        return data

    def getQuotes(self, identifier: int) -> list['Billing_Order_Quote']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getQuotes', id=identifier)
        from SoftLayer.sltypes.Billing_Order_Quote import Billing_Order_Quote
        return data

    def getRecentEvents(self, identifier: int) -> list['Notification_Occurrence_Event']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getRecentEvents', id=identifier)
        from SoftLayer.sltypes.Notification_Occurrence_Event import Notification_Occurrence_Event
        return data

    def getReferralPartner(self, identifier: int) -> 'Account':
        """"""
        data = self.client.call('SoftLayer_Account', 'getReferralPartner', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getReferredAccountFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Account', 'getReferredAccountFlag', id=identifier)
        return data

    def getReferredAccounts(self, identifier: int) -> list['Account']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getReferredAccounts', id=identifier)
        from SoftLayer.sltypes.Account import Account
        return data

    def getRegulatedWorkloads(self, identifier: int) -> list['Legal_RegulatedWorkload']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getRegulatedWorkloads', id=identifier)
        from SoftLayer.sltypes.Legal_RegulatedWorkload import Legal_RegulatedWorkload
        return data

    def getRemoteManagementCommandRequests(self, identifier: int) -> list['Hardware_Component_RemoteManagement_Command_Request']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getRemoteManagementCommandRequests', id=identifier)
        from SoftLayer.sltypes.Hardware_Component_RemoteManagement_Command_Request import Hardware_Component_RemoteManagement_Command_Request
        return data

    def getReplicationEvents(self, identifier: int) -> list['Network_Storage_Event']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getReplicationEvents', id=identifier)
        from SoftLayer.sltypes.Network_Storage_Event import Network_Storage_Event
        return data

    def getRequireSilentIBMidUserCreation(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Account', 'getRequireSilentIBMidUserCreation', id=identifier)
        return data

    def getReservedCapacityAgreements(self, identifier: int) -> list['Account_Agreement']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getReservedCapacityAgreements', id=identifier)
        from SoftLayer.sltypes.Account_Agreement import Account_Agreement
        return data

    def getReservedCapacityGroups(self, identifier: int) -> list['Virtual_ReservedCapacityGroup']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getReservedCapacityGroups', id=identifier)
        from SoftLayer.sltypes.Virtual_ReservedCapacityGroup import Virtual_ReservedCapacityGroup
        return data

    def getRouters(self, identifier: int) -> list['Hardware']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getRouters', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getRwhoisData(self, identifier: int) -> list['Network_Subnet_Rwhois_Data']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getRwhoisData', id=identifier)
        from SoftLayer.sltypes.Network_Subnet_Rwhois_Data import Network_Subnet_Rwhois_Data
        return data

    def getSamlAuthentication(self, identifier: int) -> 'Account_Authentication_Saml':
        """"""
        data = self.client.call('SoftLayer_Account', 'getSamlAuthentication', id=identifier)
        from SoftLayer.sltypes.Account_Authentication_Saml import Account_Authentication_Saml
        return data

    def getSecondaryDomains(self, identifier: int) -> list['Dns_Secondary']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getSecondaryDomains', id=identifier)
        from SoftLayer.sltypes.Dns_Secondary import Dns_Secondary
        return data

    def getSecurityCertificates(self, identifier: int) -> list['Security_Certificate']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getSecurityCertificates', id=identifier)
        from SoftLayer.sltypes.Security_Certificate import Security_Certificate
        return data

    def getSecurityGroups(self, identifier: int) -> list['Network_SecurityGroup']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getSecurityGroups', id=identifier)
        from SoftLayer.sltypes.Network_SecurityGroup import Network_SecurityGroup
        return data

    def getSecurityLevel(self, identifier: int) -> 'Security_Level':
        """"""
        data = self.client.call('SoftLayer_Account', 'getSecurityLevel', id=identifier)
        from SoftLayer.sltypes.Security_Level import Security_Level
        return data

    def getSecurityScanRequests(self, identifier: int) -> list['Network_Security_Scanner_Request']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getSecurityScanRequests', id=identifier)
        from SoftLayer.sltypes.Network_Security_Scanner_Request import Network_Security_Scanner_Request
        return data

    def getServiceBillingItems(self, identifier: int) -> list['Billing_Item']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getServiceBillingItems', id=identifier)
        from SoftLayer.sltypes.Billing_Item import Billing_Item
        return data

    def getShipments(self, identifier: int) -> list['Account_Shipment']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getShipments', id=identifier)
        from SoftLayer.sltypes.Account_Shipment import Account_Shipment
        return data

    def getSshKeys(self, identifier: int) -> list['Security_Ssh_Key']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getSshKeys', id=identifier)
        from SoftLayer.sltypes.Security_Ssh_Key import Security_Ssh_Key
        return data

    def getSslVpnUsers(self, identifier: int) -> list['User_Customer']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getSslVpnUsers', id=identifier)
        from SoftLayer.sltypes.User_Customer import User_Customer
        return data

    def getStandardPoolVirtualGuests(self, identifier: int) -> list['Virtual_Guest']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getStandardPoolVirtualGuests', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest import Virtual_Guest
        return data

    def getSubnetRegistrationDetails(self, identifier: int) -> list['Account_Regional_Registry_Detail']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getSubnetRegistrationDetails', id=identifier)
        from SoftLayer.sltypes.Account_Regional_Registry_Detail import Account_Regional_Registry_Detail
        return data

    def getSubnetRegistrations(self, identifier: int) -> list['Network_Subnet_Registration']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getSubnetRegistrations', id=identifier)
        from SoftLayer.sltypes.Network_Subnet_Registration import Network_Subnet_Registration
        return data

    def getSubnets(self, identifier: int) -> list['Network_Subnet']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getSubnets', id=identifier)
        from SoftLayer.sltypes.Network_Subnet import Network_Subnet
        return data

    def getSupportRepresentatives(self, identifier: int) -> list['User_Employee']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getSupportRepresentatives', id=identifier)
        from SoftLayer.sltypes.User_Employee import User_Employee
        return data

    def getSupportSubscriptions(self, identifier: int) -> list['Billing_Item']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getSupportSubscriptions', id=identifier)
        from SoftLayer.sltypes.Billing_Item import Billing_Item
        return data

    def getSupportTier(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Account', 'getSupportTier', id=identifier)
        return data

    def getSuppressInvoicesFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Account', 'getSuppressInvoicesFlag', id=identifier)
        return data

    def getTags(self, identifier: int) -> list['Tag']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getTags', id=identifier)
        from SoftLayer.sltypes.Tag import Tag
        return data

    def getTestAccountAttributeFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Account', 'getTestAccountAttributeFlag', id=identifier)
        return data

    def getTickets(self, identifier: int) -> list['Ticket']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getTickets', id=identifier)
        from SoftLayer.sltypes.Ticket import Ticket
        return data

    def getTicketsClosedInTheLastThreeDays(self, identifier: int) -> list['Ticket']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getTicketsClosedInTheLastThreeDays', id=identifier)
        from SoftLayer.sltypes.Ticket import Ticket
        return data

    def getTicketsClosedToday(self, identifier: int) -> list['Ticket']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getTicketsClosedToday', id=identifier)
        from SoftLayer.sltypes.Ticket import Ticket
        return data

    def getTranscodeAccounts(self, identifier: int) -> list['Network_Media_Transcode_Account']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getTranscodeAccounts', id=identifier)
        from SoftLayer.sltypes.Network_Media_Transcode_Account import Network_Media_Transcode_Account
        return data

    def getUpgradeRequests(self, identifier: int) -> list['Product_Upgrade_Request']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getUpgradeRequests', id=identifier)
        from SoftLayer.sltypes.Product_Upgrade_Request import Product_Upgrade_Request
        return data

    def getUsers(self, identifier: int) -> list['User_Customer']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getUsers', id=identifier)
        from SoftLayer.sltypes.User_Customer import User_Customer
        return data

    def getValidSecurityCertificates(self, identifier: int) -> list['Security_Certificate']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getValidSecurityCertificates', id=identifier)
        from SoftLayer.sltypes.Security_Certificate import Security_Certificate
        return data

    def getVdrUpdatesInProgressFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Account', 'getVdrUpdatesInProgressFlag', id=identifier)
        return data

    def getVirtualDedicatedRacks(self, identifier: int) -> list['Network_Bandwidth_Version1_Allotment']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getVirtualDedicatedRacks', id=identifier)
        from SoftLayer.sltypes.Network_Bandwidth_Version1_Allotment import Network_Bandwidth_Version1_Allotment
        return data

    def getVirtualDiskImages(self, identifier: int) -> list['Virtual_Disk_Image']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getVirtualDiskImages', id=identifier)
        from SoftLayer.sltypes.Virtual_Disk_Image import Virtual_Disk_Image
        return data

    def getVirtualGuests(self, identifier: int) -> list['Virtual_Guest']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getVirtualGuests', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest import Virtual_Guest
        return data

    def getVirtualGuestsOverBandwidthAllocation(self, identifier: int) -> list['Virtual_Guest']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getVirtualGuestsOverBandwidthAllocation', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest import Virtual_Guest
        return data

    def getVirtualGuestsProjectedOverBandwidthAllocation(self, identifier: int) -> list['Virtual_Guest']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getVirtualGuestsProjectedOverBandwidthAllocation', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest import Virtual_Guest
        return data

    def getVirtualGuestsWithCpanel(self, identifier: int) -> list['Virtual_Guest']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getVirtualGuestsWithCpanel', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest import Virtual_Guest
        return data

    def getVirtualGuestsWithMcafee(self, identifier: int) -> list['Virtual_Guest']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getVirtualGuestsWithMcafee', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest import Virtual_Guest
        return data

    def getVirtualGuestsWithMcafeeAntivirusRedhat(self, identifier: int) -> list['Virtual_Guest']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getVirtualGuestsWithMcafeeAntivirusRedhat', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest import Virtual_Guest
        return data

    def getVirtualGuestsWithMcafeeAntivirusWindows(self, identifier: int) -> list['Virtual_Guest']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getVirtualGuestsWithMcafeeAntivirusWindows', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest import Virtual_Guest
        return data

    def getVirtualGuestsWithMcafeeIntrusionDetectionSystem(self, identifier: int) -> list['Virtual_Guest']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getVirtualGuestsWithMcafeeIntrusionDetectionSystem', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest import Virtual_Guest
        return data

    def getVirtualGuestsWithPlesk(self, identifier: int) -> list['Virtual_Guest']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getVirtualGuestsWithPlesk', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest import Virtual_Guest
        return data

    def getVirtualGuestsWithQuantastor(self, identifier: int) -> list['Virtual_Guest']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getVirtualGuestsWithQuantastor', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest import Virtual_Guest
        return data

    def getVirtualGuestsWithUrchin(self, identifier: int) -> list['Virtual_Guest']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getVirtualGuestsWithUrchin', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest import Virtual_Guest
        return data

    def getVirtualPrivateRack(self, identifier: int) -> 'Network_Bandwidth_Version1_Allotment':
        """"""
        data = self.client.call('SoftLayer_Account', 'getVirtualPrivateRack', id=identifier)
        from SoftLayer.sltypes.Network_Bandwidth_Version1_Allotment import Network_Bandwidth_Version1_Allotment
        return data

    def getVirtualStorageArchiveRepositories(self, identifier: int) -> list['Virtual_Storage_Repository']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getVirtualStorageArchiveRepositories', id=identifier)
        from SoftLayer.sltypes.Virtual_Storage_Repository import Virtual_Storage_Repository
        return data

    def getVirtualStoragePublicRepositories(self, identifier: int) -> list['Virtual_Storage_Repository']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getVirtualStoragePublicRepositories', id=identifier)
        from SoftLayer.sltypes.Virtual_Storage_Repository import Virtual_Storage_Repository
        return data

    def getVpcVirtualGuests(self, identifier: int) -> list['Virtual_Guest']:
        """"""
        data = self.client.call('SoftLayer_Account', 'getVpcVirtualGuests', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest import Virtual_Guest
        return data

    def getVpnConfigRequiresVPNManageFlag(self, identifier: int) -> bool:
        """"""
        data = self.client.call('SoftLayer_Account', 'getVpnConfigRequiresVPNManageFlag', id=identifier)
        return data
