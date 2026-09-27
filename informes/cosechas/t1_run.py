import subprocess,time,os,json,unicodedata
from parse import parse
NAMES="Quiroga, Carrizo, Coronel, Cáceres, Córdoba, Godoy, Ledesma, Villalba, Correa, Duarte, Escobar, Figueroa, Guzmán, Juárez, Peralta, Mansilla, Ayala, Barrios, Acuña, Agüero, Chávez, Farías, Cardozo, Pereyra, Romano, Lucatti, Bianchi, Colombo, Esposito, Ferrari, Ferreyra, Rossi, Russo, Schmidt, Acosta, Aguirre, Flores, Luna, Maldonado, Mendoza, Miranda, Ojeda, Paz, Ponce, Rivero, Rojas, Roldán, Ríos, Silva, Sosa, Vargas, Vera".split(', ')
def key(n):
    n=n.upper().replace('Ñ','\x00')
    n=''.join(c for c in unicodedata.normalize('NFD',n) if unicodedata.category(c)!='Mn')
    return n.replace('\x00','Ñ')
args=open('args.txt').read().split()
os.makedirs('q',exist_ok=True)
for n in NAMES:
    fn=f'q/{n}.html'
    if os.path.exists(fn) and parse(fn)[0]: continue
    for a in range(3):
        r=subprocess.run(['curl','-sSL','-A','Mozilla/5.0 (research script)','-c','cj','-b','cj','-e','https://www.ine.es/apellidos/formGeneral.do?vista=1',*args,'--data-urlencode','cmb6='+key(n),'--data-urlencode','busc_3=','--data-urlencode','btnBuscar=Consultar','-o',fn,'-w','%{http_code}','https://www.ine.es/apellidos/formGeneralresult.do?vista=1'],capture_output=True,text=True)
        d,e=parse(fn) if os.path.exists(fn) else (None,'nofile')
        print(n,key(n),r.stdout,'OK' if d else 'FAIL '+str(e)[:150],flush=True)
        time.sleep(5)
        if d or r.stdout=='200': break
open('q/DONE','w').write('ok')
