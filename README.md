# Procrastination Detector – DSA Behavior Analyzer

### 🎯 Overview
An analytical tool that quantifies productivity by comparing a user's **intended priority** against their **actual execution sequence**. It identifies "Priority Inversion"—when low-value tasks are prioritized over high-stakes goals.

### 🧠 DSA Concepts
- **Priority Queue (Min-Heap):** Used to determine the mathematically optimal task order.
- **Vectors/Lists:** To maintain the historical timeline of user actions.
- **Sorting Algorithms:** To align execution timestamps for comparison.
- **File I/O:** JSON (Python) and Stream processing (C++) for persistent storage.

### 🚀 How to Run
1. **Python:** Run `python main.py`. Requires no external libraries.
2. **C++:** Compile with `g++ main.cpp -o detector` and run `./detector`.

### 📊 Scoring Logic
The **Procrastination Score** is calculated by $S = \sum (P_{actual} - P_{ideal}) \times 10$, where $P$ represents the numerical priority value.