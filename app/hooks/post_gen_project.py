#!/usr/bin/env python

import os
import os.path
import shutil
import subprocess
import sys

def run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE):
    try:
        subprocess.run(cmd, check=True, stdout=stdout, stderr=stderr,)
    except subprocess.CalledProcessError as e: 
        handle_subproc_error(e)

def run_in_virtualenv(cmd, venv_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE):
    venv_dir = os.path.realpath(venv_dir)
    exec_path = ""
    if os.path.exists(os.path.join(venv_dir, "bin")):
        exec_path = os.path.join(venv_dir,"bin")
    elif os.path.exists(os.path.join(venv_dir, "Scripts")):
        exec_path = os.path.join(venv_dir,"Scripts")
        """ 
        Note: Windows doesn't respect PATH in subprocess env, need to specify
        the full path to virtualenv exe. See https://bugs.python.org/issue8557.
        This is a hack.
        """
        cmd = [ os.path.join(exec_path,cmd[0]) ] + cmd[1:]
    else:
        raise ValueError("Can't find virtualenv executable path")

    env = os.environ.copy()
    env['PATH'] = os.pathsep.join([exec_path, env.get('PATH','')])
    env['VIRTUAL_ENV'] = venv_dir
    
    try:
        subprocess.run(
            cmd, 
            check=True, 
            stdout=stdout, 
            stderr=stderr, 
            env=env,
        )
    except subprocess.CalledProcessError as e: 
        handle_subproc_error(e)


def handle_subproc_error(e):
    print(f"An error occurred running `{' '.join(e.cmd)}` ({e.returncode})", file=sys.stderr)
    print(e.stderr.decode('utf-8'), file=sys.stderr)
    print(e.stdout.decode('utf-8'), file=sys.stderr)
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
run(["git", "init", "."])

print("Copying git files...", file=sys.stderr)
copy_git_files()

print("Appending to files...", file=sys.stderr)
append_files()

venv_dir = "{{ cookiecutter.virtualenv_dir }}"

print(f"Initializing virtualenv {venv_dir}...", file=sys.stderr)
run(["virtualenv", venv_dir, "--always-copy"])

print("Installing test requirements...", file=sys.stderr)
run_in_virtualenv(["pip", "install", "-r", os.path.join("test", "requirements-.txt")], venv_dir)

print("Freezing test requirements...", file=sys.stderr)
with open(os.path.join("test", "requirements.txt"), "w") as f:
    run_in_virtualenv(["pip", "freeze"], venv_dir, stdout=f)

print("Cleaning up...", file=sys.stderr)
cleanup_temp_dir()

print("Done.", file=sys.stderr)
