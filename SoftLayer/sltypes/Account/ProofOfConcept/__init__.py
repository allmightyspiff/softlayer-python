from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Account_ProofOfConcept(Entity):
    pass

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Account_ProofOfConcept'

    def approveReview(self, requestId: int, accessToken: str) -> None:
        """Allows a reviewer to approve a request"""
        data = self.client.call('SoftLayer_Account_ProofOfConcept', 'approveReview', requestId, accessToken)
        return data

    def denyReview(self, requestId: int, accessToken: str, reason: str) -> None:
        """Allows reviewer to deny a request"""
        data = self.client.call('SoftLayer_Account_ProofOfConcept', 'denyReview', requestId, accessToken, reason)
        return data

    def getAuthenticationUrl(self, targetPage: str) -> str:
        """Gets authentication URL"""
        data = self.client.call('SoftLayer_Account_ProofOfConcept', 'getAuthenticationUrl', targetPage)
        return data

    def getRequestsPendingIntegratedOfferingTeamReview(self, accessToken: str) -> list['Container_Account_ProofOfConcept_Review_Summary']:
        """Retrieves a list of requests pending IOT review in the specified regions"""
        data = self.client.call('SoftLayer_Account_ProofOfConcept', 'getRequestsPendingIntegratedOfferingTeamReview', accessToken)
        from SoftLayer.sltypes.Container_Account_ProofOfConcept_Review_Summary import Container_Account_ProofOfConcept_Review_Summary
        return data

    def getRequestsPendingOverThresholdReview(self, accessToken: str) -> list['Container_Account_ProofOfConcept_Review_Summary']:
        """Retrieves a list of requests pending over threshold review"""
        data = self.client.call('SoftLayer_Account_ProofOfConcept', 'getRequestsPendingOverThresholdReview', accessToken)
        from SoftLayer.sltypes.Container_Account_ProofOfConcept_Review_Summary import Container_Account_ProofOfConcept_Review_Summary
        return data

    def getReviewerAccessToken(self, unverifiedAuthenticationCode: str) -> str:
        """Exchanges a token"""
        data = self.client.call('SoftLayer_Account_ProofOfConcept', 'getReviewerAccessToken', unverifiedAuthenticationCode)
        return data

    def getReviewerEmailFromAccessToken(self, accessToken: str) -> str:
        """Fetches an email address using a token"""
        data = self.client.call('SoftLayer_Account_ProofOfConcept', 'getReviewerEmailFromAccessToken', accessToken)
        return data

    def getSubmittedRequest(self, requestId: int) -> 'Container_Account_ProofOfConcept_Review':
        """Retrieves full details of one PoC request submitted by an IBMer."""
        data = self.client.call('SoftLayer_Account_ProofOfConcept', 'getSubmittedRequest', requestId)
        from SoftLayer.sltypes.Container_Account_ProofOfConcept_Review import Container_Account_ProofOfConcept_Review
        return data

    def getSubmittedRequests(self, email: str, sortOrder: str) -> list['Container_Account_ProofOfConcept_Review_Summary']:
        """Retrieves a summary of proof of concept requests submitted by an IBMer."""
        data = self.client.call('SoftLayer_Account_ProofOfConcept', 'getSubmittedRequests', email, sortOrder)
        from SoftLayer.sltypes.Container_Account_ProofOfConcept_Review_Summary import Container_Account_ProofOfConcept_Review_Summary
        return data

    def getSupportEmailAddress(self) -> str:
        """Gets email address users can use to ask for help/support"""
        data = self.client.call('SoftLayer_Account_ProofOfConcept', 'getSupportEmailAddress')
        return data

    def getTotalRequestsPendingIntegratedOfferingTeamReview(self, accessToken: str) -> int:
        data = self.client.call('SoftLayer_Account_ProofOfConcept', 'getTotalRequestsPendingIntegratedOfferingTeamReview', accessToken)
        return data

    def getTotalRequestsPendingOverThresholdReviewCount(self) -> int:
        data = self.client.call('SoftLayer_Account_ProofOfConcept', 'getTotalRequestsPendingOverThresholdReviewCount')
        return data

    def isCurrentReviewer(self, requestId: int, accessToken: str) -> bool:
        """Determines if the user is one of the reviewers currently able to act"""
        data = self.client.call('SoftLayer_Account_ProofOfConcept', 'isCurrentReviewer', requestId, accessToken)
        return data

    def isIntegratedOfferingTeamReviewer(self, emailAddress: str) -> bool:
        """Retrieves Verifies a reviewer"""
        data = self.client.call('SoftLayer_Account_ProofOfConcept', 'isIntegratedOfferingTeamReviewer', emailAddress)
        return data

    def isOverThresholdReviewer(self, emailAddress: str) -> bool:
        """Verifies a reviewer"""
        data = self.client.call('SoftLayer_Account_ProofOfConcept', 'isOverThresholdReviewer', emailAddress)
        return data

    def requestAccountTeamFundedAccount(self, request: 'Container_Account_ProofOfConcept_Request_AccountFunded') -> 'Container_Account_ProofOfConcept_Review_Summary':
        """Accepts new proof of concept requests"""
        data = self.client.call('SoftLayer_Account_ProofOfConcept', 'requestAccountTeamFundedAccount', request)
        from SoftLayer.sltypes.Container_Account_ProofOfConcept_Review_Summary import Container_Account_ProofOfConcept_Review_Summary
        return data

    def requestGlobalFundedAccount(self, request: 'Container_Account_ProofOfConcept_Request_GlobalFunded') -> 'Container_Account_ProofOfConcept_Review_Summary':
        """Accepts new proof of concept requests"""
        data = self.client.call('SoftLayer_Account_ProofOfConcept', 'requestGlobalFundedAccount', request)
        from SoftLayer.sltypes.Container_Account_ProofOfConcept_Review_Summary import Container_Account_ProofOfConcept_Review_Summary
        return data

    def verifyReviewer(self, requestId: int, reviewerEmailAddress: str) -> None:
        """Validates a reviewer"""
        data = self.client.call('SoftLayer_Account_ProofOfConcept', 'verifyReviewer', requestId, reviewerEmailAddress)
        return data
