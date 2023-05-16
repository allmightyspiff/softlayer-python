# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Message_Delivery_Email_Sendgrid(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Message_Delivery_Email_Sendgrid'
        self.client = client

    def addUnsubscribeEmailAddress(
        self,
        emailAddress: str,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'addUnsubscribeEmailAddress',
            emailAddress,
            id=identifier
        )
        
        return data


    def deleteEmailListEntries(
        self,
        list: str,
        entries: str,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'deleteEmailListEntries',
            list,
            entries,
            id=identifier
        )
        
        return data


    def disableSmtpAccess(
        self,
        disable: bool,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'disableSmtpAccess',
            disable,
            id=identifier
        )
        
        return data


    def enableSmtpAccess(
        self,
        enable: bool,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'enableSmtpAccess',
            enable,
            id=identifier
        )
        
        return data


    def getAccountOverview(
        self,
        identifier: int
    ) -> 'SoftLayer_Container_Network_Message_Delivery_Email_Sendgrid_Account':

        data = self.client.call(
            self.service,
            'getAccountOverview',
            id=identifier
        )
        from SoftLayer.datatypes.Container.Network.Message.Delivery.Email.Sendgrid.Account import Account
        return Account(data)


    def getEmailList(
        self,
        list: str,
        identifier: int
    ) -> 'list[SoftLayer_Container_Network_Message_Delivery_Email_Sendgrid_List_Entry]':

        data = self.client.call(
            self.service,
            'getEmailList',
            list,
            id=identifier
        )
        from SoftLayer.datatypes.Container.Network.Message.Delivery.Email.Sendgrid.List.Entry import Entry
        return Entry(data)


    def getObject(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Message_Delivery_Email_Sendgrid':

        data = self.client.call(
            self.service,
            'getObject',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Message.Delivery.Email.Sendgrid import Sendgrid
        return Sendgrid(data)


    def getOfferingsList(
        self,
        identifier: int
    ) -> 'list[SoftLayer_Container_Network_Message_Delivery_Email_Sendgrid_Catalog_Item]':

        data = self.client.call(
            self.service,
            'getOfferingsList',
            id=identifier
        )
        from SoftLayer.datatypes.Container.Network.Message.Delivery.Email.Sendgrid.Catalog.Item import Item
        return Item(data)


    def getStatistics(
        self,
        options: 'SoftLayer_Container_Network_Message_Delivery_Email_Sendgrid_Statistics_Options',
        identifier: int
    ) -> 'list[SoftLayer_Container_Network_Message_Delivery_Email_Sendgrid_Statistics]':

        data = self.client.call(
            self.service,
            'getStatistics',
            options,
            id=identifier
        )
        from SoftLayer.datatypes.Container.Network.Message.Delivery.Email.Sendgrid.Statistics import Statistics
        return Statistics(data)


    def getStatisticsGraph(
        self,
        options: 'SoftLayer_Container_Network_Message_Delivery_Email_Sendgrid_Statistics_Options',
        identifier: int
    ) -> 'SoftLayer_Container_Network_Message_Delivery_Email_Sendgrid_Statistics_Graph':

        data = self.client.call(
            self.service,
            'getStatisticsGraph',
            options,
            id=identifier
        )
        from SoftLayer.datatypes.Container.Network.Message.Delivery.Email.Sendgrid.Statistics.Graph import Graph
        return Graph(data)


    def singleSignOn(
        self,
        identifier: int
    ) -> 'string':

        data = self.client.call(
            self.service,
            'singleSignOn',
            id=identifier
        )
        
        return data


    def updateEmailAddress(
        self,
        emailAddress: str,
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'updateEmailAddress',
            emailAddress,
            id=identifier
        )
        
        return data


    def editObject(
        self,
        templateObject: 'SoftLayer_Network_Message_Delivery',
        identifier: int
    ) -> 'boolean':

        data = self.client.call(
            self.service,
            'editObject',
            templateObject,
            id=identifier
        )
        
        return data


    def getUpgradeItemPrices(
        self,
        identifier: int,
        objectMask: Optional[str] = None
    ) -> 'list[SoftLayer_Product_Item_Price]':

        data = self.client.call(
            self.service,
            'getUpgradeItemPrices',
            id=identifier,
            mask=objectMask
        )
        from SoftLayer.datatypes.Product.Item.Price import Price
        return Price(data)


    def getEmailAddress(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getEmailAddress',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getSmtpAccess(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'string':

        data = self.client.call(
            self.service,
            'getSmtpAccess',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        
        return data


    def getAccount(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account':

        data = self.client.call(
            self.service,
            'getAccount',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account import Account
        return Account(data)


    def getBillingItem(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Billing_Item':

        data = self.client.call(
            self.service,
            'getBillingItem',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Billing.Item import Item
        return Item(data)


    def getType(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Message_Delivery_Type':

        data = self.client.call(
            self.service,
            'getType',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Message.Delivery.Type import Type
        return Type(data)


    def getVendor(
        self,
        identifier: int,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Network_Message_Delivery_Vendor':

        data = self.client.call(
            self.service,
            'getVendor',
            id=identifier,
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Network.Message.Delivery.Vendor import Vendor
        return Vendor(data)


