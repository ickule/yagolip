# YAGOLIP

## Yet Another Game Of Life In Python

This repo hosts a small command line based [Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) following [John Horton Conway](https://en.wikipedia.org/wiki/John_Horton_Conway)'s rules.

## Requirements

This programm has been tested on debian bookworm using the build in Python 3.11.2 64 bit.

You can install the necessay packages with :

```sh
sudo apt update
sudo apt install python-venv
```

## Setup

### Creating a virtual environment

To create a virtual environment in the ".venv" folder, use the following:

```sh
python3 -m venv .venv
```

You can now activate your virtual environment with:

```sh
source .venv\bin\activate
```

If you are using other shells, please use the apropriate activate file (like `activate.fish` or `activate.csh`)

Once activated, a virtual environment can be deactivated with the `deactivate` command.

### Installing dependencies

To install all Python dependencies, upgrade pip and install the modules from the requirement file, you can do so all in one with teh following command:

```sh
python3 -m pip install -U -r requirements.txt
```

### Extending PYTHONPATH environment variable

Extend your PYTHONPATH environment variable to include the workspace src folder before running the project or its tests with the following:

```sh
PYTHONPATH=./src:./tests:$PYTHONPATH
```

If you are using VSCode, the `.vscoode/yagolip.code-workspace` already contains settings to automatically extend this variable.

You can now run this program.

## Running the program

You can run the program with the following:

```sh
python src/yagolip
```

## Contributing

### Formatting

Before making a contribution, you must format you code with `black` using:

```sh
black /path/to/file
```

### Linting

Before making a contribution, you must lint your code with `ruff` using:

```sh
ruff check /path/to/file
```

## Contacts
