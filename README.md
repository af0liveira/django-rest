# API With Django REST Framework

This project is being developed as part of the course [API com Django 3: Django REST Framework](https://cursos.alura.com.br/course/api-django-3-rest-framework) from [Alura online school](https://www.alura.com.br/).
Note that, although the course is about Django 3, this project is implemented with Django 4.1.

The API allows CRUD operations for a school to manage its students, courses, and the enrollment of the students in the courses.

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

## Running the API locally

The first step is prepare and apply the database migrations:

```sh
python manage.py makemigrations
python manage.py migrate
```

Next, start the development web server with

```sh
python manage.py runserver [port]
```

The port argument is optional and its default value is `8000`.

With the default port, the API Root should be accessible on `127.0.0.1:8000` and
the Django Admin interface should be accessible on `127.0.0.1:8000/admin/`.

### User authentication

In order to access the server, it's necessary to create a superuser

```sh
python manage.py createsuperuser
```

### Populating the database

Student data can be created, requested, updated, and deleted via `127.0.0.1:8000/alunos/`.

Similarly, courses can be managed via `127.0.0.1:8000/cursos/`.

Finally, enrollments can be managed via `127.0.0.1:8000/matriculas/`.

### Viewing the students enrolled in a given course

The list of students enrolled in a given course can be requested via
`127.0.0.1:8000/curso/{curso_id}/matriculas`.

### Viewing the enrollments of a given student

The list of courses in which a given student is enrolled is accessible via
`127.0.0.1:8000/aluno/{aluno_id}/matriculas`.

---
