# UOCIS322 - Project 4 #
Brevet time calculator.

## Overview

Reimplement the RUSA ACP controle time calculator with Flask and AJAX.

### ACP controle times

That's *"controle"* with an *e*, because it's French, although "control" is also accepted. Controls are points where a rider must obtain proof of passage, and control[e] times are the minimum and maximum times by which the rider must arrive at the location.

The algorithm for calculating controle times is described here [https://rusa.org/pages/acp-brevet-control-times-calculator](https://rusa.org/pages/acp-brevet-control-times-calculator). Additional background information is given here [https://rusa.org/pages/rulesForRiders](https://rusa.org/pages/rulesForRiders). The description is ambiguous, but the examples help. Part of finishing this project is clarifying anything that is not clear about the requirements, and documenting it clearly.  

We are essentially replacing the calculator here [https://rusa.org/octime_acp.html](https://rusa.org/octime_acp.html). We can also use that calculator to clarify requirements and develop test data.  

## Getting started

In a nutshell, you will:

* Implement the logic in `acp_times.py` based on the algorithm linked above.

* Edit the template and Flask app so that the required remaining arugments are passed along.

* Create test cases using the website, and write test suites for your project.

* Update this file (`README`).

### AJAX and Flask reimplementation

The implementation that you will do will fill in times as the input fields are filled using AJAX and Flask. Currently the miles to kilometers (and some other basic stuff) is implemented with AJAX. The remainder is left to you.

## Credits
cheng cheng
ccheng7@uuoregon.eduu
