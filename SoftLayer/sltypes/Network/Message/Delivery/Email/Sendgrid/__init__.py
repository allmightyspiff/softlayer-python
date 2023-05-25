from SoftLayer.sltypes.Network.Message.Delivery import Network_Message_Delivery
from SoftLayer.sltypes.Network_Message_Delivery import Network_Message_Delivery
from SoftLayer import BaseClient

class Network_Message_Delivery_Email_Sendgrid(Network_Message_Delivery):
    pass

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Message_Delivery_Email_Sendgrid'

    def addUnsubscribeEmailAddress(self, identifier: int, emailAddress: str) -> bool:
        data = self.client.call('SoftLayer_Network_Message_Delivery_Email_Sendgrid', 'addUnsubscribeEmailAddress', emailAddress, id=identifier)
        return data

    def deleteEmailListEntries(self, identifier: int, list_: str, entries: str) -> bool:
        data = self.client.call('SoftLayer_Network_Message_Delivery_Email_Sendgrid', 'deleteEmailListEntries', list, entries, id=identifier)
        return data

    def disableSmtpAccess(self, identifier: int, disable: bool) -> bool:
        data = self.client.call('SoftLayer_Network_Message_Delivery_Email_Sendgrid', 'disableSmtpAccess', disable, id=identifier)
        return data

    def enableSmtpAccess(self, identifier: int, enable: bool) -> bool:
        data = self.client.call('SoftLayer_Network_Message_Delivery_Email_Sendgrid', 'enableSmtpAccess', enable, id=identifier)
        return data

    def getAccountOverview(self, identifier: int) -> 'Container_Network_Message_Delivery_Email_Sendgrid_Account':
        data = self.client.call('SoftLayer_Network_Message_Delivery_Email_Sendgrid', 'getAccountOverview', id=identifier)
        from SoftLayer.sltypes.Container_Network_Message_Delivery_Email_Sendgrid_Account import Container_Network_Message_Delivery_Email_Sendgrid_Account
        return data

    def getEmailList(self, identifier: int, list_: str) -> list['Container_Network_Message_Delivery_Email_Sendgrid_List_Entry']:
        data = self.client.call('SoftLayer_Network_Message_Delivery_Email_Sendgrid', 'getEmailList', list, id=identifier)
        from SoftLayer.sltypes.Container_Network_Message_Delivery_Email_Sendgrid_List_Entry import Container_Network_Message_Delivery_Email_Sendgrid_List_Entry
        return data

    def getObject(self, identifier: int) -> 'Network_Message_Delivery_Email_Sendgrid':
        """Retrieve a SoftLayer_Network_Message_Delivery_Email_Sendgrid record."""
        data = self.client.call('SoftLayer_Network_Message_Delivery_Email_Sendgrid', 'getObject', id=identifier)
        return data

    def getOfferingsList(self, identifier: int) -> list['Container_Network_Message_Delivery_Email_Sendgrid_Catalog_Item']:
        data = self.client.call('SoftLayer_Network_Message_Delivery_Email_Sendgrid', 'getOfferingsList', id=identifier)
        from SoftLayer.sltypes.Container_Network_Message_Delivery_Email_Sendgrid_Catalog_Item import Container_Network_Message_Delivery_Email_Sendgrid_Catalog_Item
        return data

    def getStatistics(self, identifier: int, options: 'Container_Network_Message_Delivery_Email_Sendgrid_Statistics_Options') -> list['Container_Network_Message_Delivery_Email_Sendgrid_Statistics']:
        data = self.client.call('SoftLayer_Network_Message_Delivery_Email_Sendgrid', 'getStatistics', options, id=identifier)
        from SoftLayer.sltypes.Container_Network_Message_Delivery_Email_Sendgrid_Statistics import Container_Network_Message_Delivery_Email_Sendgrid_Statistics
        return data

    def getStatisticsGraph(self, identifier: int, options: 'Container_Network_Message_Delivery_Email_Sendgrid_Statistics_Options') -> 'Container_Network_Message_Delivery_Email_Sendgrid_Statistics_Graph':
        data = self.client.call('SoftLayer_Network_Message_Delivery_Email_Sendgrid', 'getStatisticsGraph', options, id=identifier)
        from SoftLayer.sltypes.Container_Network_Message_Delivery_Email_Sendgrid_Statistics_Graph import Container_Network_Message_Delivery_Email_Sendgrid_Statistics_Graph
        return data

    def singleSignOn(self, identifier: int) -> str:
        data = self.client.call('SoftLayer_Network_Message_Delivery_Email_Sendgrid', 'singleSignOn', id=identifier)
        return data

    def updateEmailAddress(self, identifier: int, emailAddress: str) -> bool:
        data = self.client.call('SoftLayer_Network_Message_Delivery_Email_Sendgrid', 'updateEmailAddress', emailAddress, id=identifier)
        return data

    def getEmailAddress(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Message_Delivery_Email_Sendgrid', 'getEmailAddress', id=identifier)
        return data

    def getSmtpAccess(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Network_Message_Delivery_Email_Sendgrid', 'getSmtpAccess', id=identifier)
        return data
