# Cookiecutter add-on templates

These are intended to add common tooling to existing projects, NOT to create
a new project from scratch, although they *could* be used that way.

Let's say you have a project directory called foo in ~/projects. To add the
`logging` add-on template to this project,

```sh
cd ~/projects
~/ccutter . gh:ericgj/python-project-templates --directory add-on/logging
```

When prompted for `project_slug`, enter `foo`.

(For more info, see the top-level README.)


