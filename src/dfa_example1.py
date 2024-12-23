"""
Deterministic Finite Automata (DFA) Example

- DFA Definition:
  A Deterministic Finite Automaton (DFA) is an abstract finite state machine used in computer science
  for modeling computation. It consists of a finite set of states, a set of input symbols (called the alphabet),
  a transition function that takes a state and an input symbol and returns the next state, a start state,
  and a set of accept states.

- Purpose:
  The DFA is used to recognize patterns within input taken from some character set (or alphabet).

This example demonstrates a DFA that recognizes the language L1, defined as:
  L1 = Set of all strings that start with '0'

The DFA for this task has two states:
  1. q0: Start and accept state. If '0' is read, it stays in q0. If '1' is read, it transitions to q1.
  2. q1: Non-accept state. It stays in q1 regardless of reading '0' or '1'.

Example Implementation in Python:
"""
from PIL import Image
 
def dfa_accepts(input_string):
    # Check if the string starts with '0'
    if input_string[0] != '0':  # If the first character is not '0', reject immediately
        return False

    # Ensure the string contains only '0' and '1'
    for char in input_string:
        if char not in ['0', '1']:  # If any character is not '0' or '1'
            return False

    # The string is accepted if it starts with '0'
    return True
  

# Main loop to continuously ask the user for input until 'done'
while True:
    
    # Ask for user input
    user_input = input("Enter a string to check (only '0' and '1' are valid characters, type 'done' to exit): ")

    # If user wants to exit the loop
    if user_input.lower() == "done":
        print("Exiting the program.")
        break

    # Check if the input is valid
    if user_input.startswith('0'):
        result = "accepted"
    else:
        result = "rejected"

    # Provide feedback to the user based on their input
    if dfa_accepts(user_input):
        print(f"The input '{user_input}' is accepted.")
    else:
        print(f"The input '{user_input}' is rejected because it starts with '1'.")

   
    """
    Explanation: 
    Loop Continuation: The program keeps asking the user to enter strings until the word "done" is typed. 
    This matches your requirement to allow multiple inputs.
    Custom Message: Based on whether the string starts with '0' or '1', the program gives a detailed response.
    Exit: When the user types "done", the program exits the loop and terminates.
    """

