# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Hardware_Benchmark_Certification(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Hardware_Benchmark_Certification'
        self.client = client

    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Hardware_Benchmark_Certification':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Hardware.Benchmark.Certification import Certification
        return Certification(data)


    def getResultFile(
        self,
        
    ) -> 'base64Binary':

        data = self.client.call(
            self.service,
            'getResultFile',
            
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


    def getHardware(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Hardware':

        data = self.client.call(
            self.service,
            'getHardware',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Hardware import Hardware
        return Hardware(data)


