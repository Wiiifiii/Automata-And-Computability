# Finite State Machine Prerequisites

## Introduction to Basic Concepts

### Symbols, Alphabet, Strings, and Languages

- **Symbol**: A symbol is the most basic element of language computation. Examples of symbols include characters like 'a', 'b', 'c', digits like '0', '1', '2', and so forth.
- **Alphabet**: An alphabet, denoted as \( \Sigma \), is a collection of symbols. For instance, \( \Sigma = \{0, 1\} \) represents a binary alphabet.
- **String**: A string is a finite sequence of symbols from an alphabet. For example, '00', '01', '10', '11' are strings over the alphabet \( \Sigma = \{0, 1\} \).
- **Language**: A language is a set of strings, typically defined over an alphabet. Languages can be finite or infinite depending on their definition.

### Sets of Strings

- **\( L_1 \)**: Set of all strings of length 2.
  - Example: \( L_1 = \{00, 01, 10, 11\} \)
- **\( L_2 \)**: Set of all strings of length 3.
  - Example: \( L_2 = \{000, 001, 010, 011, 100, 101, 110, 111\} \)
- **\( L_3 \)**: Set of all strings that begin with '0'.
  - Example: \( L_3 = \{0, 00, 01, 000, 001, 010, 011, \ldots\} \)

### Powers of Alphabet \( \Sigma \)

The powers of an alphabet \( \Sigma \) describe sets of strings of certain lengths:

- **\( \Sigma^0 \)**: Set of all strings of length 0 (only the empty string \( \epsilon \)).
- **\( \Sigma^1 \)**: Set of all strings of length 1.
- **\( \Sigma^2 \)**: Set of all strings of length 2.
- **\( \Sigma^n \)**: Set of all strings of length \( n \).

### Cardinality

The cardinality of a set indicates the number of elements in that set. For a finite alphabet \( \Sigma \):
- \( |\Sigma^n| = 2^n \) for a binary alphabet where \( n \) is the length of the strings.

### Kleene Star

The Kleene Star of an alphabet \( \Sigma \), denoted \( \Sigma^* \), is the set of all possible strings of all lengths over \( \Sigma \), including the empty string \( \epsilon \).
- Example: \( \Sigma^* = \{\epsilon, 0, 1, 00, 01, 10, 11, \ldots\} \)

## Conclusion

These foundational concepts form the prerequisites necessary for understanding finite state machines and their applications in computing various languages.
