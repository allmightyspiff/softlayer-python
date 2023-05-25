from SoftLayer.sltypes.McAfee.Epolicy.Orchestrator.Version51.Policy.Object import McAfee_Epolicy_Orchestrator_Version51_Policy_Object
from SoftLayer.sltypes.Software.Component.HostIps.Mcafee import Software_Component_HostIps_Mcafee
from SoftLayer.sltypes.Software_Component_HostIps_Mcafee import Software_Component_HostIps_Mcafee

class Software_Component_HostIps_Mcafee_Epo_Version51(Software_Component_HostIps_Mcafee):
    """The SoftLayer_Software_Component_HostIps_Mcafee_Epo_Version51 data type represents a single McAfee Secure
Host IPS software component that uses the ePO Server."""
    epoVersion: str
    firewallModePolicyNames: list[McAfee_Epolicy_Orchestrator_Version51_Policy_Object]
    firewallRuleSetPolicyNames: list[McAfee_Epolicy_Orchestrator_Version51_Policy_Object]
    ipsModePolicyNames: list[McAfee_Epolicy_Orchestrator_Version51_Policy_Object]
    ipsProtectionPolicyNames: list[McAfee_Epolicy_Orchestrator_Version51_Policy_Object]
    transactionStatus: str
