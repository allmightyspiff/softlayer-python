from SoftLayer.sltypes.Entity import Entity

class Network_Monitor_Version1_Incident(Entity):
    """The SoftLayer_Network_Monitor_Version1_Incident data type models a single virtual server or physical hardware
network monitoring event. SoftLayer_Network_Monitor_Version1_Incidents are created when the SoftLayer
monitoring system detects a service down on your hardware of virtual server. As the incident is resolved it's
status changes from "SERVICE FAILURE" to "COMPLETED"."""
    status: str
