# figmasvg

Use inkscape to convert pdfs to svgs

## Getting started

```bash
figmasvg -- path/to/*.pdf
```

The above command will put svgs with the same name as the pdfs in the same directory. Under the hood, it uses `inkscape` to convert the pdfs to svgs.

`inkscape` can be installed via homebrew if you are on a mac.

## Installation

You need to have Python 3.8 or newer installed on your system. If you don't have
Python installed, we recommend installing [Mambaforge](https://github.com/conda-forge/miniforge#mambaforge).

There are several alternative options to install figmasvg:

<!--
1) Install the latest release of `figmasvg` from `PyPI <https://pypi.org/project/figmasvg/>`_:

```bash
pip install figmasvg
```
-->

1. Install the latest development version:

```bash
pip install git+https://github.com/adamgayoso/figmasvg.git@main
```
