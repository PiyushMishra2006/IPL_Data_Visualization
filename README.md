# IPL 2025 Data Analysis & Visualization using Pandas + Matplotlib

A beginner-to-intermediate data visualization project built using **Pandas** and **Matplotlib** on IPL 2025 batting and bowling datasets.  
The project explores player and team performances through various graph types while learning core Matplotlib concepts step by step.

---

## Project Objective

The goal of this project is to:

- Practice real-world data analysis using IPL datasets
- Learn Matplotlib from basics to advanced plotting
- Understand when and why different visualizations are used
- Interpret cricket statistics using graphs
- Build strong visualization skills for Data Science projects

---

## Dataset Used

### Files

- `IPL2025Batters.csv`
- `IPL2025Bowlers.csv`

### Batting Features

- Player
- Team
- Runs
- Matches
- Innings
- Average
- Balls Faced
- Strike Rate
- Hundreds
- Fifties
- Fours
- Sixes

### Bowling Features

- Player
- Team
- Wickets
- Overs
- Economy
- Strike Rate
- Average
- Runs Conceded
- Best Bowling Figures

---

## Libraries Used

```python
import pandas as pd
import matplotlib.pyplot as plt
```

---

# Visualizations Performed

## 1. Bar Plots

### Insights:

- Top 10 run scorers
- Top wicket takers
- Team-wise total runs
- Most sixes

Concepts learned:

- `plt.bar()`
- annotations using `plt.text()`
- grids
- labels
- figure sizing

---

## 2. Horizontal Bar Plots

Used for:

- Highest strike rate players
- Best economy bowlers

Concepts:

- `plt.barh()`
- horizontal comparison

---

## 3. Histograms

Used for:

- Distribution of player runs

Concepts:

- frequency distribution
- bins
- histogram interpretation

---

## 4. Scatter Plots

Used for:

- Runs vs Strike Rate

Concepts:

- relationship between variables
- trend analysis

---

## 5. Advanced Scatter Customization

Added:

- Marker size → Number of sixes
- Marker color → Batting average
- Player labels
- Transparency (`alpha`)
- Colorbar

---

## 6. Subplots

Combined multiple graphs together for comparison:

- Top scorers
- Top wicket takers

Concepts:

- `plt.subplots()`
- multiple graph layouts

---

## 7. Correlation Heatmap

Analyzed relationships between numerical batting features.

Concepts:

- correlation matrix
- `imshow()`
- colorbars

---

## 8. Box Plots

Used for:

- Runs distribution
- Economy distribution
- Multi-box comparison

Concepts:

- Median
- Quartiles
- Outliers
- IQR

---

## 9. Pie Charts

Used for:

- Team-wise run contribution
- Boundary contribution (4s)

Concepts:

- percentage contribution
- proportional analysis

---

## 10. Line Plots

Used for:

- Top run scorers
- Top wicket takers

Concepts:

- trend visualization
- progression analysis

---

## 11. Stacked Bar Charts

Used for:

- Runs contributed through 4s and 6s

Concepts:

- composition analysis
- stacked comparisons

---

## 12. Legends, Grids & Layouts

Learned:

- `plt.legend()`
- `plt.grid()`
- `plt.tight_layout()`
- tick rotation
- readability improvements

---

# Key Insights Observed

Some observations from visualizations:

- A small group of batters contributed disproportionately high runs.
- Strike rates vary significantly among top players.
- Economy rates among bowlers were comparatively concentrated.
- Elite performers often appear as outliers in boxplots.
- Boundary contribution differs between anchor batters and power hitters.
- Team run contributions are uneven across the tournament.

---

# Project Structure

```bash
IPL-2025-Matplotlib-Analysis/
│
├── IPL2025Batters.csv
├── IPL2025Bowlers.csv
├── analysis.py
├── output_images/
│      ├── top_runs.png
│      ├── wickets.png
│      ├── heatmap.png
│      └── ...
│
└── README.md
```

---

# Skills Practiced

### Python

- Pandas
- Data Cleaning
- Data Transformation
- Sorting
- Filtering
- Grouping

### Visualization

- Matplotlib basics
- Statistical plots
- Trend analysis
- Distribution analysis
- Dashboard thinking

---

# Learning Roadmap Completed

✅ Bar plots  
✅ Horizontal bar plots  
✅ Histograms  
✅ Scatter plots  
✅ Subplots  
✅ Correlation matrix  
✅ Box plots  
✅ Pie charts  
✅ Line plots  
✅ Stacked bar charts  
✅ Advanced scatter customization  
✅ Legends & Layouts  

---

# Future Improvements

Possible additions:

- Seaborn visualizations
- Plotly interactive dashboards
- IPL player comparison dashboard
- Team-wise performance dashboards
- Match-wise analysis
- Streamlit deployment

---

## Author

**Piyush Mishra**

Learning Data Analysis, Visualization and Python through project-based practice.
