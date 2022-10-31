#!/bin/bash
echo "Script for preparing the development environment"
echo "-------"

echo "Checking if config.ini exists in the current working directory -->"
if test -f "config.ini"; then
        echo "exists"
else
        echo "Copying config file from .... [should create secret dir for config files]"
        if [ $? -eq 0 ]; then echo "OK"; else "Problem copying config.ini file"; exit 1; fi
fi
echo "-------"

echo "Checking if log_worker.yaml exists in the current working directory -->"
if test -f "log_worker.yaml"; then
        echo "exists"
else
        echo "Copying log config file from local dev template log_worker.yaml.dev"
        cp log_worker.yaml.dev log_worker.yaml
        if [ $? -eq 0 ]; then echo "OK"; else echo "Problem copying log_worker.yaml file" ; exit 1; fi
fi
echo "-------"

echo "Checking if log_migrate_db.yaml exists in the current working directory -->"
if test -f "log_migrate_db.yaml"; then
        echo "exists"
else
        echo "Copying log migrate_db file from local dev template log_migrate_db.yaml.dev"
        cp log_migrate_db.yaml.dev log_migrate_db.yaml
        if [ $? -eq 0 ]; then echo "OK"; else echo "Problem copying log_migrate_db.yaml file"; exit 1; fi
fi
echo "-------"

echo "Getting python executable location"
python_exec_loc=$(which python)
if [ $? -eq 0 ]; then echo "OK"; else echo "Problem getting python exec location"; exit 1; fi
echo "$python_exec_loc"
echo "-------"

echo "Running config tests." 
$python_exec_loc test_config.py
if [ $? -eq 0 ]; then echo "OK"; else echo "Config test failed."; exit 1; fi
echo "-------"
echo "Running date format test."
$python_exec_loc test_astero.py
if [ $? -eq 0 ]; then echo "OK"; else echo "Config test failed."; exit 1; fi

echo "-------"
echo "This is the end of our automation." 

