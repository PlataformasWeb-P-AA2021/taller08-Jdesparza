from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Mundial

# se importa información del archivo configuracion
from configuracion import cadenaMundial
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadenaMundial)

Session = sessionmaker(bind=engine)
session = Session()

archivo = open('data/mundial2018.csv', 'r', encoding='utf-8')
for linea in archivo:
    linea = linea.replace('\n', '')
    token = linea.split('|')
    #print(token)
    mundial = Mundial(numero = token[0], fIFADisplayName = token[1], country = token[2], 
        lastName =  token[3], firstName = token[4], shirtName = token[5], pOS = token[6],
        height =  token[7], caps = token[8], goals = token[9])

    session.add(mundial)
archivo.close()

# se confirma las transacciones
session.commit()
