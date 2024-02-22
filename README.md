# figmasvg

Use inkscape to convert pdfs to svgs

## Getting started

```bash
figmasvg -- path/to/*.svg
```

The above command will overwrite the svgs with a new version that has been reformated to work well in Figma.

Matplotlib figures should be saved with `{"svg.fonttype": "none"}`, which can be done in a matplotlib context, or editing the rcParams.

````bash

## Installation

You need to have Python 3.9 or newer installed on your system. If you don't have
Python installed, we recommend installing [Mambaforge](https://github.com/conda-forge/miniforge#mambaforge).

There are several alternative options to install figmasvg:

<!--
1) Install the latest release of `figmasvg` from `PyPI <https://pypi.org/project/figmasvg/>`_:

```bash
pip install figmasvg
````

-->

1. Install the latest development version:

```bash
pip install git+https://github.com/adamgayoso/figmasvg.git@main
```
