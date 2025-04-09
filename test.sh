#!/bin/sh
# Check the answers 
jq '.[].average_age_per_city' answer.json 
jq '.[].average_friends_per_city' answer.json
jq '.[].person_with_most_friends' answer.json
jq '.[].most_common_hobby' answer.json 
jq '.[].most_common_name_all_cities' answer.json 
