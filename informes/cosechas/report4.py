import json
D=json.load(open('ine.json'))
def n(x): return f"{int(x):,}".replace(',','.') if isinstance(x,(int,float)) else str(x)
def pm(x): return f"{x:.2f}".replace('.',',')
o=[];w=o.append
w('# COSECHA 4 · INE — frecuencia de los 90 apellidos en España\n')
w('## 0. Fuente y método\n')
w('| Campo | Valor |\n|---|---|')
w('| Fuente | INE, «Apellidos y nombres más frecuentes». Censo de población a 1/1/2025 (publicado 23/04/2026) |')
w('| Descarga masiva | **Sí, parcial.** (1) `www.ine.es/daco/daco42/nombyapel/apellidos_frecuencia.xls`: todos los apellidos con ≥20 personas, total nacional. (2) `…/apellidos_mas_frecuentes.xls`: los 100 más frecuentes de España y los **50 más frecuentes de cada provincia**, con tasa «Por 1.000» |')
w('| Sin descarga masiva | El desglose provincial **completo** de cada apellido solo está en la consulta interactiva (`/apellidos/inicio.do`), una consulta por apellido. **No se hicieron** (pediste no hacer 90 consultas manuales) |')
w('| robots.txt | www.ine.es prohíbe /cgi-bin/, /buscar/, /Test/, /Admin/, /testin/. `/daco/` está permitido |')
w('| Rango nacional | Columna «Orden» del archivo (1): orden por frecuencia como **primer** apellido |')
w('| Top 3 provincias | Tasa «Por 1.000» habitantes de la provincia de residencia, **como primer apellido**, tomada de la hoja PROVINCIAS_RESIDENCIA del archivo (2) |')
w('| ¿Top 3 seguro? | Una provincia donde el apellido no está entre los 50 primeros tiene una tasa menor que la de su puesto 50. «SEGURO» = la 3.ª tasa listada es ≥ la mayor de esas cotas, así que ninguna provincia no listada puede superarla. «PARCIAL» = no se puede garantizar sin la consulta interactiva |')
w('| Grafía | El INE no usa tildes ni diéresis (AGUERO); conserva la Ñ (MUÑOZ, ACUÑA, NUÑEZ) |')
w('| Licencia y cita | CC BY 4.0 — «Elaboración propia con datos extraídos del sitio web del INE: www.ine.es» |')
w('')
w('## 1. Tabla\n')
w('| Apellido | Clave INE | Rango nac. (1.er ap.) | 1.er apellido | 2.º apellido | Ambos | Provincias donde está en el top 50 | Top 3 provincias (por 1.000 hab.) | Top 3 |\n|---|---|---|---|---|---|---|---|---|')
for d in D:
    f=d['frec']
    if not f:
        w(f"| {d['apellido']} | {d['clave']} | — | no figura (menos de 20 personas, o no existe) | — | — | — | — | — |"); continue
    ambos=n(f['ambos']) if f['ambos']!='..' else '«..» (secreto estadístico)'
    top='; '.join(f"{t[0].split(' - ',1)[1].title().replace(' De ',' de ')} {pm(t[3])}‰ ({n(t[2])}; puesto {t[1]})" for t in d['top3']) or '—'
    st='SEGURO' if d['top3_seguro'] else ('no calculable' if not d['top3'] else 'PARCIAL')
    w(f"| {d['apellido']} | {d['clave']} | {f['orden']} | {n(f['ap1'])} | {n(f['ap2'])} | {ambos} | {d['prov_listadas']} | {top} | {st} |")
w('')
nt=[d['apellido'] for d in D if not d['top3']]
w(f"**Sin dato provincial en la descarga masiva ({len(nt)}):** no están en el top 50 de ninguna provincia: "+', '.join(nt)+'. Para ellos solo existe la consulta interactiva, que no se hizo.\n')
w('**Nota:** Lucatti no figura en el archivo de apellidos con ≥20 personas. Eso significa que en España lo llevan menos de 20 personas como primer y segundo apellido, o nadie. El archivo no distingue entre los dos casos.')
open('COSECHA4_ine.md','w').write('\n'.join(o)+'\n')
