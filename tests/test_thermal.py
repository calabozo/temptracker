import sys
sys.path.append("./")

from backend.thermal import get_temperature
from time import time

def test_get_temperature():
    out = get_temperature()
    
    now = int(time())
    assert len(out) > 0
    assert -100 < out[0]['temp'] < 200
    assert (now-1000) < out[0]['datetime'] <= now
    