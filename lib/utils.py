# Utility library for the pipelines workshop
from datetime import datetime

def timestamp():
    """
    Return a timestamp string. Format: TS[YYYYMMDD.HHmmSS]
    Resolution is 1 sec.
    """
    return 'TS' + datetime.now().strftime('%Y%m%d.%H%M%S')