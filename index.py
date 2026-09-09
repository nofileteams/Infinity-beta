#You really managed to dig that up, didn't you? But if you have time for that sort of thing, you ought to be finding a partner, getting a job, and earning money instead.
import argparse
import json
import locale
import getpass
import platform
import os
import seedir as sd
import sys
import readchar
from pathlib import Path

main = Path("main.txt").read_text(encoding="UTF-8")
lang = locale.getlocale()[0][:2].lower()
if Path(f"{main}/lang/{lang}.json").exists() == True:
	with open(f"{main}/lang/{lang}.json", "r", encoding="UTF-8") as lang_file:
		file_lang = lang_file.read()
	with open(f"{main}/config.json", "w", encoding="UTF-8") as lang_file:
		lang_file.write(file_lang)

with open(f"{main}/config.json", "r", encoding="UTF-8") as json_file:
	data = json.loads(json_file.read())

if os.name == "nt":
	data["logo"] = "⊞"
else:
	if platform.system().lower() == "darwin":
		data["logo"] = ""
	else:
		data["logo"] = "@"

#os.chdir("/")

angry_mater = 0

data["username"] = getpass.getuser()

parser = argparse.ArgumentParser()
parser.add_argument("-f", default="none", help=data["help"]["file"])
parser.add_argument("-c", default="none", help=data["help"]["command"])
args = parser.parse_args()

sys.stdout.write(f"\x1b]2;{data["title"]}\x07")
sys.stdout.flush()

if args.c != "none" or args.f != "none":
	terminal_mode = False
else:
	terminal_mode = True

exits = False
os_name = f"{platform.system()}{platform.release()}"


with open(f"{main}/cmd/bashrc.sh", "r", encoding="UTF-8") as bashrc_file:
	bashrc = bashrc_file.read().lstrip()



#prompt = f"┌──({data["username"]}{data["logo"]}{os_name})-[{os.getcwd().replace("C:", "").replace("\\", "/")}]\n└─$"
prompt_load = Path(f"{main}/cmd/zsh.rc")

prompt = prompt_load.read_text(encoding="UTF-8").replace("$path$", f"{os.getcwd().replace("C:", "").replace("\\", "/")}").replace("$user$", f"{data["username"]}{data["logo"]}{os_name}")

def command(cmd: str):
	global load_cmd
	global exits
	global counts
	global dirs
	global ascii_liner
	global commands
	global ascii_text
	commands = False
	load_cmd = cmd
	#custom
	if load_cmd.split()[0] == "none" or load_cmd.split()[0] == "cls" or load_cmd.split()[0] == "clear" or load_cmd.split()[0] == "exit" or load_cmd.split()[0] == "ls" or load_cmd.split()[0] == "dir" or load_cmd.split()[0] == "cd" or load_cmd.split()[0] == "chdir" or load_cmd.split()[0] == "bash" or load_cmd.split()[0] == "title" or load_cmd.split()[0] == "pause" or load_cmd.split()[0] == "help" or load_cmd.startswith("./") == True or load_cmd.split()[0] == "secret" or load_cmd.split()[0] == "grep" or load_cmd.split()[0] == "tree":
		if load_cmd.split()[0] == "cls" or load_cmd.split()[0] == "clear":
			if os.name == "nt":
				log = os.system("cls")
			else:
				log = os.system("clear")
		
		if load_cmd.split()[0] == "exit":
			exits = True
			
		if load_cmd.split()[0] == "secret":
			print(data["message"]["secret2"])
		
		if load_cmd.split()[0] == "grep":
			print(data["message"]["grep"])
			
		if load_cmd.split()[0] == "tree":
			arg = load_cmd.replace(load_cmd.split()[0], "", 1).lstrip()
			counts = 0
			if arg != "":
				if os.path.exists(arg) == True:
					print(data["message"]["tree"])
					sd.seedir(arg)
				else:
					print(f"{arg}{data["message"]["ls_error"]}")
			else:
				print(data["message"]["tree"])
				sd.seedir()
		
			
		if load_cmd.split()[0] == "help":
			print(Path(f"{main}/cmd/help.txt").read_text(encoding="UTF-8"))
		
		if load_cmd.split()[0] == "pause":
			print(data["message"]["pause"])
			log = readchar.readchar()
			
		if load_cmd.startswith("./") == True:
			arg = load_cmd.replace("./", "", 1).lstrip()
			if arg != "":
				if os.name == "nt":
					log = os.system(arg)
				else:
					log = os.system(f"./{arg}")
			
		
		if load_cmd.split()[0] == "title":
			arg = load_cmd.replace(load_cmd.split()[0], "", 1).lstrip()
			sys.stdout.write(f"\x1b]2;{arg}\x07")
			sys.stdout.flush()
			
		
		if load_cmd.split()[0] == "bash":
			arg = load_cmd.replace(load_cmd.split()[0], "", 1).lstrip()
			if arg != "":
				if Path(arg).suffix == ".sh":
					if Path(arg).exists() == True:
						with open(arg, "r", encoding="UTF-8") as file_load:
							load_file = file_load.read()
						file_lines = load_file.splitlines()
						file_count = 0
						for _ in range(len(file_lines)):
							cmd_load(file_lines[file_count])
							file_count = file_count + 1
					else:
						print(f"{arg}{data["message"]["wrong_file2"]}")
				else:
					print(data["message"]["wrong_file"])
		
		if load_cmd.split()[0] == "cd" or load_cmd.split()[0] == "chdir":
			arg = load_cmd.replace(load_cmd.split()[0], "", 1).replace('"', '').replace("'", "").lstrip().strip()
			if arg != "":
				if os.path.exists(arg) == True:
					os.chdir(arg)
				else:
					print(f"{arg}{data["message"]["cd_error"]}")
			else:
				os.chdir("/")
		
		
		if load_cmd.split()[0] == "ls" or load_cmd.split()[0] == "dir":
			arg = load_cmd.replace(load_cmd.split()[0], "", 1).lstrip().strip()
			counts = 0
			if arg != "":
				if os.path.exists(arg) == True:
					dirs = os.listdir(arg)
					for _ in range(len(dirs)):
						print(dirs[counts])
						counts = counts + 1
				else:
					print(f"{arg}{data["message"]["ls_error"]}")
			else:
				dirs = os.listdir()
				for _ in range(len(dirs)):
					print(dirs[counts])
					counts = counts + 1
				
				
	else:
		if Path(f"{main}/cmd/{load_cmd.split()[0]}.{data["extensions_file"]}").exists() == True:
			if commands == False:
				commands = True
				arg = load_cmd.replace(load_cmd.split()[0], "", 1).lstrip()
				if os.name == "nt":
					log = os.system(f"{main}/cmd/{load_cmd.split()[0]}.{data["extensions_file"]} {arg}")
				else:
					log = os.system(f"./{main}/cmd/{load_cmd.split()[0]}.{data["extensions_file"]} {arg}")
		if Path(f"{main}/cmd/{load_cmd.split()[0]}/index.py").exists() == True:
			if commands == False:
				commands = True
				arg = load_cmd.replace(load_cmd.split()[0], "", 1).lstrip()
				log = os.system(f"{data["execution"]} {main}/cmd/{load_cmd.split()[0]}/index.py {arg}")
				if log == 1:
					print(f"\033[31m{data["message"]["python_error"]}\033[0m")
		
		if Path(load_cmd.split()[0]).suffix != "":
			if Path(load_cmd.split()[0]).exists() == True:
				if commands == False:
					commands = True
					arg = load_cmd.replace(load_cmd.split()[0], "", 1).lstrip().strip()
					if os.name == "nt":
						log = os.system(f"{load_cmd.split()[0]} {arg}")
					else:
						log = os.system(f"./{load_cmd.split()[0]} {arg}")
		
		if commands == False:
			commands = True
			log = os.system(cmd)


def cmd_load(loader: str):
	global cmd
	global cmd_count
	global cmds
	global prompt
	cmd_count = 0
	cmds = loader.lstrip()
	for _ in range(len(cmds.split("&&"))):
		command(cmds.split("&&")[cmd_count])
		prompt = prompt_load.read_text(encoding="UTF-8").replace("$path$", f"{os.getcwd().replace("C:", "").replace("\\", "/")}").replace("$user$", f"{data["username"]}{data["logo"]}{os_name}")
		cmd_count = cmd_count + 1
	

if bashrc != "":
	file_lines = bashrc.splitlines()
	file_count = 0
	for _ in range(len(file_lines)):
		cmd_load(file_lines[file_count])
		file_count = file_count + 1


if terminal_mode == True:
	print("")
	while True:
		try:
			cmd = input(prompt)
			if cmd != "":
				cmd_load(cmd)
			if exits == True:
				break
			print("")
		except KeyboardInterrupt:
			print("\033[31m^C\033[0m")
			angry_mater = angry_mater + 1
			if angry_mater >= 87:
				print(data["message"]["secret"])
			print("")
else:
	if args.c != "none" and args.f != "none":
		print(data["message"]["wrong_arg"])
	else:
		if args.c != "none":
			cmd_load(args.c)
		if args.f != "none":
			if Path(args.f).suffix == ".sh":
				if Path(args.f).exists() == True:
					with open(args.f, "r", encoding="UTF-8") as file_load:
						load_file = file_load.read()
					file_lines = load_file.splitlines()
					file_count = 0
					for _ in range(len(file_lines)):
						cmd_load(file_lines[file_count])
						file_count = file_count + 1
				else:
					print(f"{args.f}{data["message"]["wrong_file2"]}")
			else:
				print(data["message"]["wrong_file"])








