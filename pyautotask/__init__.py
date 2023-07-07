"""
Python __init__ to interact with an Autotask site
"""
from __future__ import absolute_import
import urllib3
from pyautotask.models.ticket_entity_info.py import TicketEntityInfo
import pyautotask.atsite

def http_debug_log_stderr():
    """Dump requests urllib3 debug messages to stderr"""
    urllib3.add_stderr_logger()
