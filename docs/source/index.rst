.. pyReMa documentation master file, created by
   sphinx-quickstart on Mon Dec 11 19:45:16 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pyReMa's documentation!
==================================
pyReMa or Pylatex Report Manager is a library whose goal is to keep track of the latex objects as well as manage the parent child relationships. For example,
A Section its Subsections and even the Subsubsections are all managed and written to their own Tex files. It then will insert them in to the main report doc making
sure the paths are relative to the main doc.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Installation
============
pyReMa works on Python 3.10+ and it is simply installed using pip:

.. code-block:: console

   $ pip install pyrema



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
