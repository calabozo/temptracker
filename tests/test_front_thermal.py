
import sys
sys.path.append("./")

from backend.db import DAO
from frontend.thermal import get_last_temp


def test_get_last_temp():
    dao = DAO(path_db=':memory:')
    dao.create_tables()
    
    entry1={'id':'a1234', 'temp':23.3, 'datetime':1674675705}
    entry2={'id':'a1245', 'temp':35.7, 'datetime':1674675700}
    entries = [entry1, entry2]
    dao.insert_thermal_entries(entries)
    
    dict_temps = get_last_temp(dao.conn)
    
    assert len(dict_temps) == 2
    assert dict_temps[0]['id'] == 'a1234'
    