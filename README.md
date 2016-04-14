[![Build Status](https://travis-ci.org/jeremy-miller/life-python.svg?branch=master)](https://travis-ci.org/jeremy-miller/life-python)
[![Coverage Status](https://coveralls.io/repos/github/jeremy-miller/life-python/badge.svg?branch=master)](https://coveralls.io/github/jeremy-miller/life-python?branch=master)
[![Codacy Badge](https://api.codacy.com/project/badge/grade/9022f54b73704803ac5993f4ed08a874)](https://www.codacy.com/app/jgmiller88/life-python)
[![Code Climate](https://codeclimate.com/github/jeremy-miller/life-python/badges/gpa.svg)](https://codeclimate.com/github/jeremy-miller/life-python)
[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/hyperium/hyper/master/LICENSE)

# Life
Python implementation of [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).
This implementation uses a Docker image to isolate the execution environment.  The Docker Python [base image](https://hub.docker.com/_/python/)
used will automatically copy over the pip file and install dependencies, as well as copy over the source code to ```/usr/src/app```.

This game has been tested on Mac OS X El Capitan (10.11).

# Usage
To interact with the Life game, follow the steps below.

### Setup
Before interacting with the Life game, the Docker environment must be setup first.

1. Create a new Docker virtual machine (called *default*): ```docker-machine create default```
2. Start the *default* Docker virtual machine: ```docker-machine start default```
3. Connect the terminal to the *default* Docker virtual machine: ```eval $(docker-machine env default)```
4. Build the Docker image: ```docker build -t jeremymiller/life-python .```

### Configuration
To configure the Life game, update the settings in the *life/config.yml* file.

### Lint and Test
To lint (using pep8 and pylint) the Life package, execute the following command: ```docker run -it --rm jeremymiller/life-python pep8 life && pylint life```

To run the Life tests, execute the following command: ```docker run -it --rm jeremymiller/life-python py.test --capture=sys```

### Run
To run the Life game, execute the following command: ```docker run -it --rm jeremymiller/life-python python main.py```
