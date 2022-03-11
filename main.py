import os, subprocess, sys
CWD = os.getcwd()
Files =  os.listdir()
ARGS = sys.argv
Arg_Path = 0
Use_Arg_Path = False
def run_ls():
    os.system("ls --color=auto " + str(ARGS[1]) + " " + str(ARGS[2]) + " " + str(ARGS[3]) + " " + str(ARGS[4]) + " " + str(ARGS[5]) + " " + str(ARGS[6]) + " " + str(ARGS[7]) + " " + str(ARGS[8]) + " " + str(ARGS[9]) + " " + str(ARGS[10]))
for i in range(10):
    ARGS.append('')
for i in range(9):
    g = i + 1
    if '/' in str(ARGS[g]):
        Arg_Path = g
        Use_Arg_Path = True
    elif '-' not in str(ARGS[g]):
        if not str(ARGS[g]) == '':
            Arg_Path = g
            Use_Arg_Path = True
# e = str(ARGS[Arg_Path])
#starts_with_slash = e.startswith("/")
if Use_Arg_Path  == False:
    if not os.path.exists(".hide"):
        run_ls()
    else:
        print("ls: cannot open directory '" + str(os.getcwd()) +  "': Permission denied")
else:
    if not os.path.exists(str(ARGS[Arg_Path]) + "/.hide"):
        run_ls()
    else:
        print("ls: cannot open directory '" + str(ARGS[Arg_Path]) +  "': Permission denied")
