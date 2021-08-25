# Python project templates

A collection of [cookiecutter][cookiecutter] templates for jumpstarting 
Python apps and libraries.

## Basic usage

First make sure you have python and cookiecutter installed and on your PATH. 
The cookiecutter [install instructions][cc-install] are helpful.

You also should have [git][git] [installed][git-install] and on your PATH.

```sh
# For an application
cookiecutter gh:ericgj/python-project-templates --directory app

# For a library
cookiecutter gh:ericgj/python-project-templates --directory library
```

## Incremental usage

The basic app and library templates are designed to be opinionated, but 
minimal, with a focus on the most tedious parts of setting up a project. (See
"My approach", below).

Once you go beyond the basics of course, you get into the weeds of this tool
vs that tool, this platform vs that platform. The approach here is not to 
provide a single monolithic template with a ton of knobs, but many 
_incremental_ templates that can be merged into the basic project structure
as needed, even after you have started work.

Cookiecutter is not designed to be used this way, so this repo provides a
`ccutter` script (in `bash` only at the moment) that provide the ability to 
incrementally update a project from multiple templates.

### To install the ccutter script:

```sh
curl https://raw.githubusercontent.com/ericgj/python-project-templates/master/bin/ccutter > ~/ccutter
chmod +x ~/ccutter
```

### To use the ccutter script:

It takes the parent directory of your target directory (i.e., equivalent to the
`-o` parameter passed to `cookiecutter`), followed by the normal cookiecutter
parameters.

For example to run the `config` template to update your project in
`~/projects`:

```sh
cd ~/projects
~/ccutter . gh:ericgj/python-project-templates --directory add-on/config
```

Always make sure the `project_slug` you specify is the same: the name of your
project directory.


## My approach

TODO


[cookiecutter]: https://cookiecutter.readthedocs.io
[cc-install]: https://cookiecutter.readthedocs.io/en/1.7.3/installation.html
[git]: https://git-scm.org
[git-install]: https://git-scm.org/downloads

