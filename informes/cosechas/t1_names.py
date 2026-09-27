import subprocess,time,os,json,unicodedata
NAMES="Quiroga, Carrizo, Coronel, Cáceres, Córdoba, Godoy, Ledesma, Villalba, Correa, Duarte, Escobar, Figueroa, Guzmán, Juárez, Peralta, Mansilla, Ayala, Barrios, Acuña, Agüero, Chávez, Farías, Cardozo, Pereyra, Romano, Lucatti, Bianchi, Colombo, Esposito, Ferrari, Ferreyra, Rossi, Russo, Schmidt, Acosta, Aguirre, Flores, Luna, Maldonado, Mendoza, Miranda, Ojeda, Paz, Ponce, Rivero, Rojas, Roldán, Ríos, Silva, Sosa, Vargas, Vera".split(', ')
def key(n):
    n=n.upper().replace('Ñ','\x00')
    n=''.join(c for c in unicodedata.normalize('NFD',n) if unicodedata.category(c)!='Mn')
    return n.replace('\x00','Ñ')
