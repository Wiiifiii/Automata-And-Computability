"""
Deterministic Finite Automata (Example-2)

Construct a DFA that accepts sets of all strings over {0,1} of length 2.
sigma = {0,1} 
L= {00,01,10,11}
    
DFA Diagram for Example 2:
    
        (q0) --0,1--> (q1) --0,1--> (q2)
                                    |
                                    v
                                (reject) [any further inputs]
                                
Example Implementation in Python:
""" 

def dfa_accepts(input_string):
    # Define the DFA transitions
    dfa = {
        'q0': {'0': 'q1', '1': 'q1'},  # From q0, '0' or '1' goes to q1
        'q1': {'0': 'q2', '1': 'q2'},  # From q1, '0' or '1' goes to q2
        'q2': {},  # From q2, any further input should be rejected (no valid transitions)
    }

    # Start at the initial state q0
    current_state = 'q0'

    # Process each character in the input string
    for char in input_string:
        if char not in dfa[current_state]:
            return False  # Reject if the character is not part of the current state transitions
        current_state = dfa[current_state][char]

    # The string is accepted if it ends in the accepting state (q2) and is of exact length 2
    return current_state == 'q2'

# Main loop to continuously ask the user for input until 'done'
while True:
    # Ask for user input
    user_input = input("Enter a string to check (only '0' and '1' are valid characters, type 'done' to exit): ")

    # If user wants to exit the loop
    if user_input.lower() == "done":
        print("Exiting the program.")
        break

    # Check if the input is valid and accepted
    if dfa_accepts(user_input):
        print(f"The input '{user_input}' is accepted.")
    else:
        print(f"The input '{user_input}' is rejected because it is not of length 2.")


    """
    Summary:
    This DFA accepts only strings of exactly length 2 consisting of characters from the alphabet 
    {0,1}{0,1}.
    Strings of length 1 or greater than 2 are rejected.
    """ 