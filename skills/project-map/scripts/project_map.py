"""Génère ou met à jour .kilo/PROJECT_MAP.md (arborescence compacte).
Usage : py project_map.py [--depth 3] [--root .]"""
import argparse, os, re

EXCLUDE = {".git", "node_modules", "dist", "build", "coverage", ".venv", "venv", "__pycache__",
           "playwright-report", "test-results", "screenshots", ".next", ".cache", ".idea", ".vscode"}
EXCLUDE_EXT = {".png", ".jpg", ".jpeg", ".gif", ".zip", ".lock", ".log", ".map", ".pdf", ".ico"}

def count_lines(path):
    try:
        with open(path, "rb") as f:
            return sum(1 for _ in f)
    except OSError:
        return 0

def tree(root, depth):
    out = []
    def walk(d, level):
        try:
            entries = sorted(os.scandir(d), key=lambda e: (not e.is_dir(), e.name.lower()))
        except OSError:
            return
        for e in entries:
            if e.name in EXCLUDE or (e.name.startswith(".") and e.name not in {".kilo", ".github"}):
                continue
            ind = "  " * level
            if e.is_dir():
                out.append(f"{ind}- {e.name}/")
                if level + 1 < depth:
                    walk(e.path, level + 1)
            elif os.path.splitext(e.name)[1].lower() not in EXCLUDE_EXT and "lock" not in e.name:
                out.append(f"{ind}- {e.name} ({count_lines(e.path)} l.)")
    walk(root, 0)
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--depth", type=int, default=3); ap.add_argument("--root", default=".")
    a = ap.parse_args()
    auto = "<!-- AUTO:START -->\n## Arborescence\n" + "\n".join(tree(a.root, a.depth)) + "\n<!-- AUTO:END -->"
    path = os.path.join(a.root, ".kilo", "PROJECT_MAP.md")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if os.path.exists(path):
        old = open(path, encoding="utf-8").read()
        new = re.sub(r"<!-- AUTO:START -->.*?<!-- AUTO:END -->", lambda m: auto, old, flags=re.S)
        if new == old and "AUTO:START" not in old:
            new = old + "\n\n" + auto
    else:
        new = ("# Carte du projet\n\n## Rôle des dossiers\n- [À compléter]\n\n"
               "## Commandes\n- Installation : [À compléter]\n- Tests : [À compléter]\n\n" + auto + "\n")
    open(path, "w", encoding="utf-8").write(new)
    print(f"{path} : {new.count(chr(10))} lignes")

if __name__ == "__main__":
    main()
