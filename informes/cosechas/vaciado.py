import re,html,json,unicodedata
names=[l.strip() for l in open('../c2/names.txt') if l.strip()]
PAGES=38; OFF=138
# --- footnotes and bodies from layout text
foot={}; body=[]
for p in range(1,PAGES+1):
    L=open(f'p{p}.txt',encoding='utf8',errors='ignore').read().split('\n')
    # drop running header line (page number + title/author)
    if L and re.search(r'(Fucilla|Spanish Nicknames as Surnames)',L[0]) and p>1: L=L[1:]
    # locate footnote block: first line (after line 25) matching "  N Capital"
    fi=None
    for i,l in enumerate(L):
        if i>20 and re.match(r'^\s{0,8}\d{1,3}\s+\S',l) and not re.match(r'^\s*\d{3}\s*$',l):
            fi=i; break
    bl=L[:fi] if fi is not None else L
    # drop bottom page number line
    bl=[l for l in bl if not re.match(r'^\s*\d{3}\s*$',l)]
    if fi is not None:
        cur=None
        for l in L[fi:]:
            m=re.match(r'^\s{0,8}(\d{1,3})\s+(.*)',l)
            if m and (cur is None or int(m.group(1))==cur+1):
                cur=int(m.group(1)); foot[cur]=dict(page=p+OFF,text=m.group(2).strip())
            elif cur is not None and l.strip() and not re.match(r'^\s*\d{3}\s*$',l):
                foot[cur]['text']+=' '+l.strip()
    for l in bl: body.append((p+OFF,l))
# --- paragraphs
paras=[]; cur=[]
for pg,l in body:
    if re.match(r'^ {2,6}\S',l) and cur:   # indented first line = new paragraph
        paras.append(cur); cur=[]
    if l.strip()=='' :
        continue
    cur.append((pg,l.strip()))
if cur: paras.append(cur)
def ptext(par):
    t=''
    for _,l in par:
        if t.endswith('-') and l[:1].islower(): t=t[:-1]+l
        else: t+=(' ' if t else '')+l
    return t
P2=[dict(pages=sorted(set(pg for pg,_ in par)),text=ptext(par),lines=par) for par in paras]
# --- italics per page from XML
x=open('fuc.xml',encoding='utf8',errors='ignore').read()
ital={}
for pm in re.finditer(r'<page number="(\d+)".*?</page>',x,re.S):
    pn=int(pm.group(1))+OFF
    ital[pn]=[html.unescape(re.sub(r'<[^>]+>','',m)) for m in re.findall(r'<i>(.*?)</i>',pm.group(0))]
def rx(name):
    s=''
    for ch in name:
        c=ch
        m={'á':'(?:á|a|ti)','é':'(?:é|e)','í':'(?:í|i|1|l)','ó':'(?:ó|o|6)','ú':'(?:ú|u)','ñ':'(?:ñ|n|fi|ii|ni)','ü':'(?:ü|u)','Á':'(?:Á|A)'}.get(c)
        s+=m if m else re.escape(c)
    return re.compile(r'(?<![A-Za-z])'+s+r'(?![a-z])')
res=[]
for n in names:
    r=rx(n)
    for par in P2:
        for m in r.finditer(par['text']):
            t=par['text']
            # sentence
            a=max(t.rfind('. ',0,m.start()),t.rfind('? ',0,m.start()),t.rfind('! ',0,m.start())); a=0 if a<0 else a+2
            b=[i for i in (t.find('. ',m.end()),t.find('? ',m.end())) if i>=0]; b=min(b)+1 if b else len(t)
            sent=t[a:b]
            # page of match: find line containing token
            pg=None; acc=''
            for p_,l in par['lines']:
                if r.search(l): pg=p_; break
            if pg is None: pg=par['pages'][0]
            # footnote markers in paragraph
            marks=sorted(set(int(k) for k in re.findall(r'(?<=[a-z\.\,;:\)"\'])(\d{1,2})(?=[\s\.,;:]|$)',t) if int(k) in foot))
            it=any(r.search(s) for s in ital.get(pg,[]))
            res.append(dict(apellido=n,forma=m.group(0),pagina=pg,paginas_parrafo=par['pages'],frase=sent,parrafo=t,notas=marks,cursiva=it))
json.dump(dict(res=res,foot=foot),open('vaciado.json','w'),ensure_ascii=False,indent=0)
from collections import Counter
c=Counter(x['apellido'] for x in res)
print(len(res),'apariciones;',len(c),'apellidos'); print(sorted(c.items(),key=lambda x:-x[1]))
print('sin aparición:',[n for n in names if n not in c])
print('notas:',{k:v['page'] for k,v in foot.items()})
