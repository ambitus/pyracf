"""Ensure a user has at least READ access to a specific resource"""

import dynamic_access

def main():
    """Entrypoint"""
    dynamic_access(True)


if __name__ == "__main__":
    main()
