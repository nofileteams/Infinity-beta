import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("file", help="stop")

args = parser.parse_args()

file = args.file
if Path(file).exists() == True:
	print(Path(file).read_text(encoding="UTF-8"))
