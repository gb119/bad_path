"""
Tests for the bad_path package.
"""

import os
import platform
import pytest
from pathlib import Path

from bad_path import (
    is_dangerous_path,
    is_system_path,
    is_sensitive_path,
    get_dangerous_paths,
    DangerousPathError,
)


class TestGetDangerousPaths:
    """Tests for get_dangerous_paths function."""

    def test_returns_list(self):
        """Test that get_dangerous_paths returns a list."""
        paths = get_dangerous_paths()
        assert isinstance(paths, list)
        assert len(paths) > 0

    def test_returns_strings(self):
        """Test that all returned paths are strings."""
        paths = get_dangerous_paths()
        assert all(isinstance(p, str) for p in paths)

    def test_platform_specific_paths(self):
        """Test that paths are appropriate for the current platform."""
        paths = get_dangerous_paths()
        system = platform.system()

        if system == "Windows":
            assert any("Windows" in p for p in paths)
        elif system == "Darwin":
            assert any("/System" in p or "/Library" in p for p in paths)
        else:  # Linux
            assert any("/etc" in p or "/bin" in p for p in paths)


class TestIsSystemPath:
    """Tests for is_system_path function."""

    def test_with_string_path(self):
        """Test with a string path."""
        result = is_system_path("/tmp/test.txt")
        assert isinstance(result, bool)

    def test_with_path_object(self):
        """Test with a Path object."""
        result = is_system_path(Path("/tmp/test.txt"))
        assert isinstance(result, bool)

    def test_safe_path_returns_false(self):
        """Test that a safe path returns False."""
        # /tmp and /home are generally safe on Unix systems
        # For Windows, use a user directory
        if platform.system() == "Windows":
            safe_path = os.path.join(os.path.expanduser("~"), "Documents", "test.txt")
        else:
            safe_path = "/tmp/test.txt"

        result = is_system_path(safe_path)
        assert result is False

    def test_dangerous_path_returns_true(self):
        """Test that a dangerous path returns True."""
        system = platform.system()

        if system == "Windows":
            dangerous_path = "C:\\Windows\\System32\\test.txt"
        else:
            dangerous_path = "/etc/passwd"

        result = is_system_path(dangerous_path)
        assert result is True

    def test_exact_dangerous_path(self):
        """Test exact match with a dangerous path."""
        system = platform.system()

        if system == "Windows":
            dangerous_path = "C:\\Windows"
        else:
            dangerous_path = "/etc"

        result = is_system_path(dangerous_path)
        assert result is True


class TestIsSensitivePath:
    """Tests for is_sensitive_path function (alias)."""

    def test_is_alias_of_is_system_path(self):
        """Test that is_sensitive_path behaves like is_system_path."""
        test_path = "/tmp/test.txt"
        assert is_sensitive_path(test_path) == is_system_path(test_path)


class TestIsDangerousPath:
    """Tests for is_dangerous_path function."""

    def test_returns_bool_by_default(self):
        """Test that is_dangerous_path returns a bool by default."""
        result = is_dangerous_path("/tmp/test.txt")
        assert isinstance(result, bool)

    def test_raise_error_on_dangerous_path(self):
        """Test that raise_error=True raises exception for dangerous paths."""
        system = platform.system()

        if system == "Windows":
            dangerous_path = "C:\\Windows\\System32\\test.txt"
        else:
            dangerous_path = "/etc/passwd"

        with pytest.raises(DangerousPathError) as exc_info:
            is_dangerous_path(dangerous_path, raise_error=True)

        assert "dangerous system location" in str(exc_info.value)

    def test_no_error_on_safe_path(self):
        """Test that raise_error=True doesn't raise exception for safe paths."""
        if platform.system() == "Windows":
            safe_path = os.path.join(os.path.expanduser("~"), "Documents", "test.txt")
        else:
            safe_path = "/tmp/test.txt"

        result = is_dangerous_path(safe_path, raise_error=True)
        assert result is False


class TestDangerousPathError:
    """Tests for DangerousPathError exception."""

    def test_is_exception(self):
        """Test that DangerousPathError is an Exception."""
        assert issubclass(DangerousPathError, Exception)

    def test_can_be_raised(self):
        """Test that DangerousPathError can be raised."""
        with pytest.raises(DangerousPathError):
            raise DangerousPathError("Test error")

    def test_error_message(self):
        """Test that DangerousPathError carries a message."""
        message = "Test error message"
        with pytest.raises(DangerousPathError) as exc_info:
            raise DangerousPathError(message)
        assert str(exc_info.value) == message
