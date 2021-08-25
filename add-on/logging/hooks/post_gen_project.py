#!/usr/bin/env python

import os
import os.path
import shutil
import sys

def append_files(root=os.path.join('.cookiecutter','append'), dest_root='.'):
    print(f"{root}/* -> {dest_root}/", file=sys.stderr)
    for (dir, _, fnames) in os.walk(root):
        for fname in fnames:
            rel = os.path.relpath(dir,root)
            src = os.path.join(dir,fname)
            dest = os.path.join(dest_root,rel,fname)
            print(f"    {dest}", file=sys.stderr)
            with open(src,'r') as s:
                with open(dest,'a') as d:
                    d.write("\n")
                    d.write(s.read())
                
def cleanup_temp_dir(dir=os.path.join('.cookiecutter')):
    shutil.rmtree(os.path.join('.',dir), ignore_errors=True)

print("Appending to files...", file=sys.stderr)
append_files()

print("Cleaning up...", file=sys.stderr)
cleanup_temp_dir()

print("Done.", file=sys.stderr)
