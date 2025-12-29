# # Social Traffic Dashboard (Tableau)

## Overview
This project analyzes monthly social media traffic across four platforms:
- LinkedIn
- Instagram
- Twitter
- Substack

The goal is to compare traffic trends over time and identify growth patterns and spikes by platform.

## Dataset
- File: `social_traffic.csv`
- Source: Provided CSV dataset for the assignment
- Schema:
  - **month** → Date (Dimension)
  - **platform** → Categorical field (Dimension)
  - **traffic** → Numeric count of visits (Measure)

### Dimensions vs Measures
- **Dimensions** describe *when* or *what category* the data belongs to (e.g., month, platform).
- **Measures** are numeric values that can be aggregated (e.g., total traffic).

## Tableau Dashboard
🔗 **Live Tableau Public Link:**  
https://public.tableau.com/views/Social_Traffic_Dashboard/Dashboard1?publish=yes

## Visualizations
- Four time-series line charts (small multiples)
- Each chart shows monthly traffic for one platform
- Shared time axis for easy comparison

## Key Insights
- LinkedIn shows explosive growth in late 2022 with a peak in December.
- Instagram grows steadily with a sharp increase in early 2023.
- Twitter spikes in late 2022 and fluctuates afterward.
- Substack begins mid-2022, peaks in August, then gradually declines.

## Tools Used
- Tableau Public
- CSV dataset
- GitHub

## Author
Joseph Nwankwo Chibuzo
