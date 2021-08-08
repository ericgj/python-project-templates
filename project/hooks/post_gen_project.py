#!/usr/bin/env python

import os
import os.path
import shutil
import subprocess
import sys

def run(cmd):
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,)
    except subprocess.CalledProcessError as e: 
        handle_subproc_error(e)

def handle_subproc_error(e):
    print(f"An error occurred running `{' '.join(e.cmd)}` ({e.returncode})", file=sys.stderr)
    print(e.stderr, file=sys.stderr)
    print(e.stdout, file=sys.stderr)
    sys.exit(1)

def append_files(root=os.path.join('.cookiecutter','append')):
    for (dir, _, fnames) in os.walk(root):
        for fname in fnames:
            rel = os.path.relpath(dir,root)
            src = os.path.join(dir,fname)
            dest = os.path.join(rel,fname)
            print(f"    {dest}", file=sys.stderr)
            with open(src,'r') as s:
                with open(dest,'a') as d:
                    d.write("\n")
                    d.write(s.read())
                
def copy_git_files(root=os.path.join('.cookiecutter','git')):
    for (dir, _, fnames) in os.walk(root):
        for fname in fnames:
            rel = os.path.relpath(dir,root)
            src = os.path.join(dir,fname)
            dest_dir = os.path.join('.git',rel)
            dest = os.path.join(dest_dir,fname)
            print(f"    {dest}", file=sys.stderr)
            os.makedirs(dest_dir,exist_ok=True)
            shutil.copyfile(src, dest)

def cleanup_temp_dir(dir='.cookiecutter'):
    shutil.rmtree(os.path.join('.',dir), ignore_errors=True)



print("Initializing git...", file=sys.stderr)
run([ "git", "init", "." ])
run([ "git", "config", "--add", "--local", "user.name", "'{{ cookiecutter.your_name }}'" ])
run([ "git", "config", "--add", "--local", "user.email", "'{{ cookiecutter.your_email }}'" ])

print("Adding git origin repo...", file=sys.stderr)
run([ "git", "remote", "add", "origin", "{{ cookiecutter.repo_origin }}" ])

print("Copying git files...", file=sys.stderr)
copy_git_files()

print("Appending to files...", file=sys.stderr)
append_files()

venv_dir = "{{ cookiecutter.virtualenv_dir }}"

print(f"Initializing virtualenv {venv_dir}...", file=sys.stderr)
run(["virtualenv", venv_dir, "--always-copy"])

print("Cleaning up...", file=sys.stderr)
cleanup_temp_dir()

print("Done.", file=sys.stderr)
