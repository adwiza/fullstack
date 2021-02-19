from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class LogEntry(Base):

    __tablename__ = 'logs'
    uid = Column(Integer, primary_key=True)
    ip_addr = Column(String(16))
    timestamp = Column(DateTime)

    def __init__(self, ip_addr, timestamp):
        self.ip_addr = ip_addr
        self.timestamp = timestamp

    def __str__(self):
        return f'{self.ip_addr} on {self.timestamp}'
