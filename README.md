[![Build Status](https://travis-ci.org/jeremy-miller/life-python.svg?branch=master)](https://travis-ci.org/jeremy-miller/life-python)
[![Test Coverage](https://coveralls.io/repos/github/jeremy-miller/life-python/badge.svg?branch=master)](https://coveralls.io/github/jeremy-miller/life-python?branch=master)
[![Codacy](https://api.codacy.com/project/badge/grade/9022f54b73704803ac5993f4ed08a874)](https://www.codacy.com/app/jgmiller88/life-python)
[![Code Climate](https://codeclimate.com/github/jeremy-miller/life-python/badges/gpa.svg)](https://codeclimate.com/github/jeremy-miller/life-python)
[![MIT Licensed](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/hyperium/hyper/master/LICENSE)
[![Python Version](https://img.shields.io/badge/Python-3.6.0-blue.svg)]()

# Life (in Python)
Python implementation of [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).
This implementation uses a Docker container to isolate the execution environment.  The Docker Python [base image](https://hub.docker.com/_/python/)
used will automatically copy over the pip file and install dependencies, as well as copy over the source code to ```/usr/src/app```.

![Usage](https://github.com/jeremy-miller/life-python/blob/master/usage.gif)

## Usage
To interact with the Life game, follow the steps below.

### Prerequisites
- [Docker](https://docs.docker.com/engine/installation/linux/ubuntu/)

### Setup
Before interacting with the Life game, the Docker container must be built: ```docker build -t jeremymiller/life-python .```

### Configuration
To configure the Life game, modify the ```starting_configuration_name``` variable in *main.py*.

### Lint
To run *pep8* on the Life package, execute the following command: ```docker run -it --rm jeremymiller/life-python pep8 life```

To run *pylint* on the Life package, execute the following command: ```docker run -it --rm jeremymiller/life-python pylint life```

### Test
To run the Life tests, execute the following command: ```docker run -it --rm jeremymiller/life-python py.test --capture=sys```

### Run
When running the Life game, it will output the updated grid in the terminal.

To run the Life game, execute the following command: ```docker run -it --rm jeremymiller/life-python python life/main.py```
