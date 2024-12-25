"""
Description:
NFA Simulation: The function simulate_nfa starts with the initial state and processes each character of the input string, transitioning to all possible next states.
DFA Construction: The function dfa_transitions creates a mapping from each set of NFA states to its possible transitions based on the NFA's rules.
DFA Acceptance Check: The function is_accepted_by_dfa checks if the computed final states from the input string belong to any of the accepting states.

"""

def simulate_nfa(nfa_trans, start_state, input_string):
    """ Simulates the NFA for a given input string starting from the start state. """
    current_states = {start_state}
    for char in input_string:
        next_states = set()
        for state in current_states:
            next_states.update(nfa_trans(state, char))
        current_states = next_states
    return current_states

def nfa_transitions(state, char):
    """ Define transitions for the NFA. """
    transitions = {
        'A': {'a': ['A', 'B'], 'b': ['C']},
        'B': {'a': ['A'], 'b': ['B']},
        'C': {'a': ['B'], 'b': ['A', 'B']}
    }
    return transitions.get(state, {}).get(char, [])

def dfa_transitions():
    """ Construct the DFA transitions based on the NFA transitions. """
    dfa_states = [
        frozenset(['A']), frozenset(['A', 'B']), frozenset(['B']), frozenset(['C']), frozenset(['A', 'B', 'C'])
    ]
    dfa_trans = {str(state): {} for state in dfa_states}
    alphabet = ['a', 'b']

    for state in dfa_states:
        for char in alphabet:
            next_state = set()
            for substate in state:
                next_state.update(nfa_transitions(substate, char))
            dfa_trans[str(state)][char] = str(frozenset(next_state))
    return dfa_trans

def is_accepted_by_dfa(dfa_trans, input_string, start_state, accepting_states):
    """ Determines if the input string is accepted by the DFA. """
    current_state = str(start_state)
    for char in input_string:
        current_state = dfa_trans[current_state].get(char, '{}')
    return current_state in accepting_states

# Define NFA and DFA settings
start_state = 'A'
nfa_accepting_states = ['B']
dfa_accepting_states = {str(frozenset(['A'])), str(frozenset(['A', 'B'])), str(frozenset(['B', 'C']))}

# Create DFA transitions
dfa_trans = dfa_transitions()

# User input loop for testing
print("NFA and DFA Results:")
while True:
    user_input = input("Enter a string to check (only 'a' and 'b' are valid characters, type 'done' to exit): ")
    if user_input.lower() == 'done':
        break
    if all(char in 'ab' for char in user_input):
        nfa_results = simulate_nfa(nfa_transitions, start_state, user_input)
        nfa_accepted = any(state in nfa_accepting_states for state in nfa_results)
        dfa_result = is_accepted_by_dfa(dfa_trans, user_input, frozenset([start_state]), dfa_accepting_states)
        print(f"The input '{user_input}' | NFA accepts: {nfa_accepted} | DFA accepts: {dfa_result}")
    else:
        print("Invalid input. Please only use 'a' and 'b'.")
