"""Console script for modern_renaissance."""
import argparse
import sys

from modern_renaissance.modern_renaissance import test_logger


def main():
    """Console script for modern_renaissance."""
    parser = argparse.ArgumentParser()
    parser.add_argument("_", nargs="*")
    args = parser.parse_args()

    print("Arguments: " + str(args._))
    test_logger()


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
