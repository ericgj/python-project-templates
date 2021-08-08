{%- if cookiecutter.has_command_line_interface|lower in ['y','yes'] %}

from argparse import ArgumentParser
import sys

def main(argv=sys.argv):
    cmd = ArgumentParser(description="{{ cookiecutter.project_short_desc }}")

    # TODO define your CLI here

    args = cmd.parse_args(argv)

    # TODO execute with parsed arguments

    print(args)

if __name__ == "__main__":
    main()

{%- endif %}
