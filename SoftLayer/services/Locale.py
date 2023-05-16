# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Locale(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Locale'
        self.client = client

    def getClosestToLanguageTag(
        self,
        languageTag: str,
        objectMask: Optional[str] = None
    ) -> 'SoftLayer_Locale':

        data = self.client.call(
            self.service,
            'getClosestToLanguageTag',
            languageTag,
            mask=objectMask
        )
        from SoftLayer.datatypes.Locale import Locale
        return Locale(data)


    def getObject(
        self,
        objectMask: Optional[str] = None,
        objectFilter: Optional[dict] = None
    ) -> 'SoftLayer_Locale':

        data = self.client.call(
            self.service,
            'getObject',
            mask=objectMask,
            filter=objectFilter
        )
        from SoftLayer.datatypes.Locale import Locale
        return Locale(data)


