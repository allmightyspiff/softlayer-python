from SoftLayer.sltypes.Entity import Entity

class Account_AbuseEmail(Entity):
    """An unfortunate facet of the hosting business is the necessity of with legal and network abuse inquiries. As
these types of inquiries frequently contain sensitive information SoftLayer keeps a separate account contact
email address for direct contact about legal and abuse matters, modeled by the SoftLayer_Account_AbuseEmail
data type. SoftLayer will typically email an account's abuse email addresses in these types of cases, and an
email is automatically sent to an account's abuse email addresses when a legal or abuse ticket is created or
updated."""
    email: str
