import pandas as pd

# Define lever states and inputs
lever_states = [
    "000", "001", "010", "011",
    "100", "101", "110", "111"
]
inputs = ["A", "B"]

# Define transitions explicitly
transitions = {
    "000": {"A": {"next_state": "100", "output": "Non-acceptance"}, "B": {"next_state": "011", "output": "Non-acceptance"}},
    "001": {"A": {"next_state": "101", "output": "Non-acceptance"}, "B": {"next_state": "000", "output": "Acceptance"}},
    "010": {"A": {"next_state": "110", "output": "Non-acceptance"}, "B": {"next_state": "001", "output": "Acceptance"}},
    "011": {"A": {"next_state": "111", "output": "Non-acceptance"}, "B": {"next_state": "010", "output": "Acceptance"}},
    "100": {"A": {"next_state": "000", "output": "Acceptance"}, "B": {"next_state": "111", "output": "Non-acceptance"}},
    "101": {"A": {"next_state": "001", "output": "Acceptance"}, "B": {"next_state": "110", "output": "Non-acceptance"}},
    "110": {"A": {"next_state": "010", "output": "Acceptance"}, "B": {"next_state": "101", "output": "Acceptance"}},
    "111": {"A": {"next_state": "001", "output": "Acceptance"}, "B": {"next_state": "110", "output": "Acceptance"}},
}

# Generate all possible combinations
rows = []
for state in lever_states:
    for inp in inputs:
        next_state = transitions[state][inp]["next_state"]
        output = transitions[state][inp]["output"]
        rows.append({
            "Lever State (Initial)": state,
            "Input": inp,
            "Next State": next_state,
            "Output": output,
            "Acceptance": "Accept" if output == "Acceptance" else "Reject"
        })

# Create a DataFrame
df = pd.DataFrame(rows)

# Save the table to a CSV file
df.to_csv("Marble_Rolling_Toy_State_Table.csv", index=False)

print("All possible transitions saved as 'Marble_Rolling_Toy_State_Table.csv'.")
