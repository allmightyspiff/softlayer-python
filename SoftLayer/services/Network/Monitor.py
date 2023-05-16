# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Network_Monitor(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Network_Monitor'
        self.client = client

    def getIpAddressesByHardware(
        self,
        hardware: SoftLayer_Hardware,
        partialIpAddress: str,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Subnet_IpAddress]':

        data = self.client.call(
            self.service,
            'getIpAddressesByHardware',
            hardware,
            partialIpAddress,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Subnet.IpAddress import IpAddress
        return IpAddress(data)


    def getIpAddressesByVirtualGuest(
        self,
        guest: SoftLayer_Virtual_Guest,
        partialIpAddress: str,
        limit: Optional[int] = None,
        offset: Optional[int] = None
    ) -> 'list[SoftLayer_Network_Subnet_IpAddress]':

        data = self.client.call(
            self.service,
            'getIpAddressesByVirtualGuest',
            guest,
            partialIpAddress,
            limit=limit,
            offset=offset
        )
        from SoftLayer.datatypes.Network.Subnet.IpAddress import IpAddress
        return IpAddress(data)


