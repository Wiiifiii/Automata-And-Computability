import pandas as pd

# Define lever states and inputs
lever_states = [
    "000", "001", "010", "011",
    "100", "101", "110", "111"
]
inputs = ["A", "B"]

# Define pre-switch transitions
# Switched state represents the lever states after switching before marble passes
pre_switch_transitions = {
    "000": {"A": {"switched_state": "100", "path": "A -> x1 -> D", "output": "Acceptance"},
            "B": {"switched_state": "011", "path": "B -> x3 -> C", "output": "Non-acceptance"}},
    "001": {"A": {"switched_state": "101", "path": "A -> x1 -> D", "output": "Acceptance"},
            "B": {"switched_state": "000", "path": "B -> x3 -> C", "output": "Non-acceptance"}},
    "010": {"A": {"switched_state": "110", "path": "A -> x1 -> D", "output": "Acceptance"},
            "B": {"switched_state": "001", "path": "B -> x3 -> C", "output": "Non-acceptance"}},
    "011": {"A": {"switched_state": "111", "path": "A -> x1 -> D", "output": "Acceptance"},
            "B": {"switched_state": "010", "path": "B -> x3 -> C", "output": "Non-acceptance"}},
    "100": {"A": {"switched_state": "000", "path": "A -> x1 -> C", "output": "Non-acceptance"},
            "B": {"switched_state": "111", "path": "B -> x3 -> D", "output": "Acceptance"}},
    "101": {"A": {"switched_state": "001", "path": "A -> x1 -> C", "output": "Non-acceptance"},
            "B": {"switched_state": "110", "path": "B -> x3 -> D", "output": "Acceptance"}},
    "110": {"A": {"switched_state": "010", "path": "A -> x1 -> C", "output": "Non-acceptance"},
            "B": {"switched_state": "101", "path": "B -> x3 -> D", "output": "Acceptance"}},
    "111": {"A": {"switched_state": "001", "path": "A -> x1 -> D", "output": "Acceptance"},
            "B": {"switched_state": "110", "path": "B -> x3 -> C", "output": "Non-acceptance"}},
}

# Generate all possible combinations
rows = []
for state in lever_states:
    for inp in inputs:
        switched_state = pre_switch_transitions[state][inp]["switched_state"]
        path = pre_switch_transitions[state][inp]["path"]
        output = pre_switch_transitions[state][inp]["output"]
        rows.append({
            "Initial State": state,
            "Input": inp,
            "Switched State": switched_state,
            "Path Taken": path,
            "Final State": switched_state,
            "Output": output,
            "Acceptance": "Accept" if output == "Acceptance" else "Reject"
        })

# Create a DataFrame
df = pd.DataFrame(rows)

# Save the table to a CSV file
df.to_csv("Pre_Switch_Marble_Rolling_Toy_Table.csv", index=False)


import ace_tools as tools; tools.display_dataframe_to_user(name="Pre-Switch Marble Rolling Toy Table", dataframe=df)
