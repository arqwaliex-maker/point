import json,re
d=json.load(open('vaciado.json')); R=d['res']; FOOT=d['foot']
NAMES=[l.strip() for l in open('../c2/names.txt') if l.strip()]
def tipo(r):
    f=r['frase']; a=r['apellido']; p=r['pagina']
    if 'patronymics that were then predominant' in f: return 'LISTA — nombrado en la lista de patronímicos predominantes (s. XIII)'
    if 'Garcia Carraffa' in f: return 'NO ES MENCIÓN — nombre del autor citado (García Carraffa)'
    if 'Lopez de la Mesa' in f: return 'NO ES MENCIÓN — nombre del autor citado (Luis López de la Mesa); la nota 6 va con la frase de los Mediomundos'
    for k,v in [('Castillo Sol','persona citada (Castillo Solórzano, novelista)'),('Guillen de Castro','persona citada (Guillén de Castro, dramaturgo)'),
                ('San Juan de la Cruz','persona citada (San Juan de la Cruz)'),('Tirso de Molina','persona citada (Tirso de Molina)'),
                ('Fernando de Rojas','persona citada (Fernando de Rojas)'),('siege of Cordoba','topónimo (Córdoba, ciudad)'),
                ('Vega de Granada','topónimo (Vega de Granada)'),('Garcia VI','persona (García VI de Navarra) — nombre de pila'),
                ('Garcia Jimenez','persona (García Jiménez) — García como nombre de pila'),('Garcia Ifiiquez','persona (García Íñiguez) — García como nombre de pila')]:
        if k in f: return 'NO ES MENCIÓN DEL APELLIDO COMO TEMA — '+v
    if a in ('Flores','Moreno','Rojas','Rodríguez') or (a,p) in (('Sánchez',139),('Sánchez',162),('Díaz',139),('Pérez',139),('López',139)):
        return 'TEMA — el apellido es objeto de la afirmación'
    return 'PERSONA — apellido de un personaje citado como ejemplo'
EXTRA=[ # found by word-boundary grep, missed by the tolerant regex
 dict(apellido='Vázquez',forma='Vasquez',pagina=139,frase=R[25]['frase'],notas=[],cursiva=False,T='LISTA — nombrado en la lista de patronímicos predominantes (s. XIII); grafía «Vasquez»'),
 dict(apellido='Giménez',forma='Jimenez',pagina=162,frase='One of the first Amados was the Goth, Don Alvaro, who was called "EI amado" by Garcia Jimenez as a token of his extreme fondness for him.',notas=[],cursiva=False,T='PERSONA — grafía «Jimenez», no «Giménez»; es el nombre de un personaje (García Jiménez)'),
 dict(apellido='Paz',forma='paz',pagina=163,frase='Those who can establish links with the noble paz family will find the eponym in the persons of the grandson of Alfonso el Sabio, so named in recognition for having brought peace to Spain through his victories over the Moors.',notas=[],cursiva=False,T='TEMA — casa nobiliaria (ver aclaración)'),
 dict(apellido='Godoy',forma='Godoy',pagina=160,frase='8 A list copied from Jose Godoy Alcantara\'s Ensayo sobre los apellidos expafioles in the Garcia Carraffa Enciclopedia. . . Vol. XXXV, p. 57.',notas=[8],cursiva=False,T='NO ES MENCIÓN — nombre del autor citado en la nota 8 (José Godoy Alcántara)'),
]
rows=[]
for r in R: r=dict(r); r['T']=tipo(r); rows.append(r)
rows+=EXTRA
order={n:i for i,n in enumerate(NAMES)}
rows.sort(key=lambda r:(order.get(r['apellido'],999),r['pagina']))
seen=set(); out=[]
w=out.append
w('# COSECHA 3 · Fucilla 1978 — vaciado de los 90 apellidos\n')
w('## 0. Fuente y método\n')
w('| Campo | Valor |\n|---|---|')
w('| Obra | Joseph G. Fucilla, «Spanish Nicknames as Surnames», *Names* 26(2), 1978, pp. 139-176. DOI 10.1179/nam.1978.26.2.139 |')
w('| Archivo | `https://ans-names.pitt.edu/ans/article/download/874/873` (PDF, 3.554.656 bytes, 38 págs.; pág. PDF 1 = p. 139) |')
w('| robots.txt | ans-names.pitt.edu: solo prohíbe `/cache/` → permitido |')
w('| Texto | **Capa OCR del PDF escaneado** (pdftotext). Las citas reproducen el OCR tal cual: «L6pez» = López, «fi/ii» = ñ, «6» = ó, «ti» = á. **Cotejar cada cita con el facsímil antes de imprimir.** |')
w('| Cursiva | Detectada con `pdftohtml -xml` (`<i>`). Nota 1 de Fucilla: la cursiva marca apellidos de la nobleza según García Carraffa |')
w('| Búsqueda | Regex tolerante al OCR (acentos, ñ) + control por palabra completa (que agregó Vasquez, Jimenez, paz, Godoy) |')
w('| Tipos | TEMA = el apellido es objeto de lo que se dice · LISTA = aparece en la lista de p. 139 · PERSONA = apellido de un personaje · NO ES MENCIÓN = nombre de autor, topónimo o nombre de pila |')
w('')
w('## 1. Apariciones (una fila por frase)\n')
w('| Apellido | Forma OCR | Pág. | Tipo | Cursiva | Nota | Frase textual (OCR) |\n|---|---|---|---|---|---|---|')
for r in rows:
    f=r['frase'].replace('|','/')
    if len(f)>400: f=f[:400]+' […]'
    w(f"| {r['apellido']} | {r['forma']} | {r['pagina']} | {r['T']} | {'sí' if r['cursiva'] else 'no'} | {', '.join(map(str,r['notas'])) or '—'} | «{f}» |")
w('')
w('## 2. Párrafos completos de las menciones TEMA (textual, OCR)\n')
w('| Apellido | Pág. | Párrafo |\n|---|---|---|')
done=set()
for r in rows:
    if r['T'].startswith('TEMA') and 'parrafo' in r:
        k=r['parrafo'][:80]
        if k in done: continue
        done.add(k)
        w(f"| {r['apellido']} | {r['pagina']} | «{r['parrafo'].strip().replace('|','/')}» |")
w("| Paz | 163 | «Individuals who have reason to claim descent from the noble Leal (loyal) family may be acquainted with the legend that tells of a granger, a partisan of Peter the Cruel, who refused to give lodging to the latter's enemy, Enrique II. Enrique took revenge by having him hanged from a turret on the grange. The gibbetted victim was referred to as Leal, which became the surname of his offspring. Those who can establish links with the noble paz family will find the eponym in the persons of the grandson of Alfonso el Sabio, so named in recognition for having brought peace to Spain through his victories over the Moors.» |")
w('')
w('## 3. Notas al pie (transcripción textual, OCR)\n')
w('| Nota | Pág. | Texto | Afecta a |\n|---|---|---|---|')
AF={'1':'Todo el artículo (criterio de cursiva = nobleza; fuente = García Carraffa)','5':'Frase «Ojos verdes…» (no a Rojas)','6':'Frase de los Mediomundos (no a López)','8':'Flores (las 40 variantes)'}
for k in sorted(FOOT,key=int):
    w(f"| {k} | {FOOT[k]['page']} | «{FOOT[k]['text']}» | {AF.get(k,'ninguno de los 90')} |")
w('')
w('## 4. Aclaraciones obligatorias\n')
w('| Punto | Aclaración |\n|---|---|')
w('| Casas nobiliarias (Flores p.160, Moreno p.147-148, Paz p.163) | Fucilla habla de familias nobles y de sus orígenes legendarios, basándose en García Carraffa (nota 1). **Eso no dice nada sobre quien lleva hoy el apellido.** Un apellido no prueba ascendencia. |')
w('| Moreno p.148 | Fucilla mismo califica de ficticia («fictitious») la descendencia romana de Mucius Murena. |')
w('| Moreno p.147 | «Moreno» aparece en cursiva en la lista de colores. Según la nota 1, la cursiva marca un apellido de la nobleza en García Carraffa. El texto lo da como apellido de color: «brown, brunette». No sugiere nada sobre las personas que lo llevan. |')
w('| Sánchez p.139 | Se transcribe literal: «Sanchez is the Latin word for saint». La afirmación es de Fucilla; este informe no la verificó. |')
w('| Flores p.160 | Fucilla deriva Flores de «Froylaz or Frolaz (eleventh century)», de Fruela. La nota 8 remite a una lista de Godoy Alcántara copiada en García Carraffa, vol. XXXV, p. 57. En la Cosecha 1, el Becerro Galicano da formas en Froila-/Froyla- (ver ese bloque). |')
w('| Paz p.163 | En el OCR, «paz» sale en minúscula y sin cursiva. Por la nota 1 se esperaría cursiva: verificar en el facsímil. |')
w('')
w('## 5. Apellidos sin mención\n')
hit={r['apellido'] for r in rows if not r['T'].startswith('NO ES MENCIÓN')}
nohit=[n for n in NAMES if n not in hit]
only=[n for n in NAMES if n in {r['apellido'] for r in rows} and n not in hit]
w(f'**Sin ninguna aparición real ({len(nohit)}):** '+', '.join(nohit)+'.\n')
w('Buscado: la forma del apellido sin tilde, con tilde y con las variantes de OCR (ñ→fi/ii/n, ó→6, á→ti, í→i/1/l), por palabra completa en las 38 páginas.')
w(f'\nDe ellos, **aparecen solo como no-mención** (autor, topónimo, nombre de pila): {", ".join(only)}.')
open('COSECHA3_fucilla.md','w').write('\n'.join(out)+'\n')
print(len(rows),len(nohit),only)
