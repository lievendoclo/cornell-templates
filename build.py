
import argparse
from pathlib import Path
from cornell_seyes import build_actief_leren_pdf

def main():
    parser = argparse.ArgumentParser(description="Build Cornell/Seyès PDF templates.")
    parser.add_argument("-o", "--output", default="output.pdf")
    args = parser.parse_args()

    out = Path(args.output).resolve()
    out.parent.mkdir(parents=True, exist_ok=True)
    build_actief_leren_pdf(str(out))
    print(f"Generated: {out}")

if __name__ == "__main__":
    main()
