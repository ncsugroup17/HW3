# Homework3

## Part 2 static analysis tools
 * Run this requirements.txt file below
 ```bash
pip install -r requirements.txt
 ```

 1. command to run radon
 ```bash
radon cc .\hw2_debugging.py rand.py -a > radon_report.txt
 ```

 ```bash
pylint hw2_debugging.py rand.py > pylint_report.txt
 ```

 ```bash
pyflakes hw2_debugging.py rand.py > pyflakes_report.txt
 ```