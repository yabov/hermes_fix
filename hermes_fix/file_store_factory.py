import datetime
import os
import sqlite3
import threading
from typing import List

from sqlalchemy import (Column, Float, ForeignKey, Integer, MetaData, String,
                        Table, and_, create_engine, not_, or_, select)

#pylint:disable=no-value-for-parameter


metadata = MetaData()
IN_SEQ = Table('IN_SEQ', metadata,
    Column('msg_num', Integer)
)
OUT_SEQ = Table('OUT_SEQ', metadata,
    Column('msg_num', Integer)
)
MESSAGE_OUT = Table('MESSAGE_OUT', metadata,
  Column('msg_num', Integer, primary_key=True),
  Column('msg_type', String, nullable=False),
  Column('data', String, nullable=False)
 )

SESSION = Table('SESSION', metadata,
    Column('session_date_time', Float, primary_key=True)
)

class SQLAlchemyStore:
    def __init__(self, session_settings: str) -> None:
        connection_string = session_settings['StorageConnectionString']
        self.file_path = None

        if "sqlite:" in connection_string and ":memory:" not in connection_string:
            self.file_path = connection_string.split('///', 1)[1].split('?',1)[0]

            path = os.path.dirname(self.file_path)
            if not os.path.exists(path):
                os.makedirs(path, exist_ok=True)
        
        engine = create_engine(connection_string, echo=False)
        self.db = engine.connect()
        metadata.create_all(engine)
        self._init_schema()

    def _init_schema(self):
        self.db.execute(IN_SEQ.insert(), msg_num=0)
        self.db.execute(OUT_SEQ.insert(), msg_num=1)
        self.db.execute(SESSION.insert(), session_date_time=datetime.datetime.utcnow().timestamp())

    def get_session_time(self) -> str:
        result = self.db.execute(select([SESSION]))
        return result.fetchone()['session_date_time']

    def get_current_in_seq(self) -> int:
        result = self.db.execute(select([IN_SEQ])).fetchone()
        return result['msg_num']

    def set_current_in_seq(self, seq: int) -> None:
        self.db.execute(IN_SEQ.update(), msg_num=seq)

    def get_current_out_seq(self) -> int:
        result = self.db.execute(select([OUT_SEQ]))
        return result.fetchone()['msg_num']

    def set_current_out_seq(self, seq: int) -> None:
        self.db.execute(OUT_SEQ.update(), msg_num=seq)

    def add_message(self, msg_num: int, msg_type: str, msg_buff: str) -> None:
        self.db.execute(MESSAGE_OUT.insert(), msg_num=msg_num, msg_type=msg_type, data=msg_buff)

    def get_messages(self, msg_begin: int, msg_end: int) -> List[str]:
        where_clause = None
        if msg_end:
            where_clause = and_(MESSAGE_OUT.c.msg_num >= msg_begin, 
                                MESSAGE_OUT.c.msg_num <= msg_end)
        else:
            where_clause = MESSAGE_OUT.c.msg_num >= msg_begin

        result = self.db.execute(select([MESSAGE_OUT]).where(where_clause) )
        return result.fetchall()

    def reconnect(self) -> None:
        engine = create_engine('sqlite:///:memory:', echo=True)
        self.db = engine.connect()

    def close(self) -> None:
        self.db.close()

    def new_day(self) -> None:
        self.db.execute(IN_SEQ.delete())
        self.db.execute(OUT_SEQ.delete())
        self.db.execute(MESSAGE_OUT.delete())
        self.db.execute(SESSION.delete())
        self._init_schema()

    def clean_up(self) -> None:
        self.db.close()
        if self.file_path:
            os.remove(self.file_path)

class FileStoreFactory:
    def create_storage(self, session_settings: dict) -> SQLAlchemyStore:
        return SQLAlchemyStore(session_settings)
