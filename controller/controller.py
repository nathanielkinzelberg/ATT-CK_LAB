import argparse
import json
import sys
import os
from dotenv import load_dotenv
from controller.client import AgentClient
from shared.logging_config import get_logger

load_dotenv()

logger = get_logger("controller")
