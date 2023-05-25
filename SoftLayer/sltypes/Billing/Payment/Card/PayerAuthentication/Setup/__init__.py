from SoftLayer.sltypes.Entity import Entity

class Billing_Payment_Card_PayerAuthentication_Setup(Entity):
    """This datatype payer authentication setup"""
    accessToken: str
    deviceDataCollectionUrl: str
    referenceId: str
