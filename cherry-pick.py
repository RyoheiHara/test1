#!/usr/bin/env python3
# cherry-pick.py

import sys
import subprocess

if (len(sys.argv) == 2):
    commit_id = sys.argv[1]
    proc = subprocess.run(["git", "cherry-pick", "{0}".format(commit_id)], encoding='utf-8', stdout=subprocess.PIPE)
    if proc.returncode == 0:
        pass
    elif proc.returncode == 1:
        # conflictしたため、Cの内容を採用
        proc = subprocess.run(["git", "checkout", "--theirs", "."], encoding='utf-8', stdout=subprocess.PIPE)
        if proc.returncode != 0:
            print("[ERR] git checkout --theirs .")
            sys.exit(1)
    else:
        print("[ERR] git cherry-pick", proc.returncode)
        sys.exit(1)

    # add
    proc = subprocess.run(["git", "add", "."], encoding='utf-8', stdout=subprocess.PIPE)
    if proc.returncode != 0:
        print("[ERR] git commit")
        sys.exit(1)

    # commit
    proc = subprocess.run(["git", "commit", "-m", "{0}の状態にした。".format(commit_id)], encoding='utf-8', stdout=subprocess.PIPE)
    if proc.returncode != 0:
        print("[ERR] git commit")
        sys.exit(1)

    # push
    proc = subprocess.run(["git", "push", "origin", "dev"], encoding='utf-8', stdout=subprocess.PIPE)
    if proc.returncode != 0:
        print("[ERR] git push")
        sys.exit(1)
        
else:
    print("[usage] python3 cherry-pick.py [commit id]")
    sys.exit(1)    


