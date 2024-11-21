import click

@click.group()
def cli():
    pass

@cli.command()
def version():
    from ._version import __version__
    click.echo(f"{__version__}")

def main() -> None:
    cli()
