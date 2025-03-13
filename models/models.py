from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, Text, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime
import os

# Definimos la ruta absoluta a la base de datos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, '..', 'database', 'ai_sales_strategy.db')

# Crear motor SQLite
engine = create_engine(f'sqlite:///{db_path}', echo=True)

# Declarar base
Base = declarative_base()

# Modelo Prospecto
class Prospect(Base):
    __tablename__ = 'prospects'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    company = Column(String(100), nullable=False)
    phone = Column(String(20))
    created_at =

from sqlalchemy import create_engine, Column, Integer, 
String, DateTime, Float, Text, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from datetime import datetime

# Conexión con SQLite
engine = create_engine('sqlite:///../database/ai_sales_strategy.db', echo=True)

Base = declarative_base()

# Modelo Prospect (cliente potencial)
class Prospect(Base):
    __tablename__ = 'prospects'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    company = Column(String(100), nullable=False)
    phone = Column(String(20), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    negotiations = relationship('Negotiation', back_populates='prospect')

# Modelo Negotiation (negociación comercial)
class Negotiation(Base):
    __tablename__ = 'negotiations'

    id = Column(Integer, primary_key=True)
    prospect_id = Column(Integer, ForeignKey('prospects.id'), nullable=False)
    status = Column(String(50), default='En Proceso')  # Ej: "En Proceso", "Ganada", "Perdida"
    start_date = Column(DateTime, default=datetime.utcnow)
    estimated_close_date = Column(DateTime, nullable=True)
    value = Column(Float, nullable=True)

    prospect = relationship('Prospect', back_populates='negotiations')
    interactions = relationship('Interaction', back_populates='negotiation')

# Modelo Interaction (registro de interacciones con prospectos)
class Interaction(Base):
    __tablename__ = 'interactions'

    id = Column(Integer, primary_key=True)
    negotiation_id = Column(Integer, ForeignKey('negotiations.id'), nullable=False)
    date = Column(DateTime, default=datetime.utcnow)
    notes = Column(Text)

    negotiation = relationship('Negotiation', back_populates='interactions')

# Crear las tablas en la base de datos
Base.metadata.create_all(engine)

# Crear sesión para pruebas rápidas (opcional)
Session = sessionmaker(bind=engine)
session = Session()


