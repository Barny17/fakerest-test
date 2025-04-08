# fakerest-test
This repository is submitted as a coding exercise per the specifications at:
https://github.com/brightsign/fakerest-test

**Author:** Bernard Payne, April 2025

## Licence
MIT-licesnsed

## Running the code

### Clone the repository
```
git clone https://github.com/Barny17/fakerest-test
cd fakerest-test
```

### Create a virtual environment (if desired)
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

### Run the Python script
```
python3 task.py
```
The output file answer.json is created and contains the computed response.


## Testing
Supply a small JSON file as input for testing (comment out as required). 
TODO: Add args.

## TODO
Add a Pytest

Consider classifying it if extended much.

Consider generating a Python package if this gets used much.

## Hat-tips
Thanks, OpenAI, for useful VSCode-integrated assistance.

## My thoughts on the exercise
This exercise targets Cloud developers... not really my role so I'm feeling a little out of sorts. I did not attempt to explore a JSON schema in any depth, focusing instead on writing code that could be assessed for roles beyond Cloud development. The code runs consistently for well-formed JSON in a text file. The code appears to generate correct answers from the server REST API request but I see that the server intermittently generates output that will cause this program to fail to parse; I have not attempted to delve further into these cases. Thanks for your understanding.
