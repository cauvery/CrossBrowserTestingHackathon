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
Default executes on version v1 if no env is provided (-s to print console output)
```
  $ pytest -s tests
```

To execute Traditional tests only 
```
  $ pytest --env=v1 -s tests/TradionalTests
```

To execute Modern tests only 
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
