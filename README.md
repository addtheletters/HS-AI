# HS-AI
Code written for the TJHSST Artificial Intelligence class, here for archival purposes.

Divided by the quarter of the school year in which it was written.

## 1: finding and searching
- implementation of 3-element vectors in vector.py
- DFS and BFS graph navigation in routes.py
- 2D graphics done with tkinter
- [A* / A Star pathfinding](https://en.wikipedia.org/wiki/A*_search_algorithm) in astar.py
- [Nelder-Mead downhill simplex method](https://en.wikipedia.org/wiki/Nelder%E2%80%93Mead_method) in labnmead.py

## 2: AI for solving / playing games
- Converting repeating decimals to fractions in recurringdecimal.py
- AI that plays [Ghost](https://en.wikipedia.org/wiki/Ghost_(game)) in ghost.py
- AI that plays [Othello / Reversi](https://en.wikipedia.org/wiki/Reversi) in revised_othello1.py. (Older versions also present.) Uses methods such as
    - N-ply [minimax](https://en.wikipedia.org/wiki/Minimax) decision making
    - [Alpha-beta](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning) pruning
- Solving [Sudokus](http://i.imgur.com/fs3Lkmj.png) in sudokusolver.py
- Fast word lookups with a [trie](https://en.wikipedia.org/wiki/Trie) in trie.py
- Generating from [Wolfram's Elementary Cellular Automata Rules](https://en.wikipedia.org/wiki/Elementary_cellular_automaton) in cellular.py

## 3: machine vision and image manipulation
- In machinevision.py:
    - [Gaussian Smoothing](https://en.wikipedia.org/wiki/Gaussian_blur)
    - [Thresholding](https://en.wikipedia.org/wiki/Thresholding_(image_processing))
    - [Sobel Transfrom](https://en.wikipedia.org/wiki/Sobel_operator)
    - [Canny Edge Detection](https://en.wikipedia.org/wiki/Canny_edge_detector)
- Detecting lines with [Hough Transform](https://en.wikipedia.org/wiki/Hough_transform) in houghtransform.py
- Monte-Carlo experiment on unique birthdays in uniquebirthdays.py

## 4: neural networks, genetic algorithms, and miscellaneous problems
- [Hillclimbing](https://en.wikipedia.org/wiki/Hill_climbing) to solve the [N-Queens problem](https://en.wikipedia.org/wiki/Eight_queens_puzzle) in nqueens.py
- Self-teaching / dynamically learning Tic-Tac-Toe AI in tictak.py
- Simple neural networks of various sorts, touching on
    - [Feed forward](https://en.wikipedia.org/wiki/Feedforward_neural_network) in ann4.py, feedfowrard.py
    - [Back propagation](https://en.wikipedia.org/wiki/Backpropagation) in ann5.py
- Setup for some simple [genetic algorithm](https://en.wikipedia.org/wiki/Genetic_algorithm) generation simulation in genetic2.py

## Permutations unit
One unit was focused around permutations; these files have been split off in a separate folder.
- Basic permutations in nthPermBasic.py
- Navigating [lexicographic permuatations](https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order) (given the nth, calculate the n+1th) in perms.py and nextPermLexi.py
- [Alphametics](https://en.wikipedia.org/wiki/Verbal_arithmetic) puzzle solver using permutations in solver.py
