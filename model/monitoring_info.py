from sqlalchemy import create_engine, Column, ARRAY, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

from config import URL_DATABASE

Base = declarative_base()
engine = create_engine(URL_DATABASE)
connection = engine.connect()


class Monitoring_System(Base):
    __tablename__ = 'monitoring_system'
    id = Column(Integer, primary_key=True)
    cpu_percent = Column(ARRAY(String))
    gpu_percent = Column(ARRAY(String))
    used_virtual_memory = Column(ARRAY(String))
    temperature_gpu = Column(ARRAY(String))
    used_disk = Column(ARRAY(String))
    time_monitoring = Column(ARRAY(String))
    host_id = Column(ForeignKey('list_hosts.id'))
    host = relationship("List_Hosts", back_populates="monitoring_systems")