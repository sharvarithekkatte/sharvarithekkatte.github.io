# Re-embed an edited template.html into index.html (bundle from Claude Design export).
# Usage: python3 _tools/repack.py index.html template.html
import re,json,sys
idx,tplf=sys.argv[1],sys.argv[2]
src=open(idx,encoding="utf-8").read(); tpl=open(tplf,encoding="utf-8").read()
m=re.search(r'(<script type="__bundler/template">\s*)(.*?)(\s*</script>)',src,re.S)
new=json.dumps(tpl,ensure_ascii=False).replace('</','<\\u002F')
out=src[:m.start(2)]+new+src[m.end(2):]
open(idx,"w",encoding="utf-8").write(out); print('ok',len(out))
