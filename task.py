#!/usr/bin/env  python3
Version = "1.1"
'''
Module performs a REST query on an endpoint and queries the data, per task description at:
    https://github.com/brightsign/fakerest-test
'''

import requests
import json
import pandas as pd
import ast
from collections import Counter
import re

# Globals
# ----------------
# URL of the endpoint 
demo_url = "http://test.brightsign.io:3000/"


def get_data(url):
    '''
    Function to make a GET request to the specified URL and return the JSON response.
    '''

    retval = None
    response = requests.get(url, stream=True)   
    # Check if the request was successful
    if response.status_code == 200:
        # Initialize a list to store the parsed JSON objects
        json_objects = []

        # Iterate over the response line-by-line
        for line in response.iter_lines():
            # Filter out keep-alive new lines
            if line:
                try:
                    # Parse each line as a JSON object
                    json_object = json.loads(line)
                    json_objects.append(json_object)
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON: {e}")
                    exit(-1)
        retval = json_objects
    else:
        print(f"Request failed with status code: {response.status_code}")
    return retval


def save_json(json_data, json_file):
    '''
    Convenience function to save JSON data to a file for testing purposes.
    '''

    with open(json_file, 'w') as file:
        json.dump(json_data, file, indent=4)
    print(f"Data saved to {json_file}")


def load_json(json_file):
    '''
    Convenience function to load demo JSON data from a file for testing purposes.
    '''

    with open(json_file, 'r') as file:
        json_data = json.load(file)
    return json_data


def process_json(json):
    '''
    Compute the required values from the supplied JSON data and return them unified in a pandas DataFrame
    '''

    # Convert the JSON data to a pandas DataFrame
    df = pd.json_normalize(json)
    if not check_dataframe(df):
        print("DataFrame check failed. Exiting.")
        exit(-1)
    
    # Calculate the average age per city
    # average_age = df['age'].mean().round().astype(int)
    average_age_per_city = df.groupby('city')['age'].mean().round().astype(int)
    # Calculate the average number of friends per city
    df['num_friends'] = df['friends'].apply(len)
    average_friends_per_city = df.groupby('city')['num_friends'].mean().round().astype(int)
    
    # Find the person with the most friends
    person_with_most_friends = df.loc[df['num_friends'].idxmax()]
    
    # Find the most common name over all cities
    # Get the most common name across all cities
    all_names = df['name'].tolist()
    # Count the occurrences of each name
    name_counts = Counter(all_names)
    # Find the most common name
    most_common_name = name_counts.most_common(1)[0][0]
    most_common_name_count = name_counts.most_common(1)[0][1]
    
    # Find the most common hobby among all friends
    all_hobbies = []
    for friends_list in df['friends']:
        for friend in friends_list:
            all_hobbies.extend(friend['hobbies'])
    # Count the occurrences of each hobby
    hobby_counts = Counter(all_hobbies)
    # Find the most common hobby
    most_common_hobby = hobby_counts.most_common(1)[0]
    
    # Combine the computed values into a DataFrame
    results_df = pd.DataFrame({
        'average_age_per_city': [average_age_per_city.to_dict()],
        'average_friends_per_city': [average_friends_per_city.to_dict()],
        'person_with_most_friends': [person_with_most_friends['name']],
        'most_friends_count': [person_with_most_friends['num_friends']],
        'most_common_name_count': [most_common_name_count],
        #'most_common_name_per_city': [most_common_name_per_city.to_dict()],
        'most_common_name_all_cities': [most_common_name],
        'most_common_hobby': [most_common_hobby[0]],
        'most_common_hobby_count': [most_common_hobby[1]]
    })
    return results_df


def check_dataframe(df):
    '''
    Check if the DataFrame has data and the correct fields
    '''

    # Define the required columns
    required_columns = ['id', 'name', 'city', 'age', 'friends']
        # Check if the DataFrame is not empty
    if df.empty:
        print("The DataFrame is empty - no data to process.")
        return False
    # Check if all required columns are present
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        print (f"The DataFrame is missing columns: {missing_columns}")
        return False
    print("The DataFrame has all required columns.")
    return True


def print_results(df):
    '''
    Convenience function to print the results in a readable format.
    '''

    print(f"The average age per city:")
    for city, mean_age in df['average_age_per_city'][0].items():
        print(f"{city}: {mean_age}")
    print()
    print(f"Average number of friends per city:")
    for city, mean_friends in df['average_friends_per_city'][0].items():
        print(f"{city}: {mean_friends}")
    print()
    print(f"Person with the most friends: {df['person_with_most_friends'][0]} (with {df['most_friends_count'][0]} friends)")
    print()
    print("Most common name for all cities:")
    print(f"{df['most_common_name_all_cities'][0]} ({df['most_common_name_count'][0]})")
    print()
    print(f"Most common hobby among all friends of all people:  {df['most_common_hobby'][0]} ({df['most_common_hobby_count'][0]})")


def save_dataframe_to_json(df, output_file):
    '''
    Convert dataframe to json and save in a readable format.
    '''
    results_df.to_json(output_file, orient='records', indent=4) # lines=True)
    print(f"Results saved to {output_file}")



if __name__ == "__main__":
    json_output_file = "answer.json" 
    # Get the data from the server (or demo file)
    json_data = get_data(demo_url)
    # Or use file input:
    # json_data = load_json("response_ok.txt")
    # json_data = load_json("test/small.json")

    # Compute the required values
    results_df = process_json(json_data)
    print_results(results_df)

    # Save the computed response as a JSON file
    save_dataframe_to_json(results_df, json_output_file)
