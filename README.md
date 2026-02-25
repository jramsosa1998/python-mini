# Python Mini-Projects

Small Python scripts demonstrating:
- Input/output
- Loops and lists
- Accumulators 
- Functions
- Git version control

Built as part of a structured software engineering refresh.

---

## Bears vs Rams Player Prop Analysis

This project contains my analysis of player prop predictions for the **Bears vs Rams divisional playoff game (January 18, 2026)**. The notebook tracks baseline sportsbook lines, applies intuition-based adjustments, and evaluates the accuracy of predictions.

**Highlights:**
- Baseline props and probabilities are documented before late-week injuries and market movements.
- Adjustments reflect matchups, target distribution, and game-flow expectations.
- Final picks summary:
  - **Swift Rushing Yards:** UNDER (Adjusted 40%)
  - **Loveland Receptions:** UNDER (Adjusted 45%)
  - **Loveland Receiving Yards:** OVER (Adjusted 65%)
  - **Puka Receptions:** UNDER (Adjusted 42%)
- Prediction accuracy: **2/4 props matched postgame outcomes**, with Swift’s rushing yard line slightly exceeded due to overtime volume and weather factors.

**Analysis Notes:**
- Swift under expected due to Rams interior defense, volume, and prior game trends.
- Loveland receiving yards over expected from explosive plays; receptions under expected due to volume split across Bears’ weapons.
- Puka receptions under expected due to Bears defensive focus and snow conditions impacting target distribution.

**View Notebook:**  
[![View Notebook](https://img.shields.io/badge/View-Notebook-blue?logo=jupyter)](https://nbviewer.org/format/script/github/jramsosa1998/python-mini/blob/main/Player_props_project/Player_BearsRamsprops_ipynb.ipynb)



### Seahawks vs Rams — Player Prop Analysis (Iteration II)

Iteration II expands the foundational tracking system built in Project I by introducing:

- Script-based modeling  
- Baseline line freeze tracking  
- Market movement logging  
- Structured postgame grading  
- Variance classification  

This project strengthens analytical discipline while maintaining a focused prop sample.  
Prop tier exposure and portfolio structuring are introduced in Iteration III (Super Bowl Case Study).

---

# Project Objective

To evaluate player props using a structured decision-quality framework that separates:

- Outcome accuracy (HIT / MISS)
- Thesis correctness
- Variance vs misread

Core evaluation pillars:

- Volume trends  
- Game script probability  
- Defensive tendencies  
- Market behavior  
- Postgame structural validation  

This is a process-driven evaluation system — not a picks sheet.

---

# Pregame Script Model

Primary assumptions entering the slate:

- Seahawks projected positive game script  
- Rams increased dropback probability under negative script  
- Defensive shell tendencies impacting short-area and RB receiving usage  
- Volume stability prioritized over efficiency volatility  

Each prop was evaluated relative to these assumptions.

---

# Results Summary

Total Props: **4**  
Correct Hits: **3**  
Hit Rate: **75%**

OVER Props Correct: **2**  
UNDER Props Correct: **1**

Two selections favored players on the losing team, challenging the market assumption that props on trailing teams are inherently weaker.

---

# Miss Classification

Misses were driven by:

- Unexpected target distribution  
- Role-based usage variance  

Importantly:

The miss reflected a shift in usage structure — not a breakdown in matchup logic.

This reinforces the distinction between:

- **Wrong outcome**
- **Wrong thesis**

Iteration II emphasizes evaluating decision quality independent of final stat variance.

---

# Key Takeaways

- Volume and matchup-based analysis can outperform market script bias  
- Props on losing teams can remain viable when usage remains stable  
- Efficiency-based expectations are less reliable than role stability  
- Separating team outcome from player usage improves analytical clarity  

The 3/4 performance — including two props on the losing team — supports the repeatability of the process under varied script conditions.

---

# Evolution → Iteration III (Super Bowl Case Study)

Iteration III formalizes this model into a capped portfolio case study introducing:

- Tier classification (Core / Divergence / Median / Boom)  
- Fixed prop cap (10–12 maximum)  
- Exposure control  
- Edge-type categorization  
- Portfolio-level performance grading  
- Structured markdown postgame summary  

The Seahawks vs Rams project serves as the refinement phase before full portfolio implementation.

---

# Tech Stack

- Python  
- Pandas  
- Jupyter Notebook  

---

# How To Run

1. Clone the repository  
2. Open:

   `Player_props_project/Seahawks_Rams_Props_ipynb.ipynb`

3. Run cells sequentially  
4. Update postgame grading fields manually  

---

Author: Jesse  
Project Type: Structured Analytical Development  
Iteration: II  
Accuracy: 75%
