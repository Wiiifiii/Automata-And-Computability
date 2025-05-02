# Automata Theory Examples in Python

This repository includes several Python programs simulating theoretical automata, such as NFAs, DFAs, Mealy Machines, and toy-model state machines. These are designed for educational purposes to help understand core concepts in automata theory.

---

## 📁 File Descriptions

### 🌀 NFA Examples

- **`nfa_example1.py`**  
  Accepts binary strings **ending in '0'** using NFA simulation.

- **`nfa_example2.py`**  
  Accepts binary strings **ending in '1'**.

- **`nfa_example3.py`**  
  Hybrid simulation resembling DFA, using composite states like `'AB'` and `'BC'`.

- **`nfa_dfa_example1.py`**  
  Simulates both an NFA and its equivalent DFA. Checks string acceptance for each.

---

### ✅ DFA Examples

- **`dfa_example1.py`**  
  DFA for strings that **start with '0'**.

- **`dfa_example2.py`**  
  DFA that accepts **only binary strings of exactly length 2**.

- **`dfa_example3.py`**  
  DFA that **rejects strings containing 'aabb'**.

- **`dfa_example4.py`**  
  DFA that accepts strings that either contain **'01'** or **a '1' followed by a '0'**.

---

### ⚙️ Mealy Machine

- **`twos_complement_mealy_machine.py`**  
  Computes **two's complement** of a binary number using a Mealy machine-like approach.

---

### 🧠 Marble Rolling Toy Models

- **`Marble Rolling Toy State Table.py`**  
  Generates all transitions of a marble toy system using binary lever states. Outputs a CSV file.

- **`2.2.1.52.MarbleDFA.py`**  
  Simulates a DFA using lever states (e.g., `'000r'`, `'101a'`) to represent positions. Accepts `'A'` or `'B'` inputs and tracks lever state transitions interactively.

- **`Pre-Switch Marble Rolling Toy Table.py`**  
  Models state transitions **before the marble drops**, including path logic like `"A -> x1 -> D"`. Outputs a transition table as CSV.

---

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Open terminal and run any script:
   ```bash
   python dfa_example1.py
   ```
3. Most scripts prompt for input strings like '010', 'abba', or 'AABB'.

💡 Educational Goals
Understand how DFAs and NFAs process strings.

Explore conversion between NFA and DFA.

Simulate real-world inspired state machines like a marble toy.

Practice working with binary operations using automata principles.