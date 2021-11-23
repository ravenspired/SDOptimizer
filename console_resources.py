class textColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


INFO = True
OK = True
WARNING = True
ERROR = True


def consoleSetup(displayINFO, displayOK, displayWARNING, displayERROR):
    INFO = displayINFO
    OK = displayOK
    WARNING = displayWARNING
    ERROR = displayERROR

def console(trace, status):

    if (status == "ok") & OK:
        print("["+f"{textColors.OKGREEN}{textColors.BOLD}OK{textColors.ENDC}"+"] - "+trace)
    elif (status == "warning") & WARNING:
        print("["+f"{textColors.WARNING}{textColors.BOLD}WARNING{textColors.ENDC}"+"] - "+trace)
    elif (status == "error") & ERROR:
        print("["+f"{textColors.FAIL}{textColors.BOLD}FATAL{textColors.ENDC}"+"] - "+trace)
    elif (INFO):
        print("["+f"{textColors.OKBLUE}{textColors.BOLD}INFO{textColors.ENDC}"+"] - "+trace)
    else:
        pass




