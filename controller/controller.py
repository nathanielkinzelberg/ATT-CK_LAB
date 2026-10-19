import argparse
import json
import sys
import os
from dotenv import load_dotenv
from controller.client import AgentClient
from shared.logging_config import get_logger

load_dotenv()

logger = get_logger("controller")

def main():
    """Entry point for the ATT&CK-Pi Lab controller CLI."""
    parser = argparse.ArgumentParser(
        prog="controller",
        description="ATT&CK-Pi Lab - Adversary Simulation Controller"
    )

    parser.add_argument("--target", required=True, help="IP adress of the agent e.g. 192.168.1.101")

    subparsers = parser.add_subparsers(dest="command")

    # 'status' command
    subparsers.add_parser("status", help="Check if the agent is alive")

    # 'list' command
    subparsers.add_parser("list", help="List all supported techniques")

    # 'run' command
    run_parser = subparsers.add_parser("run", help="Execute a technique")
    run_parser.add_argument("--technique", required=True, help="Technique ID to execute e.g. T1082")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    client = AgentClient(host=args.target)

    if args.command == "status":
        result = client.health_check()
        print(json.dumps(result, indent=2))

    elif args.command == "list":
        result = client.list_techniques()
        print(json.dumps(result, indent=2))

    elif args.command == "run":
        logger.info(f"Requesting technique {args.technique} from {args.target}")
        result = client.execute_technique(args.technique)
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()