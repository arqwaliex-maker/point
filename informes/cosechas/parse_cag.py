import re,html,os,json
names=['Rodríguez_CONTROL']+[l.strip() for l in open('names.txt') if l.strip()]
out=[]
for n in names:
    f=f'cag/{n}.html'
    if not os.path.exists(f): out.append(dict(apellido=n,estado='PENDIENTE')); continue
    s=open(f,encoding='utf8',errors='ignore').read()
    t=re.sub(r'<script.*?</script>|<style.*?</style>','',s,flags=re.S)
    t=html.unescape(re.sub(r'<[^>]+>',' ',t)); t=re.sub(r'\s+',' ',t)
    m=re.search(r'APELIDO: --> (.+?) en Galicia Número de ocorrencias: (\d+) Porcentaxe: ([^ ]+) Posición: (\S+) Número de concellos: (\d+) Concello Provincia Nº de apelidos Porcentaxe (.*?)(?: Descargar resultados|$)',t)
    if not m: out.append(dict(apellido=n,estado='NO SE PUDO LEER', raw=t[t.find('APELIDO'):t.find('APELIDO')+200])); continue
    rows=re.findall(r'(.+?) (A Coruña|Lugo|Ourense|Pontevedra) (\d+) ([\d.E-]+%)\s*',m.group(6))
    top=[dict(concello=c.strip(),provincia=p,n=int(k),pct=v) for c,p,k,v in rows[:3]]
    out.append(dict(apellido=n,forma_consultada=m.group(1),ocorrencias=int(m.group(2)),porcentaxe=m.group(3),posicion=m.group(4),concellos=int(m.group(5)),top3=top,estado='OK'))
json.dump(out,open('cag_parsed.json','w'),ensure_ascii=False,indent=0)
for o in out[:6]+[o for o in out if o['estado']!='OK'][:5]: print(o)
