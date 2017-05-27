# Traffic Simulator
A Simple Traffic Simulator

#### Usage Instructions

Provided is a trafficsim command line utility (run_sim.py) that will all for the running of simple one traffic light simulations. The usage of that script follow:

```shell
usage: run_sim.py [-h] red_ms yellow_ms green_ms [step]

Run Simple Traffic Signal Simulator. To safely exit the simulation press 'q'.

positional arguments:
  red_ms      Duration in ms for red light
  yellow_ms   Duration in ms for yellow light
  green_ms    Duration in ms for green light
  step        (Optional) Duration in ms for simulation step. Defaults to 100ms

optional arguments:
  -h, --help  show this help message and exit
```

This simulator will run indefinitely until a user safely exits by pressing the 'q' key. Note that the trafficsim package is not required to be installed as long as you execute the run_sim.py from the root directly of this repository.

An example usage of the run_sim.py utility for a traffic light sim where each light cycles every second:

```shell
python run_sim.py 1000 1000 1000
```

#### Package Installation

Simply use the setup.py provided to install the package into your disutils.

```shell
python setup.py install
```

#### Source Installation

Add path to location where you have cloned this repository to your PYTHONPATH environment variable. Install requirements.txt using pip.

On Linux/MacOSx:
```shell
export PYTHONPATH="${PYTHONPATH}:/path/to/respository"
pip install -r /path/to/repository/requirements.txt
```

#### Running Tests

```shell
python -m pytest /path/to/repository/tests
```

#### Todo

* Simulator Unit Tests
* Continuous Integration Support for automating builds

