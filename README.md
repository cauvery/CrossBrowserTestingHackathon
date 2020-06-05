1. `git clone https://github.com/cauvery/UFG_Hackathon`
2.  `UFG_Hackathon` in your favorite editor or in terminal
3. Change the Applitools API key. Get one by logging into Applitools > Person Icon > My API Key
4. Install requirements `pip install -r requirements.txt`
5. Run `ultrafastgrid_demo.py` by calling `python ultrafastgrid_demo.py`




# Cross Browser UFG Hackathon 

![](https://s3.amazonaws.com/assets.coveralls.io/badges/coveralls_unknown.svg)

## Overview

Cross Browser Testing using Traditional approach and Applitools AI with Ultrafast Grid 

## Installation

First you will need to clone the repo:

```
  $ git clone https://github.com/cauvery/CrossBrowserTestingHackathon.git
```

Install `pip` the python package installer, if you don't already have it:

```
  $ sudo easy_install pip
```

Next, install the required dependencies:

```
$ pip install -r requirements.txt 
```

## Usage

Using pytest:

To execute all tests 
```
  $ pytest --env=v1 -s tests
```

To execute only Traditional tests only 
```
  $ pytest --env=v1 -s tests/TradionalTests
```

To execute only Traditional tests only 
```
  $ pytest --env=v1 -s tests/ModernTests
```

To Execute the tests on different version, change --env=v2 as below
```
  $ pytest --env=v2 -s tests/ModernTests
```

To generate html report use --html command line option
```
  $ pytest --env=v2 -s tests/TraditionalTests  --hmtl report.html
```

To execute the tests in parallel use -n command line option
```
  $ pytest --env=v2 -s tests/TraditionalTests -n 3
```

Optional: Using tox (separate installation required):

```
  $ tox -- --env=v1 -s tests/TradionalTests
```
