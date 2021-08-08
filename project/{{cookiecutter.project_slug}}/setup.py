import codecs
import os.path
from setuptools import setup, find_packages

# Note: copied from pip setup.py

def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()

def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


{%- set license_classifiers = {
  "MIT": "License :: OSI Approved :: MIT License",
  "BSD-3-Clause": "License :: OSI Approved :: BSD License",
  "AGPL-3.0": "License :: OSI Approved :: GNU Affero General Public License v3",
  "GPL-3.0": "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
  "None": None,
}  %}

install_requires = [
]

tests_require = [
    'pytest'
]


setup(
    name="{{ cookiecutter.project_slug }}",
    version=get_version("src/{{ cookiecutter.root_source_dir }}/__init__.py"),
    author="{{ cookiecutter.your_name }}",
    author_email="{{ cookiecutter.your_email }}",
    description="{{ cookiecutter.project_short_desc }}",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    url="{{ cookiecutter.repo_origin }}",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Development Status :: 2 - Pre-Alpha",
        {%- if cookiecutter.license in license_classifiers %}
        "{{ license_classifiers[cookiecutter.license] }}", 
        {%- endif %}
    ],
    {%- if cookiecutter.has_command_line_interface|lower in ['y','yes'] %}
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.project_slug }}={{ cookiecutter.project_slug }}.__main__:main',
        ],
    },
    {%- endif %}    
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={"test": tests_require},  # for pip
    zip_safe=False,   # for mypy
)
