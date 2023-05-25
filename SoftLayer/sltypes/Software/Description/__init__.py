from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Software_Description(Entity):
    """This class holds a description for a specific installation of a Software Component.
SoftLayer_Software_Licenses tie a Software Component (A specific installation on a piece of hardware) to it's
description.   The "Manufacturer" and "Name" properties of a SoftLayer_Software_Description are used by the
framework to factory specific objects, objects that may have special methods for that specific piece of
software, or objects that contain application specific data, such as default ports.  For example, if you
create a SoftLayer_Software_Component who's SoftLayer_Software_License points to the
SoftLayer_Software_Description for "Swsoft" "Plesk", you'll actually get a
SoftLayer_Software_Component_Swsoft_Plesk object."""
    controlPanel: int
    id_: int
    licenseTermUnit: str
    licenseTermValue: int
    longDescription: str
    manufacturer: str
    name: str
    operatingSystem: int
    referenceCode: str
    upgradeSoftwareDescriptionId: int
    upgradeSwDescId: int
    version: str
    virtualLicense: int
    virtualizationPlatform: int

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Software_Description'

    def getAllObjects(self) -> list['Software_Description']:
        data = self.client.call('SoftLayer_Software_Description', 'getAllObjects')
        from SoftLayer.sltypes.Software_Description import Software_Description
        return data

    def getCustomerOwnedLicenseDescriptions(self) -> list['Software_Description']:
        data = self.client.call('SoftLayer_Software_Description', 'getCustomerOwnedLicenseDescriptions')
        from SoftLayer.sltypes.Software_Description import Software_Description
        return data

    def getObject(self, identifier: int) -> 'Software_Description':
        """Retrieve a SoftLayer_Software_Description record."""
        data = self.client.call('SoftLayer_Software_Description', 'getObject', id=identifier)
        from SoftLayer.sltypes.Software_Description import Software_Description
        return data

    def getAttributes(self, identifier: int) -> list['Software_Description_Attribute']:
        """"""
        data = self.client.call('SoftLayer_Software_Description', 'getAttributes', id=identifier)
        from SoftLayer.sltypes.Software_Description_Attribute import Software_Description_Attribute
        return data

    def getAverageInstallationDuration(self, identifier: int) -> int:
        """"""
        data = self.client.call('SoftLayer_Software_Description', 'getAverageInstallationDuration', id=identifier)
        return data

    def getCompatibleSoftwareDescriptions(self, identifier: int) -> list['Software_Description']:
        """"""
        data = self.client.call('SoftLayer_Software_Description', 'getCompatibleSoftwareDescriptions', id=identifier)
        from SoftLayer.sltypes.Software_Description import Software_Description
        return data

    def getFeatures(self, identifier: int) -> list['Software_Description_Feature']:
        """"""
        data = self.client.call('SoftLayer_Software_Description', 'getFeatures', id=identifier)
        from SoftLayer.sltypes.Software_Description_Feature import Software_Description_Feature
        return data

    def getLatestVersion(self, identifier: int) -> list['Software_Description']:
        """"""
        data = self.client.call('SoftLayer_Software_Description', 'getLatestVersion', id=identifier)
        from SoftLayer.sltypes.Software_Description import Software_Description
        return data

    def getProductItems(self, identifier: int) -> list['Product_Item']:
        """"""
        data = self.client.call('SoftLayer_Software_Description', 'getProductItems', id=identifier)
        from SoftLayer.sltypes.Product_Item import Product_Item
        return data

    def getProvisionTransactionGroup(self, identifier: int) -> 'Provisioning_Version1_Transaction_Group':
        """"""
        data = self.client.call('SoftLayer_Software_Description', 'getProvisionTransactionGroup', id=identifier)
        from SoftLayer.sltypes.Provisioning_Version1_Transaction_Group import Provisioning_Version1_Transaction_Group
        return data

    def getReloadTransactionGroup(self, identifier: int) -> 'Provisioning_Version1_Transaction_Group':
        """"""
        data = self.client.call('SoftLayer_Software_Description', 'getReloadTransactionGroup', id=identifier)
        from SoftLayer.sltypes.Provisioning_Version1_Transaction_Group import Provisioning_Version1_Transaction_Group
        return data

    def getRequiredUser(self, identifier: int) -> str:
        """"""
        data = self.client.call('SoftLayer_Software_Description', 'getRequiredUser', id=identifier)
        return data

    def getSoftwareLicenses(self, identifier: int) -> list['Software_License']:
        """"""
        data = self.client.call('SoftLayer_Software_Description', 'getSoftwareLicenses', id=identifier)
        from SoftLayer.sltypes.Software_License import Software_License
        return data

    def getUpgradeSoftwareDescription(self, identifier: int) -> 'Software_Description':
        """"""
        data = self.client.call('SoftLayer_Software_Description', 'getUpgradeSoftwareDescription', id=identifier)
        from SoftLayer.sltypes.Software_Description import Software_Description
        return data

    def getUpgradeSwDesc(self, identifier: int) -> 'Software_Description':
        """"""
        data = self.client.call('SoftLayer_Software_Description', 'getUpgradeSwDesc', id=identifier)
        from SoftLayer.sltypes.Software_Description import Software_Description
        return data

    def getValidFilesystemTypes(self, identifier: int) -> list['Configuration_Storage_Filesystem_Type']:
        """"""
        data = self.client.call('SoftLayer_Software_Description', 'getValidFilesystemTypes', id=identifier)
        from SoftLayer.sltypes.Configuration_Storage_Filesystem_Type import Configuration_Storage_Filesystem_Type
        return data
