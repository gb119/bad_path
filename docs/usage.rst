Usage Guide
===========

Basic Usage
-----------

The ``bad_path`` package provides several functions for checking if a file path
points to a system-sensitive location.

Checking for Dangerous Paths
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The simplest way to check if a path is dangerous:

.. code-block:: python

   from bad_path import is_dangerous_path

   # Returns True if the path is dangerous, False otherwise
   if is_dangerous_path("/etc/passwd"):
       print("This is a dangerous path!")

Raising Exceptions
~~~~~~~~~~~~~~~~~~

You can also have the function raise an exception instead of returning a boolean:

.. code-block:: python

   from bad_path import is_dangerous_path, DangerousPathError

   try:
       is_dangerous_path("/etc/passwd", raise_error=True)
   except DangerousPathError as e:
       print(f"Error: {e}")

Using Path Objects
~~~~~~~~~~~~~~~~~~

The package works with both strings and ``pathlib.Path`` objects:

.. code-block:: python

   from pathlib import Path
   from bad_path import is_dangerous_path

   path = Path("/etc/passwd")
   if is_dangerous_path(path):
       print("Dangerous!")

Getting Dangerous Paths for Current OS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To see which paths are considered dangerous on the current platform:

.. code-block:: python

   from bad_path import get_dangerous_paths

   dangerous = get_dangerous_paths()
   for path in dangerous:
       print(f"Dangerous path: {path}")

Platform-Specific Behavior
---------------------------

The package automatically detects the current operating system and uses
appropriate dangerous path lists:

* **Windows**: System directories like ``C:\\Windows``, ``C:\\Program Files``
* **macOS**: System directories like ``/System``, ``/Library``
* **Linux**: System directories like ``/etc``, ``/bin``, ``/usr``

Examples
--------

Validating User Input
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from bad_path import is_dangerous_path, DangerousPathError

   def save_file(filepath, content):
       """Save content to a file, but only if it's not in a dangerous location."""
       try:
           is_dangerous_path(filepath, raise_error=True)
       except DangerousPathError:
           raise ValueError("Cannot write to system directories!")
       
       with open(filepath, 'w') as f:
           f.write(content)

Filtering File Lists
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from bad_path import is_system_path
   import os

   def get_safe_files(directory):
       """Get all files in a directory that are not in system locations."""
       safe_files = []
       for root, dirs, files in os.walk(directory):
           for file in files:
               filepath = os.path.join(root, file)
               if not is_system_path(filepath):
                   safe_files.append(filepath)
       return safe_files
