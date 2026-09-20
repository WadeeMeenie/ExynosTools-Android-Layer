from pathlib import Path
import sys

root = Path(sys.argv[1])
p = root / "src/layer/layer_entry.cpp"
s = p.read_text(encoding="utf-8")
s = s.replace("VK_LAYER_VORTEK_XCLIPSE", "VK_LAYER_EXYNOSTOOLS_bcn")
p.write_text(s, encoding="utf-8")

manifest = root / "VkLayer_vortek_xclipse.json.in"
if manifest.exists():
    s = manifest.read_text(encoding="utf-8")
    s = s.replace("VK_LAYER_VORTEK_XCLIPSE", "VK_LAYER_EXYNOSTOOLS_bcn")
    s = s.replace("VkLayer_VortekXclipse", "libVkLayer_ExynosTools")
    manifest.write_text(s, encoding="utf-8")
