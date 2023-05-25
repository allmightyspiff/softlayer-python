from SoftLayer.sltypes.Entity import Entity

class Hardware_Component_Motherboard_Reboot_Time(Entity):
    """The SoftLayer_Hardware_Component_Motherboard_Reboot_Time contains the average reboot times for motherboards.
There are two types of average times.  One is for motherboards without raid, and the other is for
motherboards with raid.  These times are based on averages and have been gathered through numerous test
cases."""
    withRaid: int
    withoutRaid: int
