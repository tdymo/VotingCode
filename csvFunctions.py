import csv
from typing import Tuple

def can_vote(name: str) -> bool:
    """
    This function should determine if someone can vote.
        
    The function takes in the name of a person and reads through a csv file to determine if they are on the list of eligible voters.
    """
    with open('NamesWhoCanVote.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            for value in row:
                if name in value:
                    return True
    return False
def has_voted(name: str) -> bool:
    """
    This function should determine if someone has already voted.
        
    The function takes in the name of a person and reads through a csv file to determine if they have already voted.
    """
    with open('NamesWhoHaveVoted.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            for value in row:
                if name in value:
                    return True
    return False

def allowed_to_vote(name: str) -> bool:
    """
    This function should determine if someone is allowed to vote.
        
    This function takes in the name of a person and then runs the name
    through the can_vote and has_voted functions.
    
    If the can_vote function returns True and the has_voted function returns false,
    the allowed_to_vote function will return True.
    """
    if can_vote(name) == True:
        if has_voted(name) == False:
            return True
    return False

def just_voted(name: str) -> None:
    """
    This function should update NamesWhoHaveVoted.csv with the name given in the input.
    
    This function takes in a name as input and adds the name to the csv file.
    It returns nothing.
    """
    with open('NamesWhoHaveVoted.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([name])
        
        
def jane_voted() -> None:
    """
    This function should update Votes.csv with the name 'jane'.
    
    This function takes no input and returns nothing.
    """
    
    with open('Votes.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["jane"])


def john_voted() -> None:
    """
    This function should update Votes.csv with the name 'john'.
    
    This function takes no input and returns nothing.
    """
    with open('Votes.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["john"])
        
def count_votes() -> Tuple[int, int]:
    """
    This function should return a tuple containing the number
    of votes john has and the number of votes jane has.
    
    The function reads through the Votes.csv and counts the votes
    for jane and the votes for john
    
    This function takes no input and returns a tuple with 2 elements.
    """
    john_votes = 0
    jane_votes = 0
    with open('Votes.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            for value in row:
                if "jane" in value:
                    jane_votes += 1
                if "john" in value:
                    john_votes += 1
    return john_votes, jane_votes
        
        