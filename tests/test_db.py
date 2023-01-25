import sys
sys.path.append("./")

from backend.db import DAO


def test_insert_data():
    dao = DAO(path_db=':memory:')
    dao.create_tables()
    
    entry1={'id':'a1234', 'temp':23.3, 'datetime':1674675705}
    entry2={'id':'a1245', 'temp':35.7, 'datetime':1674675700}
    entries = [entry1, entry2]
    dao.insert_thermal_entries(entries)
    df = dao.get_all_entries()
    
    assert df.shape[0] == 2