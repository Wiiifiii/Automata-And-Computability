# Deterministic Finite Automaton (DFA) Diagram
#
# The DFA represents the following logic:
# - Accepts the string '01' or any string containing at least one '1' followed by a '0'.
#
# States:
#   q0: Start state
#   q1: After reading '1' from q0
#   q2: After reading '0' from q0
#   q3: After reading '1' from q2
#   q4: Accepting state (after reading '1' followed by '0')
#   qX: Reject state (dead state)
#
# Transitions:
#   - State q0:
#     - On input '1', move to state q1.
#     - On input '0', move to state q2.
#   - State q1:
#     - On input '1', move to state q3.
#     - On input '0', move to state q2.
#   - State q2:
#     - On input '0', move to state q4.
#     - On input '1', move to state q3.
#   - State q3:
#     - On input '0', move to state q4.
#     - On input '1', stay in state q3.
#   - State q4:
#     - Accepting state; stays here if input is valid.
#   - State qX:
#     - Reject state; stays here for invalid input.
#
# Diagram Visualization:
#
#      (q0) --1--> (q1) --1--> (q3) --0--> (q4) [accepts]
#       |           |           |
#       0           0           1
#       |           |           |
#      (q2) --0--> (q4) [accepts] (q3)
#       |           |           |
#       1           1           0
#       |           |
#      (q3) [reject] (qX)
#
# The DFA accepts any string that either contains the exact substring "01" or any string that contains
# at least one '1' followed by a '0'.


def dfa_accepts(input_string):
    # Define the DFA transitions using '0' and '1' as inputs and states
    dfa = {
        '0': {'0': '2', '1': '1'},  # From state 0, '0' goes to state 2, '1' goes to state 1
        '1': {'0': '2', '1': '3'},  # From state 1, '0' goes to state 2, '1' goes to state 3
        '2': {'0': '4', '1': '3'},  # From state 2, '0' goes to state 4, '1' goes to state 3
        '3': {'0': '4', '1': '3'},  # From state 3, '0' goes to state 4, '1' stays in state 3
        '4': {}  # Accepting state, once in state 4, the string is accepted
    }
    
    # Ensure the input only contains valid characters '0' and '1'
    for char in input_string:
        if char not in ('0', '1'):
            print(f"The input '{input_string}' is rejected because it contains invalid characters.")
            return False
    
    # Initial state is '0' (start state)
    current_state = '0'
    
    # Process each character in the input string
    for char in input_string:
        if char not in dfa[current_state]:
            print(f"The input '{input_string}' is rejected because it doesn't follow the correct pattern.")
            return False
        current_state = dfa[current_state][char]
        
    # The string is accepted if we end in the accepting state ('4')
    return current_state == '4'


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
        print(f"The input '{user_input}' is rejected because it doesn't follow the correct pattern.")
