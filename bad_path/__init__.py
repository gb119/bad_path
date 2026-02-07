"""
bad_path: A Python package to identify potentially dangerous file paths.

This package provides functions to test whether a supplied file path points to a
system-sensitive location, taking into account different OS platforms.
"""

__version__ = "0.1.0"

from .checker import (
    is_dangerous_path,
    is_system_path,
    is_sensitive_path,
    get_dangerous_paths,
    DangerousPathError,
)

__all__ = [
    "is_dangerous_path",
    "is_system_path",
    "is_sensitive_path",
    "get_dangerous_paths",
    "DangerousPathError",
]
