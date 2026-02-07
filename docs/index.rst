bad_path Documentation
======================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   usage
   api

Overview
--------

``bad_path`` is a Python package to identify potentially dangerous file paths.
It provides functions to test whether a supplied file path points to a
system-sensitive location, taking into account different OS platforms.

Features
--------

* Cross-platform support (Windows, macOS, Linux)
* Simple API for checking dangerous paths
* Customizable error handling
* Lightweight with no external dependencies

Quick Start
-----------

Install the package:

.. code-block:: bash

   pip install bad_path

Use in your code:

.. code-block:: python

   from bad_path import is_dangerous_path

   # Check if a path is dangerous
   if is_dangerous_path("/etc/passwd"):
       print("Warning: This path points to a sensitive location!")

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
