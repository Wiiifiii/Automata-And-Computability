# Finite Automata Overview

## NFA - Non-deterministic Finite Automata

### Deterministic Finite Automata (DFA)
- **Determinism**:
  - In DFA, given the current state, we know what the next state will be.
  - It has only one unique next state.
  - It has no choices or randomness.
  - It is simple and easy to design.

### Diagram for DFA:
A -> 1 -> B A -> 0 -> C C -> 1 -> D C -> 0 -> A D -> 1 -> B

## Formal Definition of NFA

Given the following NFA settings:
- **Q**: Set of all states = {A, B}
- **Σ**: Inputs = {0, 1}
- **q0**: Start state = A
- **F**: Set of final states = {B}
- **δ**: Transition function

Transitions:
| Current State | Input 0 | Input 1 | Epsilon |
|---------------|---------|---------|---------|
| A             | A, B    | A       | B       |
| B             | ∅       | ∅       | ∅       |

## Regular Languages

- A language is said to be a **REGULAR LANGUAGE** if and only if some Finite State Machine recognizes it.
- **Not Regular**: Languages which are not recognized by any FSM, require memory, or FSM's memory is very limited to store or count strings.

## Operations on Regular Languages

- **UNION**:
  - A ∪ B = { x | x ∈ A or x ∈ B }
- **CONCATENATION**:
  - A ⋅ B = { xy | x ∈ A and y ∈ B }
- **STAR**:
  - A* = { x, xx, xxx... | x ∈ A }

## Theorems on Regular Languages
- **Theorem 1**: The class of Regular Languages is closed under UNION.
- **Theorem 2**: The class of Regular Languages is closed under CONCATENATION.
