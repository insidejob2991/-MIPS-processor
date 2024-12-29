# -MIPS-processor
Python-based emulator for a custom MIPS processor designed to perform:  Sum of N Natural Numbers Fibonacci Sequence Generation Counting Occurrences of a Number in a List The project simulates MIPS-like architecture with instruction-based logic, registers, and memory handling. Ideal for learning MIPS concepts and experimenting with algorithm
This Python-based custom MIPS processor emulates the behavior of a simple instruction-based architecture to perform specific computations. It is designed to handle three primary operations:

Sum of N Natural Numbers

Calculates the sum of the first N natural numbers.
Implements a loop-based approach, adhering to MIPS-like assembly logic.
Fibonacci Sequence Generation

Computes the Fibonacci sequence up to a given term (N).
Uses iterative logic to efficiently simulate Fibonacci calculations within the MIPS paradigm.
Counting Total Occurrences of a Number in a List

Searches a list for all occurrences of a given number.
Mimics instruction-based iteration over the list, incrementing a counter for each match.
Features:

Instruction Set Emulation: Core instructions like LOAD, STORE, ADD, SUB, BEQ (Branch if Equal), and loops are simulated in Python.
Register-Based Architecture: Includes a set of registers ($t0, $t1, etc.) to store intermediate values during computation.
Memory Management: Utilizes Python lists to emulate memory storage for input data and results.
Control Flow: Implements branching and looping using conditional statements, imitating MIPS assembly logic.
Use Cases:
This custom processor can serve as:

A learning tool for understanding MIPS assembly by simulating instructions and control flow.
A practical example of embedding algorithmic logic into low-level architecture.
A demonstration of how high-level programming can emulate low-level hardware behavior.
Input/Output Examples:

Sum of N Numbers: Input: N = 10; Output: Sum = 55.
Fibonacci Sequence: Input: N = 5; Output: [0, 1, 1, 2, 3].
Count Occurrences: Input: List = [1, 2, 3, 1, 4], Target = 1; Output: Count = 2.
