from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Workload_Citrix_Workspace_Order(Entity):
    pass

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Workload_Citrix_Workspace_Order'

    def cancelWorkspaceResources(self, vlanIdentifier: str, cancelImmediately: bool, customerNote: str) -> 'Workload_Citrix_Workspace_Response_Result':
        """Cancel the orders associated with resources on the provided VLAN"""
        data = self.client.call('SoftLayer_Workload_Citrix_Workspace_Order', 'cancelWorkspaceResources', vlanIdentifier, cancelImmediately, customerNote)
        from SoftLayer.sltypes.Workload_Citrix_Workspace_Response_Result import Workload_Citrix_Workspace_Response_Result
        return data

    def getWorkspaceNames(self) -> 'Workload_Citrix_Workspace_Response_Result':
        """Get a list of all VLAN names which have 'cvad' tags associated with them."""
        data = self.client.call('SoftLayer_Workload_Citrix_Workspace_Order', 'getWorkspaceNames')
        from SoftLayer.sltypes.Workload_Citrix_Workspace_Response_Result import Workload_Citrix_Workspace_Response_Result
        return data

    def getWorkspaceResources(self, vlanIdentifier: str) -> 'Workload_Citrix_Workspace_Response_Result':
        """List the orders associated with resources on the provided VLAN"""
        data = self.client.call('SoftLayer_Workload_Citrix_Workspace_Order', 'getWorkspaceResources', vlanIdentifier)
        from SoftLayer.sltypes.Workload_Citrix_Workspace_Response_Result import Workload_Citrix_Workspace_Response_Result
        return data

    def placeWorkspaceOrder(self, orderContainer: 'Workload_Citrix_Workspace_Order_Container') -> 'Workload_Citrix_Workspace_Response':
        data = self.client.call('SoftLayer_Workload_Citrix_Workspace_Order', 'placeWorkspaceOrder', orderContainer)
        from SoftLayer.sltypes.Workload_Citrix_Workspace_Response import Workload_Citrix_Workspace_Response
        return data

    def verifyWorkspaceOrder(self, orderContainer: 'Workload_Citrix_Workspace_Order_Container') -> 'Workload_Citrix_Workspace_Response':
        """Verify that an order may be successfully placed with the details provided."""
        data = self.client.call('SoftLayer_Workload_Citrix_Workspace_Order', 'verifyWorkspaceOrder', orderContainer)
        from SoftLayer.sltypes.Workload_Citrix_Workspace_Response import Workload_Citrix_Workspace_Response
        return data
