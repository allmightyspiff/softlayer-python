.. _cli_loadbalancer:

LoadBalancers
===================================
These commands were added in version `5.8.0 <https://github.com/softlayer/softlayer-python/releases/tag/v5.8.0>`_

LBaaS Commands
~~~~~~~~~~~~~~

- `LBaaS Product <https://www.ibm.com/cloud/load-balancer>`_
- `LBaaS Documentation <https://cloud.ibm.com/docs/infrastructure/loadbalancer-service>`_

.. click:: SoftLayer.CLI.loadbal.detail:cli
   :prog: loadbal detail
   :show-nested:
.. click:: SoftLayer.CLI.loadbal.list:cli
   :prog: loadbal list
   :show-nested:
.. click:: SoftLayer.CLI.loadbal.health:cli
   :prog: loadbal health
   :show-nested:
.. click:: SoftLayer.CLI.loadbal.members:add
   :prog: loadbal member-add
   :show-nested:
.. click:: SoftLayer.CLI.loadbal.members:remove
   :prog: loadbal member-del
   :show-nested:
.. click:: SoftLayer.CLI.loadbal.pools:add
   :prog: loadbal pool-add
   :show-nested:
.. click:: SoftLayer.CLI.loadbal.pools:edit
   :prog: loadbal pool-edit
   :show-nested:
.. click:: SoftLayer.CLI.loadbal.pools:delete
   :prog: loadbal pool-del
   :show-nested:
.. click:: SoftLayer.CLI.loadbal.pools:l7pool_add
   :prog: loadbal l7pool-add
   :show-nested:
.. click:: SoftLayer.CLI.loadbal.pools:l7pool_del
   :prog: loadbal l7pool-del
   :show-nested:
.. click:: SoftLayer.CLI.loadbal.layer7_policy_list:policies
   :prog: loadbal l7policies
   :show-nested:
.. click:: SoftLayer.CLI.loadbal.order:order
   :prog: loadbal order
   :show-nested:
.. click:: SoftLayer.CLI.loadbal.order:order_options
   :prog: loadbal order-options
   :show-nested:
.. click:: SoftLayer.CLI.loadbal.order:cancel
   :prog: loadbal cancel
   :show-nested:
.. click:: SoftLayer.CLI.loadbal.protocol_add:cli
   :prog: loadbal protocol-add
   :show-nested:
.. click:: SoftLayer.CLI.loadbal.protocol_edit:cli
   :prog: loadbal protocol-edit
   :show-nested:
.. click:: SoftLayer.CLI.loadbal.protocol_delete:cli
   :prog: loadbal protocol-delete
   :show-nested:


NetScaler Commands
~~~~~~~~~~~~~~~~~~

.. click:: SoftLayer.CLI.loadbal.ns_detail:cli
   :prog: loadbal ns-detail
   :show-nested:
.. click:: SoftLayer.CLI.loadbal.ns_list:cli
   :prog: loadbal ns-list
   :show-nested: