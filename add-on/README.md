# Cookiecutter add-on templates

These are intended to add common tooling to existing projects, NOT to create
a new project from scratch, although they *could* be used that way.

Let's say you have a project directory called foo in ~/projects. To add the
`logging` add-on template to this project,

```sh
cd ~/projects
cookiecutter -s gh:ericgj/python-project-templates --directory add-on
```

When prompted for `project name`, enter `foo`.


