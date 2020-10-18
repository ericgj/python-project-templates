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


print("Initializing git...", file=sys.stderr)
run([ "git", "init", "." ])

print("Adding user name to git...", file=sys.stderr)
run([ "git", "config", "--add", "--local", "user.name", "'{{ cookiecutter.your_name }}'" ])

print("Adding user email to git...", file=sys.stderr)
run([ "git", "config", "--add", "--local", "user.email", "'{{ cookiecutter.your_email }}'" ])

print("Adding git origin repo...", file=sys.stderr)
run([ "git", "remote", "add", "origin", "{{ cookiecutter.repo_origin }}" ])

print("Done.", file=sys.stderr)
