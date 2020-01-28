import datetime
import os
import sqlite3
import threading
from typing import List


class FileStore:
    def __init__(self, session_settings: str) -> None:

        self.db = None

        self.file_path = None
        self.lock = threading.Lock()

        if session_settings['FileStorePath'] == ":memory:":
            self.file_path = session_settings['FileStorePath']
            self.db = sqlite3.connect(  # pylint: disable=no-member
                self.file_path, check_same_thread=False)
            self._create_schema()
        else:
            file_name = "%s.%s.%s.db" % (
                session_settings['BeginString'], session_settings['SenderCompID'], session_settings['TargetCompID'])

            path = session_settings['FileStorePath']
            self.file_path = os.path.join(path, file_name)

            if not os.path.exists(self.file_path):
                os.makedirs(path, exist_ok=True)
                self.db = sqlite3.connect(  # pylint: disable=no-member
                    self.file_path, check_same_thread=False)
                self._create_schema()
            else:
                self.db = sqlite3.connect(  # pylint: disable=no-member
                    self.file_path, check_same_thread=False)  

    def _create_schema(self):
        with self.lock:
            cursor = self.db.cursor()
            cursor.execute("""CREATE TABLE IN_SEQ (msg_num int)""")
            cursor.execute("""CREATE TABLE OUT_SEQ (msg_num int)""")
            cursor.execute(
                """CREATE TABLE MESSAGE_OUT (msg_num int, msg_type text, msg data)""")
            cursor.execute("""CREATE TABLE SESSION (session_date_time real)""")
            self.db.commit()
        self._init_schema()

    def _init_schema(self):
        with self.lock:
            cursor = self.db.cursor()
            cursor.execute("""INSERT INTO IN_SEQ VALUES (0)""")
            cursor.execute("""INSERT INTO OUT_SEQ VALUES (1)""")
            cursor.execute("""INSERT INTO SESSION VALUES (:date_time)""", {
                           'date_time': datetime.datetime.utcnow().timestamp()})
            self.db.commit()

    def get_session_time(self) -> str:
        with self.lock:
            cursor = self.db.cursor()
            return cursor.execute("""SELECT session_date_time from SESSION""").fetchone()[0]

    def get_current_in_seq(self) -> int:
        with self.lock:
            cursor = self.db.cursor()
            return cursor.execute("""SELECT msg_num from IN_SEQ""").fetchone()[0]

    def set_current_in_seq(self, seq: int) -> None:
        with self.lock:
            cursor = self.db.cursor()
            cursor.execute(
                """UPDATE IN_SEQ set msg_num = :seq""", {'seq': seq})
            self.db.commit()

    def get_current_out_seq(self) -> int:
        with self.lock:
            cursor = self.db.cursor()
            return cursor.execute("""SELECT msg_num from OUT_SEQ""").fetchone()[0]

    def set_current_out_seq(self, seq: int) -> None:
        with self.lock:
            cursor = self.db.cursor()
            cursor.execute(
                """UPDATE OUT_SEQ set msg_num = :seq""", {'seq': seq})
            self.db.commit()

    def add_message(self, msg_num: int, msg_type: str, msg_buff: str) -> None:
        with self.lock:
            cursor = self.db.cursor()
            cursor.execute("""INSERT INTO MESSAGE_OUT VALUES (:msg_num, :msg_type, :msg_buf)""", {
                           'msg_num': msg_num, 'msg_type': msg_type, 'msg_buf': msg_buff})
            self.db.commit()

    def get_messages(self, msg_begin: int, msg_end: int) -> List[str]:
        with self.lock:
            cursor = self.db.cursor()
            sql = """SELECT * FROM MESSAGE_OUT WHERE msg_num >= :msg_begin"""
            if msg_end:
                sql += """ and msg_num <= :msg_end"""
            return cursor.execute(sql, {'msg_begin': msg_begin, 'msg_end': msg_end}).fetchall()

    def reconnect(self) -> None:
        with self.lock:
            self.db = sqlite3.connect(  # pylint: disable=no-member
                self.file_path, check_same_thread=False) 

    def close(self) -> None:
        with self.lock:
            self.db.close()

    def new_day(self) -> None:
        with self.lock:
            cursor = self.db.cursor()
            cursor.execute("""DELETE FROM  IN_SEQ""")
            cursor.execute("""DELETE FROM  OUT_SEQ""")
            cursor.execute("""DELETE FROM  MESSAGE_OUT""")
            cursor.execute("""DELETE FROM  SESSION""")
            self.db.commit()
        self._init_schema()

    def clean_up(self) -> None:
        with self.lock:
            self.db.close()
            if self.file_path != ":memory:":
                os.remove(self.file_path)


class FileStoreFactory:
    def create_storage(self, session_settings: dict) -> FileStore:
        return FileStore(session_settings)
