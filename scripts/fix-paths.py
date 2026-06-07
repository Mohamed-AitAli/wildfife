from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
for path in root.rglob("*.html"):
    if "wordpress" in path.parts:
        continue
    text = path.read_text(encoding="utf-8")
    updated = text.replace('src="img\\', 'src="img/').replace("src='img\\", "src='img/")
    updated = updated.replace('href="guides\\', 'href="guides/').replace('href="builds\\', 'href="builds/')
    if updated != text:
        path.write_text(updated, encoding="utf-8")
        print(path.relative_to(root))
