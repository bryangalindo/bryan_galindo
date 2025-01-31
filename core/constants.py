"""
Serves any global constants (e.g., strings, ints, enums) relative
to this code base. Avoid importing the entire module (e.g., import constants)

Typical usage example:
    from core.constants import bar
    foo = bar
"""

JS_CSP_SCRIPTS = [
    "'self'",
    "https://*.jsdelivr.net",
    "https://*.jquery.com",
    "https://*.rawgit.com",
    "https://*.usefathom.com",
]

CSP_SCRIPT_EXCLUSION_HEADERS = " ".join(JS_CSP_SCRIPTS)
RESUME_DEV_URL = (
    "https://docs.google.com/document/d/"
    "15RetRj__KnEulDv_G8xkFDe5huA4553WeDHCSoiXjB0/edit?usp=sharing"
)
