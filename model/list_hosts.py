from sqlalchemy import create_engine, Column, Integer, VARCHAR
from sqlalchemy.orm import declarative_base, relationship

from config import URL_DATABASE

Base = declarative_base()
engine = create_engine(URL_DATABASE)
connection = engine.connect()


class List_Hosts(Base):
    __tablename__ = 'list_hosts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    host_name = Column(VARCHAR(255), nullable=False)
    ip_address = Column(VARCHAR(255), nullable=False)
    mac_address = Column(VARCHAR(255), nullable=False)
    system_info = relationship("System_Info", back_populates="host")
    monitoring_systems = relationship("Monitoring_System", back_populates="host")