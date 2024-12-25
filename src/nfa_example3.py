




def dfa_simulate(input_string):
    # Define the DFA transitions
    dfa = {
        'A': {'a': 'AB', 'b': 'C'},
        'AB': {'a': 'AB', 'b': 'BC'},
        'BC': {'a': 'AB', 'b': 'AB'},
        'C': {'a': '', 'b': 'AB'},
        'D': {'a': 'AB', 'b': 'D'}
    }
    
    current_state = 'A'  # Start state
    final_states = ['C', 'BC']  # Accepting states
    
    # Process the input string
    for char in input_string:
        if char in dfa[current_state]:
            current_state = dfa[current_state][char]
        else:
            return "Rejected"  # Rejection on invalid transition
    
    # Check if the current state is an accept state
    if any(state in current_state for state in final_states):
        return "Accepted"
    else:
        return "Rejected"

# Testing the DFA
test_strings = ["aab", "aba", "bbb", "baa", "abab", "baba"]
for s in test_strings:
    result = dfa_simulate(s)
    print(f"The string '{s}' is {result}.")
