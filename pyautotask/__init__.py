"""
Python __init__ to interact with an Autotask site
"""
import urllib3


def http_debug_log_stderr():
    """Dump requests urllib3 debug messages to stderr"""
    urllib3.add_stderr_logger()
