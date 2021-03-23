# This file presents a solution for the dna problem in pset6 of CS50x.

import csv
import sys
import re
import copy


def main():
    # Ensure correct usage
    if len(sys.argv) != 3:
        sys.exit("Error, human!")

    persons = []
    # Read database into memory from file
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            persons.append(row)
    # Read DNA sequence into memory from file
    with open(sys.argv[2]) as file:
        dna = file.read()
    # Identify a person based on her DNA
    find_person(dna, persons)


# Find max number of times given STR repeats in the DNA 
def longest_str(dna, STR):
    # Find longest STR in the provided DNA
    groups = re.findall(fr'(?:{STR})+', dna)
    # Proceed only if the given STR exists in the DNA
    if len(groups) > 0:
        longest = max(groups, key=len)
        longest = int(len(longest) / len(STR))
        return str(longest)
        
# Parse DNA sequence and return dictionary with longest occurences for each STR   
def parse_dna(dna, database):
    sequences = {}    
    # Find all STR occurences
    for key in database[1].keys():
        # Exclude name column from results
        if key != 'name':
            match = longest_str(dna, key)
            sequences[key] = match
    # Return dictionary with names of STRs and max number of occurences 
    return sequences    
    
def find_person(dna, persons):
    # Get dictionary with longest occurences for each STR
    sequences = parse_dna(dna, persons)
    # Get deepcopy of dictionary to temporalily modify it
    temp_sequences = copy.deepcopy(persons)
    for index, value in enumerate(persons):
        del persons[index]['name']
        if persons[index] == sequences:
            suspect_id = index
            print(temp_sequences[suspect_id]['name'])
    # If no person found in database
    print("No match")
    
    
if __name__ == "__main__":
    main()
