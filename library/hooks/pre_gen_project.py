from datetime import datetime
import json
from urllib import request
import re
import ssl
import sys

PROJECT_REGEX = re.compile(r'^[_a-zA-Z][_a-zA-Z0-9]+$')

def assert_module_name(name):
    if not PROJECT_REGEX.match(name):
        print(f"ERROR: the project slug ({name}) is not valid.", file=sys.stderr)
        sys.exit(1)


def fetch_license_file(license):
    url = f"http://api.github.com/licenses/{license.lower()}"
    req = request.Request(url, headers={'Accept': 'application/vnd.github.v3+json'}, method='GET')
    with request.urlopen(req) as res:
        data = json.loads(res.read().decode('utf-8'))
        return data['body']

assert_module_name('{{ cookiecutter.project_slug }}')

license = '{{ cookiecutter.license }}'
your_name = '{{ cookiecutter.your_name }}'
your_email = '{{ cookiecutter.your_email }}'
fullname = f"{your_name} <{your_email}>"

year = datetime.utcnow().strftime('%Y')

if not license == 'None':
    text = fetch_license_file(license)
    text = text.replace("[year]",year).replace("[fullname]",fullname)
    with open("LICENSE","w") as f:
        f.write(text)

