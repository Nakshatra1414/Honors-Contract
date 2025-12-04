# Honors-Contract

# Mastermind – Python Implementation (Honors Project)

## Overview
This project is a Python implementation of the classic board game **Mastermind**.  
It was developed as part of my Honors coursework to demonstrate algorithmic thinking, problem-solving, and clean program design.

In Mastermind, one player creates a secret color code and the other attempts to break it using logical reasoning.  
In this version, the **computer acts as the code maker**, and the user plays as the **code breaker**.

---

## How the Game Works
- The computer randomly generates a **4-color secret code**.
- The colors are chosen from the following set:

R, G, B, Y, O, P, W
(Red, Green, Blue, Yellow, Orange, Purple, White)

markdown
Copy code

- Colors **may repeat** in the secret code.
- The player has **10 attempts** to guess the correct sequence.

After each guess, feedback is provided:
- **Correct Position (⚪)** – A color is correct *and* in the right position.
- **Correct Color (🔵)** – A color appears in the secret code but in the wrong position.

The game ends when:
- The player breaks the code *(wins)*, or  
- The player uses all 10 attempts *(loss)*.

---

## Project Purpose
This project demonstrates:
- Input validation  
- Algorithmic decision-making  
- Random generation  
- Game loop logic  
- Avoiding double-counting using list manipulation  
- Clean, modular Python functions  

It also provides a foundation to add additional features such as:
- Graphical user interface (GUI)
- Data visualization of attempts
- Computer AI code-breaking algorithms

---

## Project Structure
mastermind.py # Main game file with all logic
README.md # Project explanation and usage guide

yaml
Copy code

---

## How to Run the Program

### **Prerequisites**
- Python 3 installed on your computer

### **Run from the terminal / command prompt:**
python mastermind.py

markdown
Copy code

### **During the game**
- Enter guesses as 4 letters, e.g.:
RGBY
BYOP
GGGR
