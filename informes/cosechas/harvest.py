import json,re,csv,unicodedata
exec(open('forms.py').read())
D=json.load(open('docs2.json'))
def strip(s): return ''.join(c for c in unicodedata.normalize('NFD',s) if unicodedata.category(c)!='Mn' or c=='̃')
def rx(form):
    f=form.lower(); out=''; i=0
    ACC={'á':'a','é':'e','í':'i','ó':'o','ú':'u','ü':'u'}
    while i<len(f):
        c=f[i]; c=ACC.get(c,c); nxt=f[i+1] if i+1<len(f) else ''
        if f[i:i+2]=='nn': out+='(?:nn|ñ)'; i+=2; continue
        if c=='ñ': out+='(?:ñ|nn)'
        elif c=='v': out+='[vub]'
        elif c=='b': out+='[bv]'
        elif c=='u' and nxt in 'aeiou' and nxt: out+='[uv]'
        elif c in 'zç': out+='[zç]'
        elif c=='y': out+='[yi]'
        elif c=='a': out+='[aá]'
        elif c=='e': out+='[eé]'
        elif c=='i': out+='[ií]'
        elif c=='o': out+='[oó]'
        elif c==' ': out+=r'\s+'
        else: out+=re.escape(c)
        i+=1
    return r'(?<![\wçñ])'+out+r'(?![\wçñ])'
GEN_SANTO=r'(?:sancti|sancte|sancto|sanctum|sanctorum|beati|sci)\s+$'
AMBIG={'pero':'en textos romances puede ser la conjunción «pero»','diez':'en textos romances puede ser el numeral «diez»','vera':'puede ser el adjetivo latino «vera»','rio':'palabra común «río» en romance','costa':'palabra común','moral':'palabra común «moral» (árbol)'}
def sentence(t,a,b):
    s=max(t.rfind('. ',0,a),t.rfind('; ',0,a)); s=0 if s<0 else s+2
    e1=[x for x in (t.find('. ',b),t.find('; ',b)) if x>=0]; e=min(e1)+1 if e1 else len(t)
    pre='…' if a-s>350 else ''; post='…' if e-b>350 else ''
    s=max(s,a-350); e=min(e,b+350)
    return (pre+t[s:e]+post).strip()
def year(d):
    m=re.search(r'(\d{3,4})',d['fcrit']); return int(m.group(1)) if m else 9999
rows=[]
patterns={}
for sur,fam in F.items():
    for kind,forms in fam.items():
        for fo in forms:
            patterns.setdefault(sur,[]).append((kind,fo,re.compile(rx(fo),re.I)))
Nre={sur:[re.compile(rx(f),re.I) for f in F[sur].get('N',[])] for sur in F}
EXTRA={'Iohannis','Iohannes','Iohanne','Ioan','Iuan','Iohan','Johan','Don','Domnus','Dompnus','Martin','Pedro','Peidro','Gonzalvo','Garcia','Garsia','Garci','Diag','Diago','Lop','Lope','Roi','Fortun','Michael','Blasco','Tello','Oveco','Beila','Nunno','Nunnu','Munnio','Monnio','Sancio','Sancho','Didaco','Alvaro','Gomiz','Semeno','Eximino','Ferrando','Fredinando','Dominico','Domingo','Rodrigo','Gutier','Pelagius','Pelayo','Vela','Enneco','Galindo','Aznar','Iulian','Bartolome','Vicent','Stephanus','Esteban','Maria','Mari','Urraca','Toda','Tota','Sancia','Oria'}
ALLN=[re.compile(rx(f).replace('(?<![\\wçñ])','').replace('(?![\\wçñ])',''),re.I) for sur in F for f in F[sur].get('N',[])]
NreW={sur:[re.compile(rx(f).replace('(?<![\\wçñ])','').replace('(?![\\wçñ])',''),re.I) for f in F[sur].get('N',[])] for sur in F}
for d in D:
    t=d['text']
    for sur,pl in patterns.items():
        seen=set()
        for kind,fo,cre in pl:
            for m in cre.finditer(t):
                if (m.start(),m.end()) in seen: continue
                seen.add((m.start(),m.end()))
                pre=t[max(0,m.start()-25):m.start()]
                if kind=='P' and fo in ('martini','lupi','roderici','didaci','sancii','alvari','garsie','garcie','gundisalvi','gundissalvi','gondissalvi','ranimiri','ramiri','fredenandi','fredinandi','ferrandi','fernandi','suerii','poncii','menendi','froilani','benedicti') and re.search(GEN_SANTO,pre.lower()):
                    continue
                w=m.group(0)
                if sur=='Castillo' and w in ('Castella','Castiella','Castelle','Castela'): continue  # Castilla (región), no 'castillo'
                sent=sentence(t,m.start(),m.end())
                if kind=='P':
                    FIL=r'(?:fili[uoa]s?|filie|fijo|fija|fiio|fiia)'
                    after=t[m.end():m.end()+60]; before=t[max(0,m.start()-110):m.start()]
                    okA=False
                    ma=re.match(r'[\s,]*(?:\w+\s+){0,2}'+FIL+r'\s+(?:de\s+|domni\s+|dompni\s+|don\s+)?(\w+)',after,re.I)
                    if ma and any(r.fullmatch(ma.group(1)) for r in NreW[sur]): okA=True
                    okB=False
                    for wm in re.finditer(r'\w+',before):
                        if any(r.fullmatch(wm.group(0)) for r in NreW[sur]) and re.match(r'\w+[^.;]{0,40}\b(?:suo|suus|sua|su)\s+'+FIL+r'\s+(?:\w+\s+){0,2}$',before[wm.start():],re.I):
                            okB=True; break
                    okC=False
                    if re.match(r'[\s,]*(?:suus|suo|su)\s+'+FIL+r'|[\s,]*'+FIL+r'\s+(?:eius|suus)',after,re.I):
                        mc=[x for x in re.finditer(r'(\w+)',t[max(0,m.start()-90):m.start()]) if any(r.fullmatch(x.group(1)) for r in NreW[sur])]
                        if mc: okC=True
                    if okA or okB or okC: cls='FILIACIÓN — el texto nombra explícitamente al padre con el nombre de pila correspondiente («filius/filio/fijo» en la misma cláusula)'
                    else: cls='INDETERMINADO — forma patronímica; en estos siglos suele marcar filiación, pero el documento no nombra al padre ni muestra que el nombre se herede'
                    if sur=='Ruiz': cls+=' (Roiz/Ruiz es también contracción de Rodríguez)'
                elif kind=='N':
                    cls='NO ES APELLIDO — nombre de pila (o nombre de pila en genitivo)'
                    if sur in('Arias','García','Ponce','Roldán','Moreno'): cls+='; el apellido moderno coincide con este nombre de pila'
                else:
                    before=t[max(0,m.start()-40):m.start()]
                    prevw=re.search(r'(\w+)[\s,]*$',t[max(0,m.start()-30):m.start()])
                    prevw=prevw.group(1) if prevw else ''
                    if w[0].isupper() and prevw and (prevw in EXTRA or any(r.fullmatch(prevw) for r in ALLN)):
                        cls='INDETERMINADO — va inmediatamente detrás de un nombre de pila: funciona como segundo nombre de esa persona (sobrenombre, patronímico o nombre de familia); el texto no permite saber si se hereda'
                    elif re.search(r'\bde\s+$',before):
                        cls='INDETERMINADO — «de + nombre»: puede indicar procedencia, señorío, propiedad o una persona; el texto no lo decide'
                    elif w[0].isupper(): cls='NO ES APELLIDO — topónimo o nombre propio de lugar'
                    else: cls='NO ES APELLIDO — palabra común'
                if re.search(r'(?:sancti|sancte|sancto|sanctum|sancta|sanctorum|sancte|beati|beate|sci|san|santa|sant|sancta\s+maria\s+et)\s+$',t[max(0,m.start()-25):m.start()].lower()):
                    cls='NO ES APELLIDO — advocación de santo, iglesia o monasterio (precedido de sanctus/sancta/san)'
                if fo in AMBIG: cls+=f' [ATENCIÓN: {AMBIG[fo]}]'
                flags=' || '.join(f"{src}: «{txt}»" for src,txt in d['flags'])
                rows.append(dict(apellido=sur,familia={'P':'patronímico','N':'nombre de pila','T':'topónimo / palabra común / forma del apellido'}[kind],forma_buscada=fo,forma_textual=w,doc=d['num'],url=f"https://www.ehu.eus/galicano/id{d['num']}",fecha_critica=d['fcrit'],fecha_codice=d['fcod'],folio=d['loc'],frase=sent,clasificacion=cls,advertencia_edicion=flags,anio=year(d)))
rows.sort(key=lambda r:(r['apellido'],r['anio'],r['doc']))
with open('becerro_90_apariciones.csv','w',newline='',encoding='utf-8') as fh:
    wr=csv.DictWriter(fh,fieldnames=[k for k in rows[0] if k!='anio']); wr.writeheader()
    for r in rows: wr.writerow({k:v for k,v in r.items() if k!='anio'})
json.dump(rows,open('rows.json','w'),ensure_ascii=False)
from collections import Counter
c=Counter(r['apellido'] for r in rows)
print(len(rows)); print(sorted(c.items(),key=lambda x:-x[1])[:40]); print('sin apariciones:',[s for s in F if s not in c])
