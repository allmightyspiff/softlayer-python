from SoftLayer.sltypes.Entity import Entity

class Hardware_Component_RemoteManagement_User(Entity):
    """The credentials used for remote management such as username, password, etc..."""
    password: str
    username: str
