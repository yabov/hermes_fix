import os
import sqlite3
import datetime
import threading

class FileStore:
    def __init__(self, session_settings):
        
        self.db = None

        self.file_path = None
        self.lock = threading.Lock()

        if session_settings['FileStorePath'] == ":memory:":
            self.file_path = session_settings['FileStorePath']
            self.db = sqlite3.connect(self.file_path, check_same_thread=False) # pylint: disable=no-member
            self.create_schema()
        else:
            file_name = "%s.%s.%s.db"%(session_settings['BeginString'],session_settings['SenderCompID'],session_settings['TargetCompID'])

            path = session_settings['FileStorePath']
            self.file_path = os.path.join(path, file_name)

            if not os.path.exists(self.file_path): 
                os.makedirs(path, exist_ok=True)
                self.db = sqlite3.connect(self.file_path, check_same_thread=False)# pylint: disable=no-member
                self.create_schema()
            else:
                self.db = sqlite3.connect(self.file_path, check_same_thread=False)# pylint: disable=no-member
        
    def create_schema(self):
        with self.lock:
            cursor = self.db.cursor()
            cursor.execute("""CREATE TABLE IN_SEQ (msg_num int)""")
            cursor.execute("""INSERT INTO IN_SEQ VALUES (0)""")
            cursor.execute("""CREATE TABLE OUT_SEQ (msg_num int)""")
            cursor.execute("""INSERT INTO OUT_SEQ VALUES (1)""")
            cursor.execute("""CREATE TABLE MESSAGE_OUT (msg_num int, msg_type text, msg data)""")
            cursor.execute("""CREATE TABLE SESSION (session_date_time text)""")
            cursor.execute("""INSERT INTO SESSION VALUES (:date_time)""", {'date_time' :datetime.datetime.utcnow()})
            self.db.commit()

    def get_current_in_seq(self):
        with self.lock:
            cursor = self.db.cursor()
            return cursor.execute("""SELECT msg_num from IN_SEQ""").fetchone()[0]

    def set_current_in_seq(self, seq):
        with self.lock:
            cursor = self.db.cursor()
            cursor.execute("""UPDATE IN_SEQ set msg_num = :seq""", {'seq' : seq})
            self.db.commit()

    def get_current_out_seq(self):
        with self.lock:
            cursor = self.db.cursor()
            return cursor.execute("""SELECT msg_num from OUT_SEQ""").fetchone()[0]

    def set_current_out_seq(self, seq):
        with self.lock:
            cursor = self.db.cursor()
            cursor.execute("""UPDATE OUT_SEQ set msg_num = :seq""", {'seq' : seq})
            self.db.commit()

    def add_message(self, msg_num, msg_type, msg_buff):
        with self.lock:
            cursor = self.db.cursor()
            cursor.execute("""INSERT INTO MESSAGE_OUT VALUES (:msg_num, :msg_type, :msg_buf)""", {'msg_num' : msg_num, 'msg_type': msg_type, 'msg_buf' : msg_buff})
            self.db.commit()

    def get_messages(self, msg_begin, msg_end):
        with self.lock:
            cursor = self.db.cursor()
            sql = """SELECT * FROM MESSAGE_OUT WHERE msg_num >= :msg_begin"""
            if msg_end:
                sql += """ and msg_num <= :msg_end"""
            return cursor.execute(sql, {'msg_begin': msg_begin, 'msg_end': msg_end}).fetchall()

    def reconnect(self):
        self.db = sqlite3.connect(self.file_path, check_same_thread=False) # pylint: disable=no-member

    def close(self):
        self.db.close()

    def clean_up(self):
        with self.lock:
            self.db.close()
            del self.db
            self.db = None
            if self.file_path != ":memory:":
                os.remove(self.file_path)

class FileStoreFactory:
    def create_storage(self, session_settings):
        return FileStore(session_settings)