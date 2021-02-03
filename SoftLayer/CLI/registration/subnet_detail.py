"""Get details for a subnet registration."""
# :license: MIT, see LICENSE for more details.

import click

from SoftLayer.CLI import environment
from SoftLayer.CLI import exceptions
from SoftLayer.CLI import formatting
from SoftLayer.managers.registration import RegistrationManager
from SoftLayer.managers.registration import ContactPerson
from SoftLayer.utils import clean_time

@click.command()
@click.argument('identifier')
@environment.pass_env
def cli(env, identifier):
    """Get details for a subnet registration."""

    env.registerClient = RegistrationManager(env.client)
    registration = env.registerClient.detail(identifier)

    if not registration:
        raise exceptions.CLIAbort('No Active Registration found for this Subnet')

    contact = ContactPerson(registration.get('personDetail'))
    table = formatting.KeyValueTable(['name', 'value'])
    table.align['name'] = 'r'
    table.align['value'] = 'l'
    table.add_row(['Id', registration['id']])
    table.add_row(['Created', clean_time(registration['createDate'])])
    table.add_row(['Label', contact.get('INTERNAL_LABEL')])
    table.add_row(['Name', str(contact)])
    table.add_row(['AccountId', registration['accountId']])
    table.add_row(['Email', contact.get('EMAIL_ADDRESS')])
    table.add_row(['Phone', contact.get('PHONE')])
    table.add_row(['Address', contact.get('ADDRESS')])
    table.add_row(['Subnet', "{}/{}".format(registration['networkIdentifier'],registration['cidr'])])
    table.add_row(['status', registration['status']['keyName']])
    env.fout(table)
