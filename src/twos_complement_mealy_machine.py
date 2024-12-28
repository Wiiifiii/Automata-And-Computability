def twos_complement_mealy_machine(binary_input):
    # Define states
    STATE_INITIAL = 0
    STATE_PROCESS = 1
    STATE_ADD_ONE = 2
    STATE_END = 3

    # Start state
    state = STATE_INITIAL
    inverted_bits = ""
    result = ""

    # State machine to invert bits
    for bit in binary_input:
        if state == STATE_INITIAL or state == STATE_PROCESS:
            state = STATE_PROCESS
            inverted_bits += '1' if bit == '0' else '0'  # Invert bits
    
    # Transition to Add One state
    state = STATE_ADD_ONE
    carry = 1  # We start with adding one

    # Add one to the inverted binary string
    for bit in reversed(inverted_bits):
        if state == STATE_ADD_ONE:
            if bit == '1' and carry == 1:
                result = '0' + result
                carry = 1  # Carry remains 1
            elif bit == '0' and carry == 1:
                result = '1' + result
                carry = 0  # Carry is consumed
            else:
                result = bit + result  # No carry addition

    # Check if there's any remaining carry
    if carry == 1:
        result = '1' + result

    state = STATE_END  # Transition to end state

    return result

# Request user input for the binary number
binary_input = input("Please enter a binary number: ")

# Validate the input to make sure it's a binary string
if all(c in '01' for c in binary_input):
    twos_complement = twos_complement_mealy_machine(binary_input)
    print(f"Original binary: {binary_input}")
    print(f"Two's complement: {twos_complement}")
else:
    print("Invalid input! Please make sure to enter a valid binary number (only 0s and 1s).")
