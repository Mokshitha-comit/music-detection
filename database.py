from sqlalchemy import create_engine, Column, String, Integer, Float, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Tune(Base):
    __tablename__ = 'tunes'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    features = Column(LargeBinary)
    genre = Column(String)
    mood = Column(String)
    path = Column(String)
    tempo = Column(Float)

engine = create_engine('sqlite:///tunes.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

def add_tune(name, features, genre, mood, path, tempo):
    session = Session()
    tune = Tune(name=name, features=features, genre=genre, mood=mood, path=path, tempo=tempo)
    session.add(tune)
    session.commit()
    session.close()

def get_all_tunes():
    session = Session()
    tunes = session.query(Tune).all()
    session.close()
    return tunes