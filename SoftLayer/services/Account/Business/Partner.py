# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Account_Business_Partner(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Account_Business_Partner'
        self.client = client

    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Account_Business_Partner':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Account.Business.Partner import Partner
        return Partner(data)


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


    def getChannel(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Business_Partner_Channel':

        data = self.client.call(
            self.service,
            'getChannel',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Business.Partner.Channel import Channel
        return Channel(data)


    def getSegment(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Business_Partner_Segment':

        data = self.client.call(
            self.service,
            'getSegment',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Business.Partner.Segment import Segment
        return Segment(data)


