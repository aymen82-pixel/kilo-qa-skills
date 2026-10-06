"""Extrait texte (par page) et tableaux d'un PDF.
Usage : py extract_pdf.py doc.pdf [--pages 1-10] [--out dossier]"""
import argparse, csv, os
import pdfplumber

def parse_pages(spec, n):
    if not spec:
        return range(n)
    a, _, b = spec.partition("-")
    return range(int(a) - 1, min(int(b or a), n))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf"); ap.add_argument("--pages"); ap.add_argument("--out", default="extract")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    with pdfplumber.open(a.pdf) as pdf:
        n = len(pdf.pages)
        print(f"{n} pages")
        empty = 0
        with open(os.path.join(a.out, "texte.md"), "w", encoding="utf-8") as f:
            for i in parse_pages(a.pages, n):
                page = pdf.pages[i]
                text = page.extract_text() or ""
                empty += not text.strip()
                f.write(f"\n\n## Page {i+1}\n\n{text}")
                for k, tbl in enumerate(page.extract_tables(), start=1):
                    p = os.path.join(a.out, f"p{i+1}_table{k}.csv")
                    with open(p, "w", newline="", encoding="utf-8") as c:
                        csv.writer(c, delimiter=";").writerows(tbl)
        if empty:
            print(f"Attention : {empty} page(s) sans texte - PDF probablement scanné, OCR nécessaire.")
    print(f"Sortie dans {a.out}/")

if __name__ == "__main__":
    main()
