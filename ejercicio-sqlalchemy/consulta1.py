from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Mundial

# se genera enlace al gestor de base de
# datos
engine = create_engine('sqlite:///basemundial.db')


Session = sessionmaker(bind=engine)
session = Session()

# jugadores ordenados por el numero de goles
jugadores = session.query(Mundial).order_by(Mundial.goals).all()
print("Jugadores ordenados por el numero de goles")
for s in jugadores:
    print("%s" % (s)) #se imprime el jugador
    print()