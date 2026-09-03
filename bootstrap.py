import os
import json
import re
import subprocess
from pathlib import Path


def replace(text,key,value):
    pattern=rf"(?m)^{re.escape(key)}\s*=.*$"
    line=f"{key} = {value}"
    return re.sub(pattern,line,text,count=1) if re.search(pattern,text) else text+"\n"+line+"\n"


root=Path("/MoneyPrinterTurbo")
example=root/"config.example.toml"
target=root/"config.toml"
if not example.exists(): raise RuntimeError("MoneyPrinterTurbo config.example.toml was not found")
pexels=os.environ.get("PEXELS_API_KEY","").strip()
if not pexels: raise RuntimeError("PEXELS_API_KEY is required")
text=example.read_text(encoding="utf-8")
text=replace(text,"listen_host",'"0.0.0.0"')
text=replace(text,"listen_port",str(int(os.environ.get("PORT","8080"))))
text=replace(text,"video_source",'"pexels"')
text=replace(text,"pexels_api_keys",json.dumps([pexels]))
api_key=os.environ.get("MPT_API_KEY","").strip()
if api_key: text=replace(text,"api_key",json.dumps(api_key))
target.write_text(text,encoding="utf-8")
subprocess.run(["python","main.py"],cwd=root,check=True)
