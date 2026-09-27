import unicodedata,urllib.parse,subprocess,time,os,sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
def q(n):
    n=n.lower()
    out=''
    for ch in n:
        if ch=='ñ': out+='ñ'; continue
        d=unicodedata.normalize('NFD',ch); out+=''.join(c for c in d if unicodedata.category(c)!='Mn')
    return out
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"
names=['Rodríguez_CONTROL']+[l.strip() for l in open('names.txt') if l.strip()]
for n in names:
    base=n.replace('_CONTROL','')
    qq=q(base); url='https://ilg.usc.es/cag/Controlador?busca='+urllib.parse.quote(qq)
    fn=f"cag/{n}.html"
    for attempt in range(3):
        r=subprocess.run(['curl','-sS','-A',UA,'-L','--max-time','40','-o',fn,'-w','%{http_code}',url],capture_output=True,text=True)
        print(n,qq,r.stdout,r.stderr.strip()[:80],flush=True)
        if r.stdout=='200' and os.path.getsize(fn)>5000: break
        time.sleep(10)
    time.sleep(10)
open('cag/DONE','w').write('ok')
