"""Remove any permissions granting READ access or better to a specific resource"""

import dynamic_access

def main():
    """Entrypoint"""
    dynamic_access(False)


if __name__ == "__main__":
    main()
