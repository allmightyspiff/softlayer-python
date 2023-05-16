# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Message_Delivery_Email_Sendgrid(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Message_Delivery_Email_Sendgrid'
        self.client = client

    def addUnsubscribeEmailAddress(
        self,
        emailAddress: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'addUnsubscribeEmailAddress',
            emailAddress
        )
        
        return data


    def deleteEmailListEntries(
        self,
        list: str,
        entries: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deleteEmailListEntries',
            list,
            entries
        )
        
        return data


    def disableSmtpAccess(
        self,
        disable: boolean
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'disableSmtpAccess',
            disable
        )
        
        return data


    def enableSmtpAccess(
        self,
        enable: boolean
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'enableSmtpAccess',
            enable
        )
        
        return data


    def getAccountOverview(
        self,
        
    ) -> 'SoftLayer_Container_Network_Message_Delivery_Email_Sendgrid_Account':

        data = self.client.call(
            self.service,
            'getAccountOverview',
            
        )
        from SoftLayer.datatypes.Container.Network.Message.Delivery.Email.Sendgrid.Account import Account
        return Account(data)


    def getEmailList(
        self,
        list: str
    ) -> 'list[SoftLayer_Container_Network_Message_Delivery_Email_Sendgrid_List_Entry]':

        data = self.client.call(
            self.service,
            'getEmailList',
            list
        )
        from SoftLayer.datatypes.Container.Network.Message.Delivery.Email.Sendgrid.List.Entry import Entry
        return Entry(data)


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Message_Delivery_Email_Sendgrid':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Message.Delivery.Email.Sendgrid import Sendgrid
        return Sendgrid(data)


    def getOfferingsList(
        self,
        
    ) -> 'list[SoftLayer_Container_Network_Message_Delivery_Email_Sendgrid_Catalog_Item]':

        data = self.client.call(
            self.service,
            'getOfferingsList',
            
        )
        from SoftLayer.datatypes.Container.Network.Message.Delivery.Email.Sendgrid.Catalog.Item import Item
        return Item(data)


    def getStatistics(
        self,
        options: SoftLayer_Container_Network_Message_Delivery_Email_Sendgrid_Statistics_Options
    ) -> 'list[SoftLayer_Container_Network_Message_Delivery_Email_Sendgrid_Statistics]':

        data = self.client.call(
            self.service,
            'getStatistics',
            options
        )
        from SoftLayer.datatypes.Container.Network.Message.Delivery.Email.Sendgrid.Statistics import Statistics
        return Statistics(data)


    def getStatisticsGraph(
        self,
        options: SoftLayer_Container_Network_Message_Delivery_Email_Sendgrid_Statistics_Options
    ) -> 'SoftLayer_Container_Network_Message_Delivery_Email_Sendgrid_Statistics_Graph':

        data = self.client.call(
            self.service,
            'getStatisticsGraph',
            options
        )
        from SoftLayer.datatypes.Container.Network.Message.Delivery.Email.Sendgrid.Statistics.Graph import Graph
        return Graph(data)


    def singleSignOn(
        self,
        
    ) -> 'string':

        data = self.client.call(
            self.service,
            'singleSignOn',
            
        )
        
        return data


    def updateEmailAddress(
        self,
        emailAddress: str
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'updateEmailAddress',
            emailAddress
        )
        
        return data


    def editObject(
        self,
        templateObject: SoftLayer_Network_Message_Delivery
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'editObject',
            templateObject
        )
        
        return data


    def getUpgradeItemPrices(
        self,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Product_Item_Price]':

        data = self.client.call(
            self.service,
            'getUpgradeItemPrices',
            mask=objectMask
        )
        from SoftLayer.datatypes.Product.Item.Price import Price
        return Price(data)


    def getEmailAddress(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getEmailAddress',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getSmtpAccess(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getSmtpAccess',
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getAccount(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account':

        data = self.client.call(
            self.service,
            'getAccount',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account import Account
        return Account(data)


    def getBillingItem(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Item':

        data = self.client.call(
            self.service,
            'getBillingItem',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Item import Item
        return Item(data)


    def getType(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Message_Delivery_Type':

        data = self.client.call(
            self.service,
            'getType',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Message.Delivery.Type import Type
        return Type(data)


    def getVendor(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Message_Delivery_Vendor':

        data = self.client.call(
            self.service,
            'getVendor',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Message.Delivery.Vendor import Vendor
        return Vendor(data)


