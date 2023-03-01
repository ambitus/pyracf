"""Remove any permissions granting READ access or better to a specific resource"""

from dynamic_access import update_access_dynamic


def main():
    """Entrypoint"""
    update_access_dynamic("del")


if __name__ == "__main__":
    main()
