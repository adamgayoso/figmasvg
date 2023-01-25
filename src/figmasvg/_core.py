import click
from reportlab.graphics import renderSVG
from svglib.svglib import svg2rlg


@click.command()
@click.argument("files", nargs=-1, type=click.Path())
def convert(files):
    """Simple program that converts pdfs to svgs using inkscape."""
    for filename in files:
        drawing = svg2rlg(filename)
        renderSVG.drawToFile(drawing, filename)
