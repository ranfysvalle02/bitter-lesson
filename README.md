# How Computation Outperforms Human Knowledge

![](https://ginimachine.com/wp-content/uploads/2021/09/Computer-Vs-Human-Which-One-is-Best-for-Risk-Managementpng.png)

Have you ever wondered why artificial intelligence (AI) has made such rapid progress in recent years? A significant part of the answer lies in a concept known as **["The Bitter Lesson,"](http://www.incompleteideas.net/IncIdeas/BitterLesson.html)** introduced by AI researcher Rich Sutton. In this blog post, we'll explore this concept and demonstrate its core principle using a simple Python simulation.

## Understanding "The Bitter Lesson"

At its heart, "The Bitter Lesson" observes that:

> **General methods that leverage computation are ultimately more effective than specialized methods that rely on human knowledge.**

In other words, algorithms that can learn and improve through computation tend to outperform those that depend on hand-crafted human expertise, especially as computational resources grow.

## Problem Solving
![](https://keoughp.wordpress.com/wp-content/uploads/2010/05/flowchart.jpg)

Imagine you're trying to solve a complex problem. There are two main strategies you might use:

1. **Specialized Method:** This approach relies on built-in human knowledge and expertise. It's like having a detailed guide tailored to the problem. While effective up to a point, its performance remains relatively constant, regardless of how much computation time you invest.

2. **General Method:** This strategy leverages computation through search and learning. Think of it as exploring different possibilities and improving through experience. The key here is that performance **improves** with more computational power and time.

## Simulating the Concepts with Python

Let's bring these ideas to life with a Python simulation. We'll compare the specialized and general methods across different problem sizes and computation times.

### The Specialized Method

The specialized method represents algorithms heavily reliant on human-designed features. Its performance is constant, unaffected by additional computation.

```python
def specialized_method(problem_size):
    # Fixed solution quality, independent of problem size
    solution_quality = 0.7
    return solution_quality
```

### The General Method

The general method simulates algorithms that improve through computation, such as machine learning models.

```python
def general_method(problem_size, computation_time):
    # Assume a constant computation speed (steps per second)
    computation_speed = 1000  # Arbitrary units
    total_steps = int(computation_time * computation_speed)
    # Improvement per step decreases with larger problem sizes
    improvement_per_step = 1.0 / problem_size
    # Calculate total improvement
    solution_quality = total_steps * improvement_per_step
    # Cap the solution quality at 1.0 (maximum possible quality)
    return min(solution_quality, 1.0)
```

### Running the Simulation

We'll compare the two methods across various problem sizes and computation times.

```python
def main():
    print("=== The Bitter Lesson Demonstration ===\n")
    print("Comparing Specialized and General Methods in Problem Solving\n")

    problem_sizes = [5000, 10000, 20000]  # Different problem complexities
    computation_times = [0.1, 0.5, 1.0, 2.0]  # Computation times in seconds

    # Specialized Method Results
    print("Specialized Method Results (Constant Performance):")
    for size in problem_sizes:
        quality = specialized_method(size)
        print(f"  Problem Size {size}: Solution Quality = {quality:.2f}")
    print("\n")

    # General Method Results
    print("General Method Results (Performance Improves with Computation):")
    for size in problem_sizes:
        print(f"\nProblem Size {size}:")
        for time in computation_times:
            quality = general_method(size, time)
            print(f"  Computation Time {time}s -> Solution Quality: {quality:.2f}")
        print(f"(Performance improves with more computation time for problem size {size}.)")

    # Conclusion
    print("\n=== Conclusion ===")
    print("The specialized method achieves a fixed solution quality, regardless of computation time or problem size.")
    print("In contrast, the general method's performance improves with increased computation time, especially for larger problems.")
    print("\nThis demonstrates 'The Bitter Lesson' that general methods leveraging computation can ultimately outperform specialized methods.\n")

if __name__ == "__main__":
    main()
```

### Output of the Simulation

When you run the code, you get output like this:

```
=== The Bitter Lesson Demonstration ===

Comparing Specialized and General Methods in Problem Solving

Specialized Method Results (Constant Performance):
  Problem Size 5000: Solution Quality = 0.70
  Problem Size 10000: Solution Quality = 0.70
  Problem Size 20000: Solution Quality = 0.70


General Method Results (Performance Improves with Computation):

Problem Size 5000:
  Computation Time 0.1s -> Solution Quality: 0.02
  Computation Time 0.5s -> Solution Quality: 0.10
  Computation Time 1.0s -> Solution Quality: 0.20
  Computation Time 2.0s -> Solution Quality: 0.40
(Performance improves with more computation time for problem size 5000.)

Problem Size 10000:
  Computation Time 0.1s -> Solution Quality: 0.01
  Computation Time 0.5s -> Solution Quality: 0.05
  Computation Time 1.0s -> Solution Quality: 0.10
  Computation Time 2.0s -> Solution Quality: 0.20
(Performance improves with more computation time for problem size 10000.)

Problem Size 20000:
  Computation Time 0.1s -> Solution Quality: 0.01
  Computation Time 0.5s -> Solution Quality: 0.03
  Computation Time 1.0s -> Solution Quality: 0.05
  Computation Time 2.0s -> Solution Quality: 0.10
(Performance improves with more computation time for problem size 20000.)

=== Conclusion ===
The specialized method achieves a fixed solution quality, regardless of computation time or problem size.
In contrast, the general method's performance improves with increased computation time, especially for larger problems.

This demonstrates 'The Bitter Lesson' that general methods leveraging computation can ultimately outperform specialized methods.
```

### Interpreting the Results

- **Specialized Method:**
  - **Consistent Performance:** The solution quality remains at **0.70** for all problem sizes.
  - **Limitation:** Does not benefit from additional computation time.

- **General Method:**
  - **Performance Scales with Computation:**
    - For **smaller problem sizes**, the solution quality improves more rapidly.
    - For **larger problem sizes**, it takes more computation time to see significant improvements.
  - **Trend:** Given enough computation time, the general method can potentially surpass the specialized method's performance.

### Key Takeaways

- **Scalability:** The general method scales with computation time and problem complexity, making it more adaptable to a variety of problems.
- **Computation as a Resource:** Leveraging computational power allows general methods to explore more possibilities and improve over time.
- **Limitations of Specialized Methods:** While effective in certain contexts, specialized methods are constrained by the extent of human-designed features and cannot easily adapt or improve with additional computation.

## Why Does "The Bitter Lesson" Matter?

As computational resources continue to grow, the advantages of general methods become more pronounced. This has several implications:

- **Artificial Intelligence Development:** Machine learning models, especially deep learning architectures, exemplify the power of general methods. They've achieved remarkable success in areas like image recognition, natural language processing, and game playing by leveraging massive computational resources.
- **Research Focus:** The AI community increasingly prioritizes developing general-purpose algorithms that can learn and adapt, rather than crafting specialized solutions for specific problems.
- **Real-World Applications:** General methods are more flexible and can be applied to a wide range of tasks, making them valuable in dynamic and complex environments.

## Reflecting on the Future of AI

["The Bitter Lesson" ](http://www.incompleteideas.net/IncIdeas/BitterLesson.html)serves as a guiding principle for the future of AI:

- **Embrace Generality:** Focusing on algorithms that can leverage computation to learn and improve is key to advancing AI capabilities.
- **Invest in Computation:** As hardware continues to improve, so does the potential of general methods. Investing in computational infrastructure can yield significant returns.
- **Continual Learning:** General methods often support continual learning, allowing systems to adapt over time without explicit reprogramming.
