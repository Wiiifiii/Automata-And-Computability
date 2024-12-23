"""
    Deterministic Finite Automata (Example-3)
    
    Construct a DFA that accepts any strings over {a,b} that does not contain the string
    "aabb" in it.
    
    DFA Diagram for Example 3:
    
        (q0) --a--> (q1) --a--> (q2) --b--> (q3) --b--> (q4)
         |           |           |           |        [reject]
         b           b           a           a          (trap state)
         |           |           |
         v           v           v
        (q0) <----b--(q0) <----b--(q0) <----b--
        [start]    [start after 'b']   [start over]

    
"""

def dfa_accepts(input_string):
    # Define the DFA transitions
    dfa = {
        'q0': {'a': 'q1', 'b': 'q0'},  # From q0, 'a' goes to q1, 'b' stays in q0
        'q1': {'a': 'q2', 'b': 'q0'},  # From q1, 'a' goes to q2, 'b' goes to q0
        'q2': {'a': 'q1', 'b': 'q3'},  # From q2, 'a' goes to q1, 'b' goes to q3
        'q3': {'a': 'q1', 'b': 'q4'},  # From q3, 'a' goes to q1, 'b' goes to reject (q4)
        'q4': {}  # From q4 (reject state), there are no valid transitions (stay in reject)
    }

    # Initial state is q0
    current_state = 'q0'

    # Process each character in the input string
    for char in input_string:
        if char not in dfa[current_state]:
            return False  # Reject if the character is not part of the current state transitions
        current_state = dfa[current_state][char]
        
        # If the DFA reaches the reject state, immediately reject the string
        if current_state == 'q4':
            return False

    # The string is accepted if it does not contain "aabb" (does not reach q4)
    return current_state != 'q4'


# Main loop to continuously ask the user for input until 'done'
while True:
    # Ask for user input
    user_input = input("Enter a string to check (only 'a' and 'b' are valid characters, type 'done' to exit): ")

    # If user wants to exit the loop
    if user_input.lower() == "done":       
        print("Exiting the program.")
        break

    # Check if the input is valid and accepted
    if dfa_accepts(user_input):
        print(f"The input '{user_input}' is accepted.")
    else:
        print(f"The input '{user_input}' is rejected because it contains 'aabb'.")
