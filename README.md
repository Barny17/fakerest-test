# fakerest-test
This repository is submitted as a coding exercise per the specifications at:
https://github.com/brightsign/fakerest-test

**Author:** Bernard Payne, April 2025

## Licence
MIT-licensed

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
```
### Install dependencies
```
pip install -r requirements.txt
```

### Run the Python script
```
python3 task.py
```
The output file answer.json is created and contains the computed response.

### Test the output 

Using **jq**: 
```
$ jq '.[].average_age_per_city' answer.json 
{
  "Austin": 56,
  "Boston": 60,
  "Branson": 57,
  ...

$ jq '.[].average_friends_per_city' answer.json
{
  "Austin": 4,
  "Boston": 4,
  "Branson": 4,
...
}

$ jq '.[].person_with_most_friends' answer.json
  "Ava"

$ jq '.[].most_common_name_all_cities' answer.json 
"Lucas"

$ jq '.[].most_common_hobby' answer.json 
"Television"
```
The shell script *test.sh* will test the contents of answer.json in this way.
```
sh test.sh
```

\* Tested on Ubuntu 20.04 using Python 3.8.10

\* Also tested on MacOS Monterey and Python 3.13.2

## Testing
Supply a small JSON file as input for testing (comment out as required). 
TODO: Add args.

## Security
There is no inherent security implemented in this script. The data retrieved is reported to be 'fake' and thus compliant with anticipated Data Privacy and Sharing requirements.

## TODO
Add a Pytest

Consider classifying it if extended much.

Consider generating a Python package if this gets used much.

## Hat-tips
Thanks, OpenAI, for useful VSCode-integrated assistance.

## My thoughts on the exercise
This exercise targets Cloud developers... not really my role so I'm feeling a little out of sorts. I did not attempt to explore a JSON schema in any depth, focusing instead on writing code that could be assessed for roles beyond Cloud development. 

The code runs consistently for well-formed JSON that was captured in a text file for testing. The code appears to generate correct answers from the server REST API request (tested using jq). However, I see from curl use that the server intermittently generates different output formats that will cause this program to fail to parse; I have not attempted to resolve for these cases. Thanks for your understanding.
