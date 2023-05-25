from SoftLayer.sltypes.User.Security.Question import User_Security_Question
from SoftLayer.sltypes.Entity import Entity

class Container_User_Customer_PasswordSet(Entity):
    """Container for holding information necessary for the setting and resetting of customer passwords"""
    answeredSecurityQuestionId: int
    authenticationMethods: list[int]
    digitCountRequirement: int
    key: str
    lowercaseCountRequirement: int
    maximumPasswordLengthRequirement: int
    minimumPasswordLengthRequirement: int
    password: str
    securityAnswer: str
    securityQuestions: list[User_Security_Question]
    specialCharacterCountRequirement: int
    specialCharactersAllowed: str
    uppercaseCountRequirement: int
    userId: int
