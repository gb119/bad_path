"""
Darwin (macOS) dangerous/sensitive paths.
"""

# Common sensitive paths for POSIX-based systems
common_paths = [
    "/etc",
    "/bin",
    "/sbin",
    "/boot",
    "/sys",
    "/proc",
    "/dev",
]

system_paths = common_paths + [
    "/System",
    "/Library",
    "/private/etc",  # System configuration (don't use /private to allow /private/tmp)
    "/private/var",  # System variables/logs (but /private/var/tmp is safe)
    "/var",
    "/usr",
    "/Applications",
]
