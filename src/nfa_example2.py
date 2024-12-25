


"""
    NFA to accept strings that end with '1'.
    
    States:
    A - Initial state, loops on '0', transitions to A and B on '1'
    B - Accepting state, no outgoing transitions (trap state for both '0' and '1')
    
    Transitions:
    A -> '0' -> A
    A -> '1' -> A, B
    B -> '0' -> None
    B -> '1' -> None
    
    Acceptance:
    If the final set of states includes B, the string is accepted.

    Args:
    input_string (str): The string to check against the NFA.

    Returns:
    bool: True if the string is accepted by the NFA, False otherwise.
    
      Initial State
        A
     ┌───┐
     │   │0
     ▼   │
  ┌───────┐    1     ┌───┐
  │   A   ├───┬─────►│ B │
  └───────┘           └───┘
     │0,1              Accepting State
     │
     ▼
    None (Trap State)
    Explanation of the Diagram:

    State A is the initial state. It transitions to itself on input '0' and to both itself and state B on input '1'.
    State B is the accepting state. Any path that leads to state B on the final input character (which must be '1') will mean the NFA accepts the string.
    This diagram shows how the NFA processes inputs and the importance of the final character to determine if a string is accepted. 
    The trap state is conceptual to indicate there are no further transitions from B on any input, ensuring that the accepted string must end with '1'.
"""
def nfa_accepts(input_string):
    # Define the NFA transitions
    nfa = {
        'A': {'0': ['A'], '1': ['A', 'B']},
        'B': {'0': [], '1': []}  # State B has no valid transitions
    }
    current_states = ['A']  # Start in the initial state A

    # Process each character in the input string
    for char in input_string:
        next_states = []
        for state in current_states:
            next_states.extend(nfa[state].get(char, []))  # Transition to next states based on input
        current_states = list(set(next_states))  # Eliminate duplicate states

    # The string is accepted if state B is one of the current states
    return 'B' in current_states

# Interactively test strings entered by the user
print("Enter a string to check (only '0' and '1' are valid characters, type 'done' to exit):")
while True:
    user_input = input()
    if user_input == 'done':
        break
    if all(char in {'0', '1'} for char in user_input):  # Validate input
        result = "accepts" if nfa_accepts(user_input) else "rejects"
        print(f"NFA {result} the string '{user_input}'")
    else:
        print("Invalid input: only '0' and '1' are allowed.")
