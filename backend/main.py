import logging
import argparse
import time
from db import DAO
from thermal import get_temperature

SECS_ELAPSED = 60*5

def main(db_filename):
    dao = DAO(path_db=db_filename)
    dao.create_tables()
    
    while True:
        entries = get_temperature()
        dao.insert_thermal_entries(entries)
        logging.debug(f"Saving temperatures {len(entries)} sensors: {','.join([str(x['temp']) for x in entries])}")
        time.sleep(SECS_ELAPSED)
        
    
if __name__=="__main__":

    parser = argparse.ArgumentParser(
        description='Downloads data from different sensors.',
        epilog='''It stores the data in the table data.''')
    parser.add_argument('--log' ,metavar='LEVEL', help='Set log level. ERROR, WARNING, INFO, DEBUG', default='DEBUG')
    parser.add_argument('--logFile' ,metavar='LOG_FILE', help='Saves the log info in a file.',default=None)
    parser.add_argument('--db', metavar='FILE_NAME', help='SQLite datafile to store the data',default='thermal.db')

    args = parser.parse_args()

    loglevel =args.log
    log_file =args.logFile
    db_file  =args.db

    numeric_level = getattr(logging, loglevel.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level: %s' % loglevel)

    logging.basicConfig(filename=log_file ,format='%(asctime)s %(levelname)s:\t%(message)s' ,level=numeric_level)
    logging.info(f"Starting thermal. Saving in {db_file}")
    main(db_file)
    

