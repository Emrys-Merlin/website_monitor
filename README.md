# Website monitor

This script checks the http status code of a list of websites and exposes the code as prometheus metrics.

## Installation

Before you install the script, I would recommend that you create a new virtual environment with your favorite virtual environment framework (e.g. venv, conda,...).

```bash
$ git clone github.com/Emrys-Merlin/website_monitor
$ cd website_monitor
$ pip install -e .
$ cp website_monitor/example_config.yaml website_monitor/config.yaml
```
## Configuration

```yaml
# Time between website polling
sleep_time: 10

# Port at which prometheus metrics are exposed
port: 8000

# List with names (for humans) and urls of websites to monitor
websites:
  blog: http://www.google.de
```

## Usage

After the configuration file is set up, you can simply run `website_monitor`. It might make sense to build a system.d or supervisor.d service file around it.
