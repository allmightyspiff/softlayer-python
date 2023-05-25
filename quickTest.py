import SoftLayer
from SoftLayer.sltypes.Account import Account
# from SoftLayer.sltypes.Network.Vlan import Network_Vlan

client = SoftLayer.create_client_from_env()


sl_account = Account(client)
# print(dir(sl_account))

print("========= ACCOUNT ==========")
result = sl_account.getObject()
print(result)
# print("========= VLAN ==========")
# sl_vlan = SoftLayer_Network_Vlan(client)
# result = sl_vlan.getObject(identifier=1404267)
# print(result)