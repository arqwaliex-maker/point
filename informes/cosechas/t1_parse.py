import re,html,sys
PROVS=None
def parse(fn):
    t=open(fn,encoding='utf8',errors='replace').read()
    t=re.sub(r'<script.*?</script>|<style.*?</style>','',t,flags=re.S)
    x=html.unescape(re.sub(r'<[^>]+>',' | ',t)); x=re.sub(r'(\s*\|\s*)+',' | ',x); x=re.sub(r'\s+',' ',x)
    m=re.search(r'Apellido: (.*?) \| Descargar como.*?Por mil \(‰\) \| (Total \| [\d.]+ \| .*?) \| (?:Mapa de frecuencia|NOTAS)',x,re.S)
    if not m: return None, x[x.find('Resultados'):x.find('Resultados')+400]
    cells=m.group(2).split(' | ')
    rows=[cells[i:i+7] for i in range(0,len(cells)-6,7)]
    return dict(apellido=m.group(1).strip(),rows=rows), None
if __name__=='__main__':
    d,e=parse(sys.argv[1]); print(e or d['rows'][:3], len(d['rows']) if d else '')
