# Mad Libs Game Example

# Asking the user for input
adjective1 = input("Enter an adjective: ")
noun1 = input("Enter a noun: ")
verb_past_tense1 = input("Enter a verb in past tense: ")
adverb1 = input("Enter an adverb: ")
adjective2 = input("Enter another adjective: ")
noun2 = input("Enter another noun: ")
noun3 = input("Enter one more noun: ")
adjective3 = input("Enter another adjective: ")
verb1 = input("Enter a verb: ")
adverb2 = input("Enter another adverb: ")
verb_past_tense2 = input("Enter another verb in past tense: ")
adjective4 = input("Enter another adjective: ")

# The story template
story = f"""
One day, my {adjective1} friend and I decided to go to the {noun1} park.
We {verb_past_tense1} {adverb1} through the park, looking for the {adjective2} spot.
Suddenly, we saw a {noun2} in the distance. It was too {adjective3} to {verb1}, so we
decided to {adverb2} walk away. By the time we got back to the {noun3}, it was already
dark. We {verb_past_tense2} home, laughing about our {adjective4} adventure.
"""

# Printing the story
print(story)