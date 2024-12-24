# Regular Languages

A language is said to be a **regular language** if and only if some **Finite State Machine** (FSM) recognizes it.

## What languages are **not regular**?

The languages:
- Which are **not recognized** by any FSM.
- Which **require memory**.

### Memory of FSM:
- The memory of FSM is very limited.
- It cannot store or count strings.

**Examples:**
- `ababbababb`
- `a^n b^n` (example: `aaabbb` or `aaaabbbbb`).

---

# Operations on Regular Languages

### UNION
For two languages `A` and `B`:
- `A ∪ B = { x | x ∈ A or x ∈ B }`

### CONCATENATION
For two languages `A` and `B`:
- `A o B = { xy | x ∈ A and y ∈ B }`

### STAR (Kleene Star)
For a language `A`:
- `A* = { x1, x2, x3, ...., xk | k ≥ 0 and each x ∈ A }`

**Example:**
- `A = { pq, δ }`
- `B = { t, uv }`

Operations on these sets:
- `A ∪ B = { pq, δ, t, uv }`
- `A o B = { pat, pquv, δt, δuv }`
- `A* = { ε, pq, δ, pqpq, δδ, pqpqpq, δδδ, ... }`

---

# Theorems on Regular Languages

### Theorem 1: 
The class of **Regular Languages** is closed under **UNION**.

### Theorem 2: 
The class of **Regular Languages** is closed under **CONCATENATION**.
