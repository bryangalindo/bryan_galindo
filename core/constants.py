"""
Serves any global constants (e.g., strings, ints, enums) relative
to this code base. Avoid importing the entire module (e.g., import constants)

Typical usage example:
    from core.constants import bar
    foo = bar
"""
CSP_SCRIPT_EXCLUSION_HEADERS = (
    "cdn.jsdelivr.net code.jquery.com cdn.rawgit.com cdn.usefathom.com"
)
