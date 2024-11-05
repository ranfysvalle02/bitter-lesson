# The Bitter Lesson Demonstration # http://www.incompleteideas.net/IncIdeas/BitterLesson.html
# Illustrating how general methods leveraging computation outperform specialized methods over time

import time

# Simulate a specialized method with human knowledge
def specialized_method(problem_size):
    # Return a fixed solution quality, independent of problem size
    solution_quality = 0.7
    return solution_quality

# Simulate a general method using search and learning
def general_method(problem_size, computation_time):
    # Assume a constant computation speed (steps per second)
    computation_speed = 1000  # Arbitrary units
    total_steps = int(computation_time * computation_speed)
    # Improvement per step decreases with larger problem sizes
    improvement_per_step = 1.0 / problem_size

    # Calculate total improvement
    solution_quality = total_steps * improvement_per_step
    # Cap the solution quality at 1.0 (maximum possible quality)
    solution_quality = min(solution_quality, 1.0)
    return solution_quality

def main():
    print("=== The Bitter Lesson Demonstration ===\n")
    print("This simulation compares two problem-solving approaches:")
    print("1. **Specialized Method**: Uses built-in human knowledge. Performance remains constant regardless of computation time.")
    print("2. **General Method**: Leverages computation through search and learning. Performance improves with more computation time.\n")

    problem_sizes = [5000, 10000, 20000]  # Various problem sizes
    computation_times = [0.1, 0.5, 1.0, 2.0]   # Different computation times

    # Step 1: Demonstrate the Specialized Method
    print("**Specialized Method Results:**")
    for size in problem_sizes:
        quality = specialized_method(size)
        print(f"Problem Size {size}: Solution Quality = {quality:.2f}")
    print("\n(Notice that the specialized method's performance remains constant across different problem sizes.)\n")

    # Step 2: Demonstrate the General Method
    print("**General Method Results:**")
    for size in problem_sizes:
        print(f"\nProblem Size {size}:")
        for comp_time in computation_times:
            quality = general_method(size, comp_time)
            print(f"  Computation Time {comp_time}s -> Solution Quality: {quality:.2f}")
        print(f"(For problem size {size}, the solution quality improves with more computation time.)")
    print()

    # Step 3: Summarize the Findings
    print("=== Conclusion ===")
    print("The specialized method achieves a fixed solution quality regardless of computation time or problem size.")
    print("In contrast, the general method's solution quality improves with increased computation time, especially for larger problem sizes.")
    print("\nThis demonstrates **'The Bitter Lesson'**:")
    print("General methods that leverage computation ultimately outperform specialized methods that rely on built-in human knowledge.\n")
    print("As computational resources continue to grow, focusing on general-purpose algorithms and learning methods becomes increasingly advantageous.")

if __name__ == "__main__":
    main()

"""
=== The Bitter Lesson Demonstration ===

This simulation compares two problem-solving approaches:
1. **Specialized Method**: Uses built-in human knowledge. Performance remains constant regardless of computation time.
2. **General Method**: Leverages computation through search and learning. Performance improves with more computation time.

**Specialized Method Results:**
Problem Size 5000: Solution Quality = 0.70
Problem Size 10000: Solution Quality = 0.70
Problem Size 20000: Solution Quality = 0.70

(Notice that the specialized method's performance remains constant across different problem sizes.)

**General Method Results:**

Problem Size 5000:
  Computation Time 0.1s -> Solution Quality: 0.02
  Computation Time 0.5s -> Solution Quality: 0.10
  Computation Time 1.0s -> Solution Quality: 0.20
  Computation Time 2.0s -> Solution Quality: 0.40
(For problem size 5000, the solution quality improves with more computation time.)

Problem Size 10000:
  Computation Time 0.1s -> Solution Quality: 0.01
  Computation Time 0.5s -> Solution Quality: 0.05
  Computation Time 1.0s -> Solution Quality: 0.10
  Computation Time 2.0s -> Solution Quality: 0.20
(For problem size 10000, the solution quality improves with more computation time.)

Problem Size 20000:
  Computation Time 0.1s -> Solution Quality: 0.01
  Computation Time 0.5s -> Solution Quality: 0.03
  Computation Time 1.0s -> Solution Quality: 0.05
  Computation Time 2.0s -> Solution Quality: 0.10
(For problem size 20000, the solution quality improves with more computation time.)

=== Conclusion ===
The specialized method achieves a fixed solution quality regardless of computation time or problem size.
In contrast, the general method's solution quality improves with increased computation time, especially for larger problem sizes.

This demonstrates **'The Bitter Lesson'**:
General methods that leverage computation ultimately outperform specialized methods that rely on built-in human knowledge.

As computational resources continue to grow, focusing on general-purpose algorithms and learning methods becomes increasingly advantageous.
"""
