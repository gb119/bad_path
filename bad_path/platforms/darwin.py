"""
Darwin (macOS) dangerous/sensitive paths.
"""

# Common sensitive paths across all platforms
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
    "/private",
    "/var",
    "/usr",
    "/Applications",
]
