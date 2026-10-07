import platform
import socket
import time
from shared.base import AttackTechnique
from shared.models import TechniqueResult
from shared.logging_config import get_logger

logger = get_logger("t1082")  # creates a logger named "t1082" — shows up in every log line