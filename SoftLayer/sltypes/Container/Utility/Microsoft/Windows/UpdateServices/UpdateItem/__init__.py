from SoftLayer.sltypes.Entity import Entity

class Container_Utility_Microsoft_Windows_UpdateServices_UpdateItem(Entity):
    """SoftLayer_Container_Utility_Microsoft_Windows_UpdateServices_UpdateItem models a single Microsoft Update as
reported by SoftLayer's private Windows Server Update Services (WSUS) services. All servers purchased with
Microsoft Windows retrieve updates from SoftLayer's WSUS servers by default."""
    description: str
    failed: bool
    kbArticleNumber: int
    optional: bool
    requiresReboot: bool
