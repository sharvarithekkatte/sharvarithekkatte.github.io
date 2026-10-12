import re,json,base64,gzip,sys,os
src=open(sys.argv[1]).read(); out=sys.argv[2]
def block(t):
    m=re.search(r'<script type="__bundler/%s">(.*?)</script>'%t,src,re.S); return m.group(1) if m else None
man=json.loads(block('manifest')); tpl=json.loads(block('template'))
print('page_order',block('page_order')); print('ext',(block('ext_resources') or '')[:500])
open(os.path.join(out,'template.html'),'w').write(tpl)
for u,e in man.items():
    b=base64.b64decode(e['data'])
    if e.get('compressed'): b=gzip.decompress(b)
    open(os.path.join(out,u),'wb').write(b); print(u,e['mime'],len(b))
