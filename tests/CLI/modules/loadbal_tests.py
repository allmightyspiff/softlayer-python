"""
    SoftLayer.tests.CLI.modules.loadbal_tests
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    :license: MIT, see LICENSE for more details.
"""

from SoftLayer import testing
from SoftLayer.CLI import exceptions
from SoftLayer.fixtures import SoftLayer_Product_Package


class LoadbalTests(testing.TestCase):

    def test_order(self):
        result = self.run_command(['loadbal', 'order', '--name', 'test', '--datacenter', 'par01', '--label',
                                   'labeltest', '--subnet', '759282'])

        self.assert_no_fail(result)

    def test_order_with_frontend(self):
        result = self.run_command(['loadbal', 'order', '--name', 'test', '--datacenter', 'par01', '--label',
                                   'labeltest', '--frontend', 'TCP:80', '--backend', 'TCP:80', '--subnet', '759282'])

        self.assert_no_fail(result)

    def test_order_with_backend(self):
        result = self.run_command(['loadbal', 'order', '--name', 'test', '--datacenter', 'par01', '--label',
                                   'labeltest', '--backend', 'HTTP:80', '--subnet', '759282'])

        self.assert_no_fail(result)

    def test_order_backend_fail(self):
        result = self.run_command(['loadbal', 'order', '--name', 'test', '--datacenter', 'par01', '--label',
                                   'labeltest', '--backend', 'HTTP', '--subnet', '759282'])

        self.assertEqual(result.exit_code, 2)
        self.assertIsInstance(result.exception, exceptions.ArgumentError)

    def test_verify_order(self):
        result = self.run_command(['loadbal', 'order', '--verify', '--name', 'test', '--datacenter', 'par01', '--label',
                                   'labeltest', '--subnet', '759282'])

        self.assert_no_fail(result)

    def test_order_options(self):
        mock = self.set_mock('SoftLayer_Product_Package', 'getAllObjects')
        mock.return_value = SoftLayer_Product_Package.getAllObjectsLoadbal
        result = self.run_command(['loadbal', 'order-options'])

        self.assert_no_fail(result)

    def test_order_options_with_datacenter(self):
        mock = self.set_mock('SoftLayer_Product_Package', 'getAllObjects')
        mock.return_value = SoftLayer_Product_Package.getAllObjectsLoadbal
        result = self.run_command(['loadbal', 'order-options', '--datacenter', 'ams03'])

        self.assert_no_fail(result)

    def test_cancel(self):
        result = self.run_command(['loadbal', 'cancel', '11111'])

        self.assert_no_fail(result)
        self.assert_called_with('SoftLayer_Network_LBaaS_LoadBalancer', 'cancelLoadBalancer')

    def test_ns_list(self):
        result = self.run_command(['loadbal', 'ns-list'])

        self.assert_no_fail(result)

    def test_ns_list_empty(self):
        mock = self.set_mock('SoftLayer_Account', 'getApplicationDeliveryControllers')
        mock.return_value = []

        result = self.run_command(['loadbal', 'ns-list'])

        self.assert_no_fail(result)

    def test_ns_detail(self):
        result = self.run_command(['loadbal', 'ns-detail', '11111'])

        self.assert_no_fail(result)
