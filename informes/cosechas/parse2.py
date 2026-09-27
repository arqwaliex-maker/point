import re,glob,json,html
FLAG=r"fals|apócrif|sospech|dudos|interpol|cuestionab|reemplaz|manipul|espuri|añadid"
docs=[]
for f in glob.glob('../s/tei/*.xml'):
    s=open(f,encoding='cp1252',errors='replace').read()
    webid=int(re.search(r'BGSMC_(\d+)',f).group(1))
    num=re.search(r'<item>Documento ([^<]+)</item>',s); num=num.group(1).strip() if num else '?'
    def lab(name):
        m=re.search(name+r'</label>\s*<item>(.*?)</item>',s,re.S)
        return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>','',m.group(1)))).strip() if m else ''
    fcod=lab('Fecha c.dice'); fcr=lab('Fecha cr.tica'); reg=lab('Regesta'); nfe=lab('Notas fecha')
    loc=re.search(r'<locus[^>]*>([^<]*)</locus>',s); loc=loc.group(1) if loc else ''
    bibl=[re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>','',b))).strip() for b in re.findall(r'<bibl>(.*?)</bibl>',s,re.S)]
    flags=[('Referencias (listBibl)',b) for b in bibl if re.search(FLAG,b,re.I)]
    if nfe and re.search(FLAG,nfe,re.I): flags.append(('Notas fecha',nfe))
    body=s[s.find('<div type="document">'):] if '<div type="document">' in s else ''
    body=re.sub(r'<note[^>]*type="gloss"[^>]*>.*?</note>',' ',body,flags=re.S)
    body=re.sub(r'<note[^>]*/>','',body)
    body=re.sub(r'<[^>]+>','',body)
    body=re.sub(r'\s+',' ',html.unescape(body)).strip()
    body=re.sub(r'(\w)-\s+-(\w)',r'\1\2',body)   # une palabras partidas por renglón ("Bas- -coniana")
    docs.append(dict(webid=webid,num=num,fcod=fcod,fcrit=fcr,reg=reg,notasfecha=nfe,loc=loc,bibl=bibl,flags=flags,text=body))
json.dump(docs,open('docs2.json','w'),ensure_ascii=False)
print(len(docs), sum(1 for d in docs if d['flags']), 'docs con advertencias')
import collections
print(collections.Counter(d['num'].endswith('*') for d in docs))
