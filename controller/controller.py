import argparse  # built-in Python library — parses CLI commands and flags
import json       # built-in Python library — formats the result as readable JSON
import sys        # built-in Python library — used to exit the program with an error code
import os         # built-in Python library — used to access environment variables
from dotenv import load_dotenv           # loads the .env file so we can read the API token
from controller.client import AgentClient  # our HTTP client that talks to the agent
from shared.logging_config import get_logger  # shared logging setup from Phase 1

load_dotenv()  # reads .env and makes ATTACK_PI_API_TOKEN available

logger = get_logger("controller")  # creates a logger named "controller"


def main():
    """Entry point for the ATT&CK-Pi Lab controller CLI."""

    # create the top-level argument parser — this handles --target and the subcommands
    parser = argparse.ArgumentParser(
        prog="controller",
        description="ATT&CK-Pi Lab - Adversary Simulation Controller"
    )

    # --target is required for every command — it's the Pi's IP address
    parser.add_argument("--target", required=True, help="IP address of the agent e.g. 192.168.1.101")

    # subparsers lets us define multiple commands: status, list, run
    subparsers = parser.add_subparsers(dest="command")  # dest="command" stores which command was typed

    # 'status' command — checks if the agent is alive
    subparsers.add_parser("status", help="Check if the agent is alive")

    # 'list' command — lists all supported techniques
    subparsers.add_parser("list", help="List all supported techniques")

    # 'run' command — executes a technique, requires --technique flag
    run_parser = subparsers.add_parser("run", help="Execute a technique")
    run_parser.add_argument("--technique", required=True, help="Technique ID to execute e.g. T1082")

    # parse whatever the user typed into the args object
    args = parser.parse_args()

    # if no command was typed, print help and exit
    if not args.command:
        parser.print_help()
        sys.exit(1)

    # create the HTTP client pointed at the target IP
    client = AgentClient(host=args.target)

    if args.command == "status":
        result = client.health_check()          # calls GET /health on the agent
        print(json.dumps(result, indent=2))     # prints the result as formatted JSON

    elif args.command == "list":
        result = client.list_techniques()       # calls GET /techniques on the agent
        print(json.dumps(result, indent=2))

    elif args.command == "run":
        logger.info(f"Requesting technique {args.technique} from {args.target}")
        result = client.execute_technique(args.technique)  # calls POST /techniques/{id}/execute
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()  # only runs if this file is executed directly, not when imported
