# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Workload_Citrix_Deployment_Type(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Workload_Citrix_Deployment_Type'
        self.client = client

    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Workload_Citrix_Deployment_Type':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Workload.Citrix.Deployment.Type import Type
        return Type(data)


