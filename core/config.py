"""
Central location for environment variables.

Typical usage example:
    import core.config as cfg
    foo = cfg.FOO
"""
import os

from dotenv import load_dotenv

load_dotenv()

RESUME_URL: str = os.environ["RESUME_URL"]
SENTRY_DSN: str = os.environ["SENTRY_DSN"]
