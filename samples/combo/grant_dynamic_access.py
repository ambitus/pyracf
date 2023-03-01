"""Ensure a user has at least READ access to a specific resource"""

from dynamic_access import update_access_dynamic


def main():
    """Entrypoint"""
    update_access_dynamic("add")


if __name__ == "__main__":
    main()
