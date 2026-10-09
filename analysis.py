"""
Social Media Traffic Analysis — 2025
Dataset: social_media_performance.csv (10,000 posts, open data via Kaggle)
Author: Joseph Nwankwo
"""
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

df = pd.read_csv("social_media_performance.csv")
df["post_datetime"] = pd.to_datetime(df["post_datetime"])
df["month"] = df["post_datetime"].dt.to_period("M").astype(str)

print(f"Posts: {len(df):,} | {df['post_datetime'].min().date()} -> {df['post_datetime'].max().date()}")
print(f"Platforms: {sorted(df['platform'].unique())}")

# 1. Traffic by platform
traffic = df.groupby("platform")["views"].agg(["sum", "mean", "count"])
traffic.columns = ["total_views", "avg_views", "posts"]
print("\n--- Traffic by platform ---")
print(traffic.sort_values("total_views", ascending=False).round(1).to_string())

# 2. Engagement by platform
eng = df.groupby("platform")["engagement_rate"].mean().sort_values(ascending=False)
print("\n--- Avg engagement rate by platform ---")
print(eng.round(3).to_string())

# 3. Content type performance
ct = df.groupby("content_type")["views"].mean().sort_values(ascending=False)
print("\n--- Avg views by content type ---")
print(ct.round(0).to_string())

# 4. Monthly trend
monthly = df.groupby("month")["views"].sum()
print("\n--- Monthly traffic ---")
print(monthly.to_string())
print(f"\nPeak month: {monthly.idxmax()} ({monthly.max():,} views)")

# 5. Viral vs non-viral
print("\n--- Viral vs non-viral ---")
print(df.groupby("is_viral").agg(posts=("views", "size"),
      avg_views=("views", "mean"), avg_likes=("likes", "mean"),
      avg_shares=("shares", "mean")).round(1).to_string())

# 6. Sentiment vs engagement
print("\nSentiment/engagement correlation:",
      round(df[["sentiment_score", "engagement_rate"]].corr().iloc[0, 1], 3))

# Charts
colors = {"YouTube": "#c0392b", "Instagram": "#8e44ad",
          "Medium": "#16a085", "LinkedIn": "#2471a3"}
plt.rcParams.update({"font.size": 11})

g = df.groupby("platform")["views"].sum().sort_values(ascending=False)
fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.bar(g.index, g.values / 1e6, color=[colors[p] for p in g.index])
ax.set_ylabel("Total views (millions)")
ax.set_title("Total Social Media Traffic by Platform (2025)")
for b, v in zip(bars, g.values):
    ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 8,
            f"{v/1e6:.0f}M", ha="center", fontsize=10)
fig.tight_layout(); fig.savefig("chart_traffic_by_platform.png", dpi=120); plt.close(fig)

m = df.groupby("month")["views"].sum()
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(m.index, m.values / 1e6, marker="o", color="#2c3e50", linewidth=2)
ax.set_ylabel("Views (millions)")
ax.set_title("Monthly Social Media Traffic — 2025")
ax.tick_params(axis="x", rotation=45)
fig.tight_layout(); fig.savefig("chart_monthly_trend.png", dpi=120); plt.close(fig)

e = df.groupby("platform")["engagement_rate"].mean().sort_values(ascending=False)
fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.bar(e.index, e.values, color=[colors[p] for p in e.index])
ax.set_ylabel("Avg engagement rate")
ax.set_title("Engagement Rate by Platform")
for b, v in zip(bars, e.values):
    ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 0.002,
            f"{v:.2f}", ha="center", fontsize=10)
fig.tight_layout(); fig.savefig("chart_engagement_by_platform.png", dpi=120); plt.close(fig)

print("\nCharts saved.")
