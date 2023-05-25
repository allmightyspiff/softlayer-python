from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Workload_Citrix_Client(Entity):
    pass

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Workload_Citrix_Client'

    def createResourceLocation(self, citrixCredentials: 'Workload_Citrix_Request') -> 'Workload_Citrix_Client_Response':
        data = self.client.call('SoftLayer_Workload_Citrix_Client', 'createResourceLocation', citrixCredentials)
        from SoftLayer.sltypes.Workload_Citrix_Client_Response import Workload_Citrix_Client_Response
        return data

    def getResourceLocations(self, citrixCredentials: 'Workload_Citrix_Request') -> 'Workload_Citrix_Client_Response':
        data = self.client.call('SoftLayer_Workload_Citrix_Client', 'getResourceLocations', citrixCredentials)
        from SoftLayer.sltypes.Workload_Citrix_Client_Response import Workload_Citrix_Client_Response
        return data

    def validateCitrixCredentials(self, citrixCredentials: 'Workload_Citrix_Request') -> 'Workload_Citrix_Client_Response':
        data = self.client.call('SoftLayer_Workload_Citrix_Client', 'validateCitrixCredentials', citrixCredentials)
        from SoftLayer.sltypes.Workload_Citrix_Client_Response import Workload_Citrix_Client_Response
        return data
