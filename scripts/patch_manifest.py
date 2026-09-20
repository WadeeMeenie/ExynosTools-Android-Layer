import json
import sys
from pathlib import Path

p = Path(sys.argv[1])
data = json.loads(p.read_text(encoding="utf-8"))
layer = data["layer"]
layer["name"] = "VK_LAYER_EXYNOSTOOLS_bcn"
layer["library_path"] = "libVkLayer_ExynosTools.so"
p.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
