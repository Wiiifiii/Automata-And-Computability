class MarbleDFA:
    def __init__(self):
        # Initial state
        self.current_state = '000r'
        
        # Define the transitions for each input from each state
        self.transitions = {
            ('000r', 'A'): '100a',
            ('000r', 'B'): '001r',
            ('100a', 'A'): '000r',
            ('100a', 'B'): '101a',
            ('001r', 'A'): '101a',
            ('001r', 'B'): '000r',
            ('101a', 'A'): '001r',
            ('101a', 'B'): '100a',
             # Hypothetical additional transitions
            ('010a', 'A'): '110r',
            ('010a', 'B'): '011r',
            ('110r', 'A'): '010a',
            ('110r', 'B'): '111a',
            ('011r', 'A'): '111a',
            ('011r', 'B'): '010a',
            ('111a', 'A'): '011r',
            ('111a', 'B'): '110r',
        }

    def input(self, inp):
        # Handle the input and update the state based on the transition rules
        if (self.current_state, inp) in self.transitions:
            self.current_state = self.transitions[(self.current_state, inp)]
        else:
            print(f"No transition defined from {self.current_state} with input {inp}")
        return self.current_state

    def is_accepting(self):
        # Check if the current state is an accepting state
        return self.current_state[-1] == 'a'

def main():
    dfa = MarbleDFA()
    print("Marble Rolling Toy DFA Simulator")
    print("Enter a sequence of drops using 'A' or 'B' (e.g., 'ABBA'), or type 'quit' to exit:")

    while True:
        user_input = input("Enter input sequence: ").upper()
        if user_input == 'QUIT':
            break
        states = []
        for inp in user_input:
            if inp not in ['A', 'B']:
                print("Invalid input! Use only 'A' or 'B'.")
                break
            state = dfa.input(inp)
            states.append(state)

        final_state = states[-1] if states else dfa.current_state
        lever_positions = final_state[:-1]  # Strip the acceptance character
        lever_directions = ''.join('L' if x == '0' else 'R' for x in lever_positions)

        result = "accepted" if dfa.is_accepting() else "rejected"
        print(f"Final state: {final_state} ({result}) because the lever positions are {lever_directions}.")

if __name__ == "__main__":
    main()

    """
    What This Code Does:
    Initialization: It sets up the DFA with the starting state and transition rules.
    User Interaction: It prompts the user to enter a sequence of inputs ('A' for left and 'B' for right) and processes these inputs through the DFA.
    Processing: As it processes each input, it updates the state based on the defined transitions.
    Feedback: After processing the input sequence, it reports the final state and whether it is accepting or rejecting, 
    along with the positions of the levers (L for left and R for right based on the binary representation in the state).
    """ 