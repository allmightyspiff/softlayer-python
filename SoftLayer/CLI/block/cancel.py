"""Cancel an existing iSCSI account."""
# :license: MIT, see LICENSE for more details.

import click

import SoftLayer
from SoftLayer.CLI import environment
from SoftLayer.CLI import exceptions
from SoftLayer.CLI import formatting
from SoftLayer.CLI import helpers


@click.command(cls=SoftLayer.CLI.command.SLCommand, )
@click.argument('volume-id')
@click.option('--reason', help="An optional reason for cancellation")
@click.option('--immediate', is_flag=True,
              help="Cancels the block storage volume immediately instead of on the billing anniversary")
@click.option('--force', default=False, is_flag=True, help="Force cancel block volume without confirmation")
@environment.pass_env
def cli(env, volume_id, reason, immediate, force):
    """Cancel an existing block storage volume.

    Example::
        slcli block volume-cancel 12345678 --immediate -f
        This command cancels volume with ID 12345678 immediately and without asking for confirmation.

        slcli block volume-cancel SL02SEL30111-77
        This command cancels volume with username SL02SEL30111-77 and ask for confirmation
"""

    manager = SoftLayer.BlockStorageManager(env.client)
    # Get the actual number for the ID incase the user put in the volume username
    block_volume_id = helpers.resolve_id(manager.resolve_ids, volume_id, 'File Storage')
    

    if not force:
        if not (env.skip_confirmations or
                formatting.confirm(f"This will cancel the block volume: {volume_id} and cannot be undone. Continue?")):
            raise exceptions.CLIAbort('Aborted')

    cancelled = manager.cancel_block_volume(12341111, reason, immediate)

    if cancelled:
        if immediate:
            click.echo(f'Volume with id {volume_id} has been marked for immediate cancellation')
        else:
            click.echo(f'Volume with id {volume_id} has been marked for cancellation')
    else:
        click.echo(f'Unable to cancel volume {volume_id}')
