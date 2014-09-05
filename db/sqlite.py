"""SQLite interface for npcgen"""

import sqlite3
import os

def create_database(dbname):
    """create a sqlite database or return None"""
    if os.path.isfile(dbname):
        return None
    else:
        conn = sqlite3.connect(dbname)
        c = conn.cursor()
        c.execute('''CREATE TABLE classes
                    (name TEXT,
                     description TEXT,
                     alignment BLOB,
                     hitdie INTEGER,
                     skillranks INTEGER,
                     baseattack REAL,
                     fortsave BLOB,
                     refsave BLOB,
                     willsave BLOB
                     )''')
        
        c.execute('''CREATE TABLE skills
                    (name TEXT,
                     ability TEXT,
                     description TEXT,
                     barbarian INTEGER,
                     bard INTEGER,
                     cleric INTEGER,
                     druid INTEGER,
                     fighter INTEGER,
                     monk INTEGER,
                     paladin INTEGER,
                     ranger INTEGER,
                     rogue INTEGER,
                     sorcerer INTEGER,
                     wizard INTEGER
                     )''')

        c.execute('''CREATE TABLE ex
                    (name TEXT,
                     description TEXT,
                     level INTEGER
                     )''')
        c.close()
def get_database(dbname):
    """Return a cursor to given db"""
    if not os.path.isfile(dbname):
        raise IOError

    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    return c
