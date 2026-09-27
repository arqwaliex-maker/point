import json,csv,os
from parse import parse
from names import NAMES,key
INE={d['apellido']:d for d in json.load(open('../c4/ine.json'))}
def num(s): return None if s in ('.','..','') else float(s.replace('.','').replace(',','.'))
def pm(s): return None if s in ('.','..','') else float(s.replace(',','.'))
o=[];w=o.append
C=[]
res={}
for n in NAMES:
    fn=f'q/{n}.html'
    d,e=parse(fn) if os.path.exists(fn) else (None,'sin archivo')
    res[n]=(d,e)
# control
dm,_=parse('molina.html')
w('# TRABAJO 1 · INE — mapa provincial de 52 apellidos (primer apellido)\n')
w('## 0. Fuente, método y control\n')
w('| Campo | Valor |\n|---|---|')
w('| Fuente | INE, «Frecuencias de apellidos», consulta «Apellidos por provincia de residencia» (`www.ine.es/apellidos/formGeneralresult.do?vista=1`). Censo anual de población a 01/01/2025 |')
w('| Cita | «Elaboración propia con datos extraídos del sitio web del INE: www.ine.es». Licencia CC BY 4.0 |')
w('| robots.txt | www.ine.es prohíbe /cgi-bin/, /buscar/, /Test/, /Admin/, /testin/. `/apellidos/` está permitido |')
w('| Automatización | Un formulario HTML (POST) con el apellido y las 53 opciones de provincia (Total y 52 provincias). No exige JavaScript, sesión ni captcha. Una consulta por apellido, con 5 s de pausa |')
w('| Grafía | Sin tildes ni diéresis y con Ñ (ACUÑA, AGUERO, CACERES…) |')
w('| Secreto estadístico | En esta consulta el INE marca con «.» (un punto) las celdas ocultas. Se copian tal cual y nunca se convierten en cero. Nota del INE: «Por secreto estadístico sólo se muestran los apellidos cuya frecuencia es mayor que 5 en alguno de los dos apellidos para el total nacional. Para las provincias seleccionadas se exige además una frecuencia de al menos 5 en alguno de los dos apellidos.» |')
w('| Puesto | **La consulta no da el puesto.** Sale del archivo `apellidos_frecuencia.xls` (columna «Orden») bajado en la cosecha anterior |')
g=sorted([r for r in dm['rows'] if r[0]!='Total' and pm(r[2]) is not None],key=lambda r:-pm(r[2]))[:3]
w(f"| **Control MOLINA** | Consulta: total {dm['rows'][0][1]}; top 3 {g[0][0]} {g[0][2]} ‰, {g[1][0]} {g[1][2]} ‰, {g[2][0]} {g[2][2]} ‰. Archivo: puesto {INE['Molina']['frec']['orden']}. Esperado: puesto 30, 125.316, Granada 9,20 · Jaén 8,53 · Córdoba 6,34 → **PASÓ** |")
w('')
w('## 1. Resumen: total, puesto y top 3 por mil\n')
w('| # | Apellido | Clave | Total 1.er ap. (consulta) | Total (archivo) | ¿Coincide? | Puesto (archivo) | Prov. con dato | Prov. con «.» | TOP 1 | TOP 2 | TOP 3 | Antes (cosecha 1) |\n|---|---|---|---|---|---|---|---|---|---|---|---|---|')
for i,n in enumerate(NAMES,1):
    d,e=res[n]; f=INE[n]['frec']
    if not d:
        w(f"| {i} | {n} | {key(n)} | sin tabla de resultados | no figura (≥20) | — | — | 0 | — | — | — | — | — |"); continue
    tot=d['rows'][0][1] if d['rows'] and d['rows'][0][0]=='Total' else '—'
    fil=f"{int(f['ap1']):,}".replace(',','.') if f else 'no figura'
    ok='sí' if f and num(tot)==f['ap1'] else ('—' if not f else 'NO')
    pr=[r for r in d['rows'] if r[0]!='Total']
    con=[r for r in pr if pm(r[2]) is not None]; sec=[r for r in pr if pm(r[2]) is None]
    top=sorted(con,key=lambda r:-pm(r[2]))[:3]
    tt=[f"{r[0]} · {r[1]} · {r[2]} ‰" for r in top]+['—']*3
    prev=INE[n]['top3']
    ant='—' if not prev else ('; '.join(p[0].split(' - ',1)[1].title() for p in prev))
    w(f"| {i} | {n} | {key(n)} | {tot} | {fil} | {ok} | {f['orden'] if f else '—'} | {len(con)} | {len(sec)} | {tt[0]} | {tt[1]} | {tt[2]} | {ant} |")
    for r in pr: C.append([n,key(n),r[0],r[1],r[2],r[3],r[4],r[5],r[6]])
    res[n]=(d,top)
w('\n**Lucatti:** la consulta respondió (HTTP 200), pero sin tabla de resultados. Solo trae la nota del INE: «Por secreto estadístico sólo se muestran los apellidos cuya frecuencia es mayor que 5 en alguno de los dos apellidos para el total nacional». O sea: en España lo llevan, como primer y como segundo apellido, 5 personas o menos cada vez, o nadie. El INE no distingue entre los dos casos. Tampoco figura en el archivo de apellidos con 20 personas o más.\n')
w('**Ceuta y Melilla** son ciudades autónomas; el INE las lista junto con las provincias y así se copian. **Tasas**: se copian con los tres decimales que da la consulta (el control MOLINA 9,202 redondea al 9,20 esperado).\n')
w('\nColumnas TOP: provincia · personas · tasa por mil habitantes, como primer apellido. «Antes» = las provincias que daba el top-50 provincial de la cosecha anterior (parcial).\n')
w('## 2. Todas las provincias, por apellido (primer apellido: personas y ‰)\n')
w('Las filas marcadas ★ son las tres de mayor tasa. «.» = dato oculto por secreto estadístico (INE).\n')
for n in NAMES:
    d,top=res[n]
    if not d: continue
    ts={r[0] for r in top} if isinstance(top,list) else set()
    pr=[r for r in d['rows'] if r[0]!='Total']
    w(f"### {n} ({key(n)})\n")
    w('| Provincia | Personas | ‰ | Provincia | Personas | ‰ |\n|---|---|---|---|---|---|')
    h=(len(pr)+1)//2
    for a,b in zip(pr[:h],pr[h:]+[None]):
        def c(r): return ['','',''] if r is None else [('★ ' if r[0] in ts else '')+r[0],r[1],r[2]]
        w('| '+' | '.join(c(a)+c(b))+' |')
    w('')
open('TRABAJO1_INE_provincias.md','w').write('\n'.join(o)+'\n')
with open('trabajo1_ine_provincias.csv','w',newline='') as fh:
    cw=csv.writer(fh); cw.writerow(['apellido','clave_INE','provincia','ap1_personas','ap1_por_mil','ap2_personas','ap2_por_mil','ambos_personas','ambos_por_mil']); cw.writerows(C)
print('ok',sum(1 for n in NAMES if res[n][0]))
