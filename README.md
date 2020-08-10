# PySpark Cookiecutter

The project template is written to be compiled with [Cookiecutter](http://cookiecutter.readthedocs.io/).

The purpose of this repo is to make standard practices for developing PySpark applications.
The general architecture of this cookiecutter makes it adaptable to many custom use-cases. 

## Getting Started

Create a YAML file called `config.yaml` with custom values specific to you and your project
```
default_context:
  author_name: "M. Lara"
  author_email: "test@example.com"
  project_name: "Sample App"
  project_short_description: "This is a simple PySpark App"
```

To generate a project from this cookiecutter do
```
cookiecutter gh:manlara/cookiecutter-python-spark --default-config config.yaml
```

This will generate a folder ending in `-job` and beginning with the input project name lowercased and spaces replaced with an underscore.
All code relevant to your application is contained within. The `Makefile` is used to test code locally and deploy to Databricks.

## Roadmap:

While this repo does make generating PySpark applications simple, it could be extended to do more. 
If you are interested in adding additional CI/CD pipelines or local development tools feel free to make a pull request.