# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Workload_Citrix_Workspace_Order(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Workload_Citrix_Workspace_Order'
        self.client = client
# This file was automatically generated with tools/generateTypes.py
    def cancelWorkspaceResources(
        self,
        vlanIdentifier: str,
        cancelImmediately: boolean,
        customerNote: str
    ) -> 'SoftLayer_Workload_Citrix_Workspace_Response_Result':
        data = self.client.call(
            self.service,
            'cancelWorkspaceResources',
            vlanIdentifier,
            cancelImmediately,
            customerNote
        )
        from SoftLayer.datatypes.Workload.Citrix.Workspace.Response.Result import Result
        return SL_Result(data)

# This file was automatically generated with tools/generateTypes.py
    def getWorkspaceNames(
        self,
        
    ) -> 'SoftLayer_Workload_Citrix_Workspace_Response_Result':
        data = self.client.call(
            self.service,
            'getWorkspaceNames',
            
        )
        from SoftLayer.datatypes.Workload.Citrix.Workspace.Response.Result import Result
        return SL_Result(data)

# This file was automatically generated with tools/generateTypes.py
    def getWorkspaceResources(
        self,
        vlanIdentifier: str
    ) -> 'SoftLayer_Workload_Citrix_Workspace_Response_Result':
        data = self.client.call(
            self.service,
            'getWorkspaceResources',
            vlanIdentifier
        )
        from SoftLayer.datatypes.Workload.Citrix.Workspace.Response.Result import Result
        return SL_Result(data)

# This file was automatically generated with tools/generateTypes.py
    def placeWorkspaceOrder(
        self,
        orderContainer: SoftLayer_Workload_Citrix_Workspace_Order_Container
    ) -> 'SoftLayer_Workload_Citrix_Workspace_Response':
        data = self.client.call(
            self.service,
            'placeWorkspaceOrder',
            orderContainer
        )
        from SoftLayer.datatypes.Workload.Citrix.Workspace.Response import Response
        return SL_Response(data)

# This file was automatically generated with tools/generateTypes.py
    def verifyWorkspaceOrder(
        self,
        orderContainer: SoftLayer_Workload_Citrix_Workspace_Order_Container
    ) -> 'SoftLayer_Workload_Citrix_Workspace_Response':
        data = self.client.call(
            self.service,
            'verifyWorkspaceOrder',
            orderContainer
        )
        from SoftLayer.datatypes.Workload.Citrix.Workspace.Response import Response
        return SL_Response(data)


