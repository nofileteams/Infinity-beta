from pathlib import Path
import os

Path("main.txt").open("w", encoding="UTF-8").write(os.getcwd())
log = input("install library? y/n")
if log != "n":
	os.system(pip3 install -r requirement.txt)
