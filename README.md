<h1>
  <img src="https://upload.wikimedia.org/wikipedia/commons/e/e0/Sudoku_Puzzle_by_L2G-20050714_standardized_layout.svg" 
       alt="Sudoku Logo" 
       style="height: 40px; vertical-align: middle">
  Solving Sudoku Using an Evolutionary Algorithm
</h1>

This repository contains a Python-based implementation of solving Sudoku puzzles using evolutionary algorithms. Evolutionary algorithms are inspired by natural selection and are used to find near-optimal solutions to optimization problems.

## Introduction

Sudoku is a popular number puzzle game. This project takes an innovative approach by using evolutionary algorithms to solve Sudoku puzzles. Rather than brute-forcing through possible solutions, the algorithm simulates the process of natural selection to iteratively improve potential solutions.

## Features

- Solve Sudoku puzzles using evolutionary concepts like mutation and crossover.
- Configurable parameters for the evolutionary process (e.g., population size, mutation rate).
- An intuitive interface for providing Sudoku puzzles as input.
- Detailed logging of the solving process.

## Installation

1. Clone the repository:
   ```bash
     git clone https://github.com/ridakhann/solving-suduko-using-evolutionary-algorithm.git
2. Navigate to the project directory:
   ```bash
    cd solving-suduko-using-evolutionary-algorithm
### How It Works

The evolutionary algorithm used in this project typically involves the following steps:

1. **Initialization**: Generate an initial population of random Sudoku grids.
2. **Fitness Evaluation**: Assign a fitness score to each grid based on how close it is to being a valid solution.
3. **Selection**: Select the fittest grids to be parents for the next generation.
4. **Crossover**: Combine parent grids to create offspring grids.
5. **Mutation**: Introduce small random changes to offspring grids to maintain genetic diversity.
6. **Repeat**: Iterate through generations until a valid solution is found or a stopping condition is met.

<h2>Examples</h2>

<h3>Input Puzzle</h3>
<pre>
5 3 _ | _ 7 _ | _ _ _ 
6 _ _ | 1 9 5 | _ _ _ 
_ 9 8 | _ _ _ | _ 6 _ 
------+-------+------
8 _ _ | _ 6 _ | _ _ 3 
4 _ _ | 8 _ 3 | _ _ 1 
7 _ _ | _ 2 _ | _ _ 6 
------+-------+------
_ 6 _ | _ _ _ | 2 8 _ 
_ _ _ | 4 1 9 | _ _ 5 
_ _ _ | _ 8 _ | _ 7 9 
</pre>

<h3>Output Puzzle</h3>
<pre>
5 3 4 | 6 7 8 | 9 1 2 
6 7 2 | 1 9 5 | 3 4 8 
1 9 8 | 3 4 2 | 5 6 7 
------+-------+------
8 5 9 | 7 6 1 | 4 2 3 
4 2 6 | 8 5 3 | 7 9 1 
7 1 3 | 9 2 4 | 8 5 6 
------+-------+------
9 6 1 | 5 3 7 | 2 8 4 
2 8 7 | 4 1 9 | 6 3 5 
3 4 5 | 2 8 6 | 1 7 9 
</pre>

<h2>File Structure</h2>
<ul>
  <li><strong>main.py</strong>: Entry point of the application; orchestrates the solving process.</li>
  <li><strong>EA.py</strong>: Contains the implementation of the evolutionary algorithm.</li>
  <li><strong>sudoko.py</strong>: Handles Sudoku puzzle representation and related utility functions.</li>
  <li><strong>grid1_50.txt</strong>, <strong>grid2_17.txt</strong>, <strong>grid3_27.txt</strong>: Sample Sudoku puzzles with varying difficulty levels.</li>
</ul>

<h2>Contributing</h2>
<p>Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.</p>
