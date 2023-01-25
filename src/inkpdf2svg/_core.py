import os

import click


@click.command()
@click.argument("files", nargs=-1, type=click.Path())
def convert(files):
    """Simple program that converts pdfs to svgs using inkscape."""
    for filename in files:
        # Run the inkscape command
        os.system(f"inkscape {filename} -l --export-filename={filename[:-4]}.svg")
