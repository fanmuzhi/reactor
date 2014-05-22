"""test sqlalchemy orm
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
Base = declarative_base()
Engine = create_engine("sqlite:///topaz.db")
Session = sessionmaker(bind=Engine)


class DUT(Base):
    __tablename__ = "dut"

    id = Column(Integer, primary_key=True)
    pwrcycs = Column("PWRCYCS", Integer)
    lastcap = Column(Integer)
    model = Column(String(10))
    fwver = Column(String(10))
    hwver = Column(String(10))
    cappn = Column(String(10))
    sn = Column(String(10))
    pcbver = Column(String(10))
    mfdate = Column(String(10))
    endusr = Column(String(10))
    pca = Column(String(10))
    cint = Column(Integer)

    slotnum = Column(Integer)
    archieved = Column(Integer)   # running or archieved.
    status = Column(Integer)
    testdate = Column(Integer)

    #DUT is one to many class refer to Cycles
    cycles = relationship("Cycle", backref="dut")


class Cycle(Base):
    __tablename__ = "cycle"

    id = Column(Integer, primary_key=True)
    readiness = Column(Integer)
    pgemstat = Column(Integer)
    temp = Column(Integer)
    vin = Column(Integer)
    vcap = Column(Integer)
    vc1 = Column(Integer)
    vc2 = Column(Integer)
    vc3 = Column(Integer)
    vc4 = Column(Integer)
    vc5 = Column(Integer)
    vc6 = Column(Integer)
    reserved = Column(Integer)
    time = Column(Integer)
    dutid = Column(Integer, ForeignKey("dut.id"))


if __name__ == "__main__":
    DUT.metadata.create_all(Engine)     # create table
    Cycle.metadata.create_all(Engine)     # create table

    session = Session()

    dut = DUT()
    dut.pwrcycs = 150
    dut.lastcap = 117
    dut.model = "topaz"

    cycle = Cycle()
    cycle.vin = 117
    cycle.vcap = 112
    cycle.temp = 45
    dut.cycles.append(cycle)

    session.add(dut)
    session.commit()
