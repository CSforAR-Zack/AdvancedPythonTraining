from sqlalchemy import Column, Integer, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Day(Base):
    __tablename__ = 'days'
    id = Column(Integer, primary_key=True)
    date = Column('date', DateTime)
    tmin = Column('tmin', Integer)
    tmax = Column('tmax', Integer)
    
def main():
    engine = create_engine("sqlite:///data.db")

    Base.metadata.create_all(engine)

if __name__ == "__main__":
    main()