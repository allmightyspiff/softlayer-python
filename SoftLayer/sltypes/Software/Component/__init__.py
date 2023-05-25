from SoftLayer.sltypes.Entity import Entity
from SoftLayer import BaseClient

class Software_Component(Entity):
    """A SoftLayer_Software_Component ties the installation of a specific piece of software onto a specific piece of
hardware.   SoftLayer_Software_Component works with SoftLayer_Software_License and
SoftLayer_Software_Description to tie this all together.   <ul> <li>SoftLayer_Software_Component is the
installation of a specific piece of software onto a specific piece of hardware in accordance to a software
license. <ul> <li>SoftLayer_Software_License dictates when and how a specific piece of software may be
installed onto a piece of hardware. <ul> <li>SoftLayer_Software_Description describes a specific piece of
software which can be installed onto hardware in accordance with it's license agreement.
</li></ul></li></ul></li></ul>"""
    hardwareId: int
    id_: int
    manufacturerActivationCode: str
    manufacturerLicenseInstance: str

    def __init__(self, client: BaseClient):
        self.client = client
        self._name = 'SoftLayer_Software_Component'

    def getLicenseFile(self, identifier: int) -> str:
        """Get the license file for a software component if it is supported."""
        data = self.client.call('SoftLayer_Software_Component', 'getLicenseFile', id=identifier)
        return data

    def getObject(self, identifier: int) -> 'Software_Component':
        """Retrieve a SoftLayer_Software_Component record."""
        data = self.client.call('SoftLayer_Software_Component', 'getObject', id=identifier)
        return data

    def getVendorSetUpConfiguration(self, identifier: int) -> str:
        data = self.client.call('SoftLayer_Software_Component', 'getVendorSetUpConfiguration', id=identifier)
        return data

    def getAverageInstallationDuration(self, identifier: int) -> int:
        """"""
        data = self.client.call('SoftLayer_Software_Component', 'getAverageInstallationDuration', id=identifier)
        return data

    def getBillingItem(self, identifier: int) -> 'Billing_Item':
        """"""
        data = self.client.call('SoftLayer_Software_Component', 'getBillingItem', id=identifier)
        from SoftLayer.sltypes.Billing_Item import Billing_Item
        return data

    def getHardware(self, identifier: int) -> 'Hardware':
        """"""
        data = self.client.call('SoftLayer_Software_Component', 'getHardware', id=identifier)
        from SoftLayer.sltypes.Hardware import Hardware
        return data

    def getPasswordHistory(self, identifier: int) -> list['Software_Component_Password_History']:
        """"""
        data = self.client.call('SoftLayer_Software_Component', 'getPasswordHistory', id=identifier)
        from SoftLayer.sltypes.Software_Component_Password_History import Software_Component_Password_History
        return data

    def getPasswords(self, identifier: int) -> list['Software_Component_Password']:
        """"""
        data = self.client.call('SoftLayer_Software_Component', 'getPasswords', id=identifier)
        from SoftLayer.sltypes.Software_Component_Password import Software_Component_Password
        return data

    def getSoftwareDescription(self, identifier: int) -> 'Software_Description':
        """"""
        data = self.client.call('SoftLayer_Software_Component', 'getSoftwareDescription', id=identifier)
        from SoftLayer.sltypes.Software_Description import Software_Description
        return data

    def getSoftwareLicense(self, identifier: int) -> 'Software_License':
        """"""
        data = self.client.call('SoftLayer_Software_Component', 'getSoftwareLicense', id=identifier)
        from SoftLayer.sltypes.Software_License import Software_License
        return data

    def getVirtualGuest(self, identifier: int) -> 'Virtual_Guest':
        """"""
        data = self.client.call('SoftLayer_Software_Component', 'getVirtualGuest', id=identifier)
        from SoftLayer.sltypes.Virtual_Guest import Virtual_Guest
        return data
