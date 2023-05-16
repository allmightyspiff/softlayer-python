# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Workload_Citrix_Client(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Workload_Citrix_Client'
        self.client = client

    def createResourceLocation(
        self,
        citrixCredentials: SoftLayer_Workload_Citrix_Request
    ) -> 'SoftLayer_Workload_Citrix_Client_Response':

        data = self.client.call(
            self.service,
            'createResourceLocation',
            citrixCredentials
        )
        from SoftLayer.datatypes.Workload.Citrix.Client.Response import Response
        return Response(data)


    def getResourceLocations(
        self,
        citrixCredentials: SoftLayer_Workload_Citrix_Request
    ) -> 'SoftLayer_Workload_Citrix_Client_Response':

        data = self.client.call(
            self.service,
            'getResourceLocations',
            citrixCredentials
        )
        from SoftLayer.datatypes.Workload.Citrix.Client.Response import Response
        return Response(data)


    def validateCitrixCredentials(
        self,
        citrixCredentials: SoftLayer_Workload_Citrix_Request
    ) -> 'SoftLayer_Workload_Citrix_Client_Response':

        data = self.client.call(
            self.service,
            'validateCitrixCredentials',
            citrixCredentials
        )
        from SoftLayer.datatypes.Workload.Citrix.Client.Response import Response
        return Response(data)


