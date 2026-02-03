
import argparse
from pathlib import Path
from cornell_seyes import build_actief_leren_pdf, build_wiskunde_pdf

def main():
    outSeyes = Path("output/cornell-seyes.pdf").resolve()
    outCarre = Path("output/cornell-carre.pdf").resolve()
    outSeyes.parent.mkdir(parents=True, exist_ok=True)
    build_actief_leren_pdf(str(outSeyes))
    build_wiskunde_pdf(str(outCarre))

if __name__ == "__main__":
    main()
