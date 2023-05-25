from datetime import datetime
from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Network_Application_Delivery_Controller_Configuration_History(Entity):
    """The SoftLayer_Network_Application_Delivery_Controller_Configuration_History data type models a single
instance of a configuration history entry for an application delivery controller. The configuration history
entries are used to support creating backups of an application delivery controller's configuration state in
order to restore them later if needed."""
    createDate: datetime
    id_: int
    notes: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Network_Application_Delivery_Controller_Configuration_History'

    def deleteObject(self, identifier: int) -> bool:
        """Remove a configuration history record."""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_Configuration_History', 'deleteObject', id=identifier)
        return data

    def getObject(self, identifier: int) -> 'Network_Application_Delivery_Controller_Configuration_History':
        """Retrieve a SoftLayer_Network_Application_Delivery_Controller_Configuration_History record."""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_Configuration_History', 'getObject', id=identifier)
        return data

    def getController(self, identifier: int) -> 'Network_Application_Delivery_Controller':
        """"""
        data = self.client.call('SoftLayer_Network_Application_Delivery_Controller_Configuration_History', 'getController', id=identifier)
        from SoftLayer.sltypes.Network_Application_Delivery_Controller import Network_Application_Delivery_Controller
        return data
