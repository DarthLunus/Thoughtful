Thoughtful Package Sort
=========================

This project simulates the behavior of a robotic arm in **Thoughtful's** automated factory, sorting packages based on their dimensions and mass.

Objective:
----------
Classify packages into three categories:

1. STANDARD: Packages that are **neither heavy nor bulky**.
2. SPECIAL: Packages that are **either heavy OR bulky**.
3. REJECTED: Packages that are **both heavy AND bulky**.

Classification Rules:
---------------------
- A package is **bulky** if:
  - Volume ≥ 1,000,000 cm³ (width * height * length), **OR**
  - Any dimension ≥ 150 cm.
  
- A package is **heavy** if:
  - Mass ≥ 20 kg.

Project Structure:
------------------
- sort.py     # Package classification logic
- main.py       # Script to test packages with examples
- .venv/        # Python virtual environment (optional)

How to Use:
-----------
1. Clone the repository:

   git clone https://github.com/your-username/thoughtful-package-sorter.git
   cd thoughtful-package-sorter

2. Create and activate a virtual environment (optional, but recommended):

   python -m venv .venv
   source .venv/bin/activate      # Linux/macOS
   # or
   .venv\Scripts\activate         # Windows

3. Run the test script:

   python main.py

Example Output:
---------------
Package 1: {'width': 30, 'height': 40, 'length': 50, 'mass': 5, 'classification': 'STANDARD'}
Package 2: {'width': 160, 'height': 30, 'length': 40, 'mass': 10, 'classification': 'SPECIAL'}
Package 5: {'width': 100, 'height': 100, 'length': 100, 'mass': 25, 'classification': 'REJECTED'}
...

Technologies:
-------------
- Python 3.10+
- Typing with `typing`
- Object-Oriented Programming

Evaluation Criteria Met:
-------------------------
- Clear and correct classification logic
- Use of good practices with classes and methods
- Coverage of cases with sample data
- Separation of responsibilities (validation, structure, main function)

License:
--------
This project is for technical evaluation purposes only.
