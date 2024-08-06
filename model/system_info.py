from sqlalchemy import create_engine, Column, VARCHAR, Integer, FLOAT, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

from config import URL_DATABASE

Base = declarative_base()
engine = create_engine(URL_DATABASE)
connection = engine.connect()


class System_Info(Base):
    __tablename__ = 'system_info'
    id = Column(Integer, primary_key=True)
    proc_name = Column(VARCHAR(255), nullable=False)
    freq_proc = Column(VARCHAR(255))
    gpu_name = Column(VARCHAR(255), nullable=False)
    gpu_memory = Column(FLOAT)
    total_memory = Column(FLOAT)
    total_virtual_memory = Column(FLOAT)
    hosts_id = Column(ForeignKey('list_hosts.id'))
    host = relationship("List_Hosts", back_populates="system_info")