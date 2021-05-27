from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

# se importa información del archivo configuracion
from configuracion import cadenaMundial

# se genera en enlace al gestor de base de
# datos
engine = create_engine(cadenaMundial)

Base = declarative_base()

# tabla del Mundial con los datos de todos los jugadores
class Mundial(Base):
    __tablename__ = 'mundial'
    id = Column(Integer, primary_key=True)
    numero = Column(Integer, nullable=False)
    fIFADisplayName = Column(String(100), nullable=False)
    country = Column(String(100), nullable=False)
    lastName = Column(String(100), nullable=False)
    firstName = Column(String(100), nullable=False)
    shirtName = Column(String(100), nullable=False)
    pOS = Column(String(100), nullable=False)
    height = Column(Integer, nullable=False)
    caps = Column(Integer, nullable=False)
    goals = Column(Integer, nullable=False)

    def __repr__(self):
        return "Mundial: numero= %s - fIFADisplayName= %s - country= %s - lastName= %s" \
            "firstName= %s - shirtName= %s - pOS= %s - height= %s - caps= %s - goals= %s" % (
                self.numero,
                self.fIFADisplayName,
                self.country,
                self.lastName,
                self.firstName,
                self.shirtName,
                self.pOS,
                self.height,
                self.caps,
                self.goals
                )


Base.metadata.create_all(engine)
