# See tags your interpreter supports
import sys, pkgutil
print(sys.version); import pip; print(pip.__version__)
import pip._internal.models.format_control as fc
import pip._internal.models.target_python as tp
print(tp.TargetPython().get_tags()[:5])  # top 5 tags

# Inspect wheel metadata (it’s just a zip)
import zipfile, sys
w = sys.argv[1] if len(sys.argv)>1 else 'some.whl'
with zipfile.ZipFile(w) as z:
    for p in z.namelist():
        if p.endswith(('METADATA','WHEEL','RECORD')):
            print('---', p, '---'); print(z.read(p).decode()[:500])
