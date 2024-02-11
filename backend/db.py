import sqlite3
from typing import List, Dict
import pandas as pd

class DAO(object):
    
    def __init__(self, path_db='db/database.db'):
        self.conn = sqlite3.connect(path_db)
    
    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS thermal(
                           id VARCHAR(15),
                           temp REAL,
                           datetime INTEGER
                       );
                       """)
        cursor.execute("""
                CREATE TABLE IF NOT EXISTS probes(
                    id VARCHAR(15) PRIMARY KEY,
                    name VARCHAR(30)
                );
                """)
        
    def insert_thermal_entries(self, entries: List):
        cursor = self.conn.cursor()
        
        data = [(entry['id'], entry['temp'], entry['datetime']) for entry in entries]       
        cursor.executemany("INSERT INTO thermal VALUES (?,?,?)", data)
        self.conn.commit()
        
    def get_all_entries(self):
        df = pd.read_sql_query("SELECT * from thermal", self.conn)
        return df
    
    def save_probe_names(self, dict_probes: Dict):
        cursor = self.conn.cursor()
        
        data = [(entry['id'], entry['name']) for entry in entries]   
        cursor.execute("INSERT OR REPLACE INTO probes VALUES (?,?)", (30, 'John'))
        self.conn.commit()

