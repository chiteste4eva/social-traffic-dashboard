# Social Media Traffic Analysis (Tableau)

An end-to-end analytics project on **10,000 social media posts** across four platforms
(YouTube, Instagram, Medium, LinkedIn) over 2025 — comparing traffic volume, engagement,
content formats, and what makes a post go viral.

## Tableau Dashboard
🔗 **Live on Tableau Public:**
https://public.tableau.com/views/Social_Media_Traffic_Analysis_2025/Dashboard1

## Dataset
- File: `social_media_performance.csv` (10,000 rows, 15 columns)
- Source: Open data (Kaggle — Social Media Performance and Engagement Data)
- Key fields: `platform`, `content_type`, `topic`, `post_datetime`, `views`,
  `likes`, `comments`, `shares`, `engagement_rate`, `is_viral`, `sentiment_score`

## Key Insights
- **YouTube dominates traffic** — 1.29B views (60% of total), 516K avg views/post.
- **Instagram wins engagement** — highest engagement rate (0.15) and viral rate (67%),
  despite lower total traffic than YouTube.
- **Video is king** — highest average views of any content type (433K/post).
- **Traffic peaked in August 2025** (205M views); topics are evenly spread with
  Sports, Entertainment, and Technology leading.
- **Viral posts get 3x the likes and shares** of non-viral posts — but similar view
  counts, so engagement depth, not reach, separates them.
- Sentiment is only weakly correlated with engagement (0.21) — format and platform
  matter more than tone.

## Tools Used
- Python (pandas, matplotlib) — data cleaning & exploratory analysis
- Tableau Public — interactive dashboard
- GitHub — project hosting

## Files
| File | Description |
|---|---|
| `social_media_performance.csv` | Raw dataset (10,000 posts) |
| `analysis.py` | Python EDA script (reproduces all findings & charts) |
| `chart_traffic_by_platform.png` | Total views by platform |
| `chart_monthly_trend.png` | Monthly traffic trend |
| `chart_engagement_by_platform.png` | Engagement rate by platform |

## How to Reproduce
```bash
pip install pandas matplotlib
python analysis.py
```
