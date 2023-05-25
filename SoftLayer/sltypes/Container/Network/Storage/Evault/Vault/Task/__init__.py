from SoftLayer.sltypes.Entity import Entity

class Container_Network_Storage_Evault_Vault_Task(Entity):
    """SoftLayer's StorageLayer Evault services provides details regarding the the purchased vault.   When a job is
created using the Webcc Console, the job created is identified as a task on the vault. Using this service,
information regarding the task can be retrieved."""
    id_: int
    name: str
    usedPoolsize: int
