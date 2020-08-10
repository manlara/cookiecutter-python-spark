"""
{{ cookiecutter.project_short_description }}
"""

import os
import argparse
import {{ cookiecutter.project_name }}

def main(arguments):
    app_name = "{{ cookiecutter.project_name }}"

if __name__ == '__main__':
    main_parser = argparse.ArgumentParser()
    main_parser.add_argument('args', nargs=argparse.REMAINDER)
    args = main_parser.parse_args().args
    if type(args)==list:
        args = args[0]
    print("args ===> ", args)
    parser = argparse.ArgumentParser()
    # parser.add_argument("--var", type=str, nargs='?', default="")
    arguments = parser.parse_args(args.split())
    print("arguments ==> ", arguments)
    main(arguments)
