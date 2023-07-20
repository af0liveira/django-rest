# API With Django REST Framework

This project is being developed as part of the course [API com Django 3: Django REST Framework](https://cursos.alura.com.br/course/api-django-3-rest-framework) from [Alura online school](https://www.alura.com.br/).

The project implements the API of a school management system.

## Virtual development environment (VDE)

A virtual development environment (VDE) is used to isolate the project isolated and avoid incompatibilities.
The specs are stored in `environment.yml`, which is suitable for creating virtual environments with
[conda](https://docs.conda.io/projects/conda/en/stable/)
or
[miniconda](https://docs.conda.io/en/latest/miniconda.html).

The following instructions should suffice for using _conda_ within this project.
For information on installation and usage of _conda_, please see documentation at
[conda](https://docs.conda.io/projects/conda/en/stable/)
or
[miniconda](https://docs.conda.io/en/latest/miniconda.html).

### Creating and activating the VDE with conda

The following command can be used to create the VDE within the folder `./venv`

```sh
conda create --prefix ./venv --file environment.yml
```

The environment can be activated and deactivated with the commands

```sh
conda activate ./venv  # activates the local ./venv environment
conda deactivate   # deactivates the active environment
```

### Updating the VDE

New packages can be installed with

```sh
# Make sure the VDE has been activated!
conda install <name>
```

If new packages have been installed, the `environment.yml` should be updated with

```sh
conda list -e > environment.yml
```

---
