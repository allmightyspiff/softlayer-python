# This file was automatically generated with tools/generateTypes.py
from SoftLayer import Client
from typing import Optional

class SoftLayer_Account_Internal_Ibm_CostRecovery_Validator(object):

    def __init__(self, client: Client) -> None:
        self.service = 'SoftLayer_Account_Internal_Ibm_CostRecovery_Validator'
        self.client = client

    def getSprintContainer(
        self,
        accountId: str,
        countryId: str
    ) -> 'Sprint_Container_CostRecovery':

        data = self.client.call(
            self.service,
            'getSprintContainer',
            accountId,
            countryId
        )
        
        return data


    def validateByAccountAndCountryId(
        self,
        accountId: str,
        countryId: str
    ) -> 'Sprint_Container_CostRecovery':

        data = self.client.call(
            self.service,
            'validateByAccountAndCountryId',
            accountId,
            countryId
        )
        
        return data


