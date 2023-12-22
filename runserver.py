"""Runs an instance of the Flask server, which runs the application.

Author: Michael Willen"""

from sys import stderr
import argparse
import sys
from stylebook import app


def main(args=None):
    """main function. Calls parse_args and runs the Flask server."""

    port = parse_args(args)

    try:
        app.run(host='0.0.0.0', port=port, debug=True)
    except Exception as ex:
        print(ex, file=stderr)
        sys.exit(1)

#-----------------------------------------------------------------------

def parse_args(args):
    """
    * Sets up parsing for command line arguments
    * Reads in command line arguments and returns port"""

    parser = argparse.ArgumentParser(description="Stylebook for the Yale Daily News.")
    parser.add_argument("port", help="the port at which the server should listen", type=int)
    args = parser.parse_args(args)
    port = int(args.port)

    return port

#-----------------------------------------------------------------------

if __name__ == '__main__':
    main()
