def nfa_accepts(input_string):
    # Define the NFA transitions
    nfa = {
        'A': {'0': ['A', 'B'], '1': ['A']},
        'B': {'0': [], '1': []}
    }
    current_states = ['A']  # Start with the initial state A

    # Process each character in the input string
    for char in input_string:
        # Move to the next set of states based on the character and current states
        next_states = []
        for state in current_states:
            if char in nfa[state]:
                next_states.extend(nfa[state][char])
        current_states = next_states

    # Determine if the string is accepted by checking if B is a final state in the current states
    return 'B' in current_states

# Interactively test strings entered by the user
print("Enter a string to check (only '0' and '1' are valid characters, type 'done' to exit):")
while True:
    user_input = input()
    if user_input == 'done':
        break
    if all(char in {'0', '1'} for char in user_input):  # Ensure only '0' and '1' are in the input
        result = "accepts" if nfa_accepts(user_input) else "rejects"
        print(f"NFA {result} the string '{user_input}'")
    else:
        print("Invalid input: only '0' and '1' are allowed.")
