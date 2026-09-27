import xlrd,json,unicodedata
NAMES=[l.strip() for l in open('../c2/names.txt') if l.strip()]
def key(n):
    n=n.upper().replace('Ñ','\x00')
    n=''.join(c for c in unicodedata.normalize('NFD',n) if unicodedata.category(c)!='Mn')
    return n.replace('\x00','Ñ')
F={}
for s in xlrd.open_workbook('apellidos_frecuencia.xls').sheets():
    for r in range(5,s.nrows):
        v=s.row_values(r)
        if isinstance(v[0],float) and v[1]: F[v[1].strip()]=dict(orden=int(v[0]),ap1=v[2],ap2=v[3],ambos=v[4],hoja=s.name)
b=xlrd.open_workbook('apellidos_mas_frecuentes.xls')
E=b.sheet_by_name('ESPAÑA_100'); ESP={}
for r in range(5,E.nrows):
    v=E.row_values(r)
    if v[1]: ESP[v[1].strip()]=dict(orden=int(v[0]),n=v[2],x1000=v[3])
P=b.sheet_by_name('PROVINCIAS_RESIDENCIA')
h3=P.row_values(3); h4=P.row_values(4)
groups=[(c,h3[c]) for c in range(P.ncols) if h4[c]=='PRIMER APELLIDO']
PROV={}  # prov -> {ap: (orden,n,x1000)}, and min x1000 (50th)
for c,prov in groups:
    d={}
    for r in range(5,P.nrows):
        v=P.row_values(r)
        if isinstance(v[0],float) and v[c]: d[v[c].strip()]=(int(v[0]),v[c+1],v[c+2])
    PROV[prov]=d
print(len(groups),'provincias', len(F),'apellidos')
out=[]
for n in NAMES:
    k=key(n); f=F.get(k)
    listed=sorted([(p,)+d[k] for p,d in PROV.items() if k in d],key=lambda x:-x[3])
    # bound: max over provinces where NOT listed of that province's 50th x1000
    bound=max([min(t[2] for t in d.values()) for p,d in PROV.items() if k not in d],default=0)
    top=listed[:3]
    seguro = len(top)==3 and top[2][3]>=bound
    out.append(dict(apellido=n,clave=k,frec=f,esp100=ESP.get(k),prov_listadas=len(listed),top3=top,cota=bound,top3_seguro=seguro))
json.dump(out,open('ine.json','w'),ensure_ascii=False,indent=0)
for o in out: print(o['apellido'],o['clave'],o['frec'] and (o['frec']['orden'],o['frec']['ap1']),o['prov_listadas'],[ (t[0],round(t[3],2)) for t in o['top3']],round(o['cota'],2),o['top3_seguro'])
