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

def dfa_accepts(input_string):
    # Define the DFA transitions
    dfa = {
        'q0': {'0': 'q0', '1': 'q1'},  # From q0, reading '0' stays in q0, '1' goes to q1
        'q1': {'0': 'q1', '1': 'q1'}   # From q1, reading any character stays in q1
    }
    current_state = 'q0'  # Start in the start state q0

    # Process each character in the input string
    for char in input_string:
        current_state = dfa[current_state][char]  # Transition to the next state

    # Determine if the string is accepted
    # The string is accepted if the machine ends in state q0
    return current_state == 'q0'

# Test cases to demonstrate the DFA's functionality
test_strings = ['0', '01', '000', '010', '011', '100']
for string in test_strings:
    result = "accepts" if dfa_accepts(string) else "rejects"
    print(f"DFA {result} the string '{string}'")

"""
Explanation of Test Cases:
- '0', '000', and '010' start with '0', so they are accepted.
- '01' also starts with '0', thus it is accepted even though it has a '1' after the '0'.
- '011' and '100' do not start with '0', so they are rejected.
"""
