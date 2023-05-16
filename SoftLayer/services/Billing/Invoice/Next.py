# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Billing_Invoice_Next(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Billing_Invoice_Next'
        self.client = client

    def getExcel(
        self,
        documentCreateDate: dateTime
    ) -> 'base64Binary':

        data = self.client.call(
            self.service,
            'getExcel',
            documentCreateDate
        )
        
        return data


    def getPdf(
        self,
        documentCreateDate: dateTime
    ) -> 'base64Binary':

        data = self.client.call(
            self.service,
            'getPdf',
            documentCreateDate
        )
        
        return data


    def getPdfDetailed(
        self,
        documentCreateDate: dateTime
    ) -> 'base64Binary':

        data = self.client.call(
            self.service,
            'getPdfDetailed',
            documentCreateDate
        )
        
        return data


