import json
D=json.load(open('cag_parsed.json'))
def n(x): return f"{x:,}".replace(',','.')
def pc(s): return s.replace('.',',')
o=[];w=o.append
w('# COSECHA 2 · Cartografía dos apelidos de Galicia (ILG-USC)\n')
w('## 0. Fuente y método\n')
w('| Campo | Valor |\n|---|---|')
w('| Fuente | Instituto da Lingua Galega, Universidade de Santiago de Compostela, *Cartografía dos apelidos de Galicia*, ISSN 2659-8205 |')
w('| Consulta | `https://ilg.usc.es/cag/Controlador?busca=<apellido>`: minúsculas, sin tildes, **con ñ**; una consulta por apellido |')
w('| robots.txt | Permitido. `Crawl-delay: 10` → 10 s de espera entre consultas (se respetó) |')
w('| Fecha de consulta | 27/09/2026 |')
w('| Control | «rodriguez» → **236.756 ocorrencias, posición 1** → **PASÓ** (esperado: 236.756 y posición 1) |')
w('| Top 3 | Los tres primeros concellos de la tabla de resultados, que la página ordena por porcentaxe descendente (comprobado en las 90 consultas) |')
w('| Posición «N[k]» | Se copia tal cual. La página no explica el corchete. Por los datos, parece el número de apellidos empatados en esa posición: Esposito, Ferreyra y Schmidt dan 14 ocorrencias y «1359[174]» cada uno. **Es una deducción, no una definición de la fuente.** |')
w('| Agüero | «aguero» → 21. «agüero» (con diéresis) → devuelve una ficha vacía (0) con el nombre en blanco: el buscador no procesa la ü. Vale el dato de «aguero» |')
w('')
w('## 1. Tabla (control primero)\n')
w('| Apellido | Forma consultada | Ocorrencias | Porcentaxe | Posición | Nº concellos | Top 1 (concello · prov. · n · %) | Top 2 | Top 3 |\n|---|---|---|---|---|---|---|---|---|')
for d in D:
    t=[f"{x['concello']} · {x['provincia']} · {n(x['n'])} · {pc(x['pct'])}" for x in d['top3']]+['—']*3
    name='**CONTROL: Rodríguez**' if d['apellido'].endswith('CONTROL') else d['apellido']
    w(f"| {name} | {d['forma_consultada'] or '(vacía)'} | {n(d['ocorrencias'])} | {pc(d['porcentaxe'])} | {d['posicion']} | {d['concellos']} | {t[0]} | {t[1]} | {t[2]} |")
w('')
zero=[d['apellido'] for d in D if d['ocorrencias']==0]
low=[f"{d['apellido']} ({d['ocorrencias']})" for d in D if 0<d['ocorrencias']<50]
w(f'**Ausencias (el control pasó, así que son reportables):** {", ".join(zero) or "ninguna"}. Consultado: «lucatti» → 0 ocorrencias, 0 concellos. Es la única ausencia.\n')
w(f'**Frecuencia muy baja (<50):** {", ".join(low)}. Con cifras tan chicas, el porcentaje por concello es muy sensible a 1-2 personas.\n')
w('**Alcance:** la Cartografía cuenta portadores del apellido en Galicia. No dice nada sobre el origen de cada familia ni sobre quién lo lleva fuera de Galicia.')
open('COSECHA2_cartografia.md','w').write('\n'.join(o)+'\n')
