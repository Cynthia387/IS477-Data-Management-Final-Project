import os
import pandas as pd
import matplotlib.pyplot as plt

PROCESSED_DIR = os.path.join("data", "processed")
RESULTS_DIR = os.path.join("results")
FIGURES_DIR = os.path.join(RESULTS_DIR, "figures")
os.makedirs(FIGURES_DIR, exist_ok=True)
INTEGRATED_FILE = os.path.join(PROCESSED_DIR, "calorie_obesity.csv")

def load_data() -> pd.DataFrame:
    if not os.path.exists(INTEGRATED_FILE):
        raise FileNotFoundError(
            f"{INTEGRATED_FILE} not found. Make sure integrate_data.py has been run."
        )
    df = pd.read_csv(INTEGRATED_FILE)
    return df
def compute_global_correlation(df: pd.DataFrame) -> float:
    subset = df[["Calories_per_person", "Obesity_Rate"]].dropna()
    corr = subset["Calories_per_person"].corr(subset["Obesity_Rate"])
    return corr
  
def compute_yearly_correlation(df: pd.DataFrame) -> pd.DataFrame:
    records = []
    for year, group in df.groupby("Year"):
        sub = group[["Calories_per_person", "Obesity_Rate"]].dropna()
        if len(sub) >= 5:
            corr = sub["Calories_per_person"].corr(sub["Obesity_Rate"])
            records.append(
                {"Year": year, "correlation": corr, "n_countries": len(sub)}
            )
    return pd.DataFrame(records).sort_values("Year")

def scatter_calories_vs_obesity(df: pd.DataFrame, year: int | None = None) -> None:
    if year is not None:
        plot_df = df[df["Year"] == year].dropna(
            subset=["Calories_per_person", "Obesity_Rate"]
        )
        title_suffix = f"{year}"
        file_suffix = str(year)
    else:
        plot_df = df.dropna(subset=["Calories_per_person", "Obesity_Rate"])
        title_suffix = "All Years"
        file_suffix = "all_years"

    if plot_df.empty:
        print(f"[WARN] No data available for scatter plot ({title_suffix}).")
        return
    plt.figure(figsize=(8, 6))
    plt.scatter(
        plot_df["Calories_per_person"],
        plot_df["Obesity_Rate"],
        alpha=0.6,
        edgecolor="none",
    )
    plt.xlabel("Daily calories per person")
    plt.ylabel("Adult obesity rate (%)")
    plt.title(f"Calories vs Adult Obesity ({title_suffix})")
    plt.grid(True, linestyle="--", alpha=0.3)

    out_path = os.path.join(
        FIGURES_DIR,
        f"scatter_calories_obesity_{file_suffix}.png",
    )
    plt.tight_layout()
    plt.savefig(out_path, dpi=300)
    plt.close()
    print(f"[INFO] Saved scatter plot to {out_path}")

def line_trend_for_country(df: pd.DataFrame, country: str) -> None:
    country_df = df[df["Entity"] == country].dropna(
        subset=["Calories_per_person", "Obesity_Rate"]
    ).sort_values("Year")

    if country_df.empty:
        print(f"[WARN] No data available for {country}.")
        return

    plt.figure(figsize=(9, 5))
    plt.plot(
        country_df["Year"],
        country_df["Calories_per_person"],
        label="Calories per person",
    )
    ax1 = plt.gca()
    ax2 = ax1.twinx()
    ax2.plot(
        country_df["Year"],
        country_df["Obesity_Rate"],
        label="Obesity rate (%)",
        linestyle="--",
    )
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Daily calories per person")
    ax2.set_ylabel("Adult obesity rate (%)")
    plt.title(f"Calories and Obesity Over Time – {country}")
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left")

    country_slug = country.lower().replace(" ", "_")
    out_path = os.path.join(FIGURES_DIR, f"trend_{country_slug}.png")
    plt.tight_layout()
    plt.savefig(out_path, dpi=300)
    plt.close()
    print(f"[INFO] Saved trend plot for {country} to {out_path}")

def yearly_correlation_plot(yearly_corr: pd.DataFrame) -> None:
    if yearly_corr.empty:
        print("[WARN] No yearly correlation data to plot.")
        return
    plt.figure(figsize=(9, 5))
    plt.plot(yearly_corr["Year"], yearly_corr["correlation"], marker="o")
    plt.axhline(0, color="gray", linewidth=0.8)
    plt.xlabel("Year")
    plt.ylabel("Correlation (Calories vs Obesity)")
    plt.title("Yearly Correlation Between Calories and Adult Obesity")
    plt.grid(True, linestyle="--", alpha=0.3)

    out_path = os.path.join(FIGURES_DIR, "yearly_correlation.png")
    plt.tight_layout()
    plt.savefig(out_path, dpi=300)
    plt.close()
    print(f"[INFO] Saved yearly correlation plot to {out_path}")

def main():
    print("[INFO] Loading integrated dataset...")
    df = load_data()

    print("[INFO] Computing global correlation...")
    global_corr = compute_global_correlation(df)
    print(f"[RESULT] Global correlation (all years): {global_corr:.3f}")

    print("[INFO] Computing yearly correlation...")
    yearly_corr = compute_yearly_correlation(df)
    corr_out = os.path.join(RESULTS_DIR, "yearly_correlation.csv")
    os.makedirs(RESULTS_DIR, exist_ok=True)
    yearly_corr.to_csv(corr_out, index=False)
    print(f"[INFO] Saved yearly correlation table to {corr_out}")

    print("[INFO] Creating visualizations...")
    scatter_calories_vs_obesity(df, year=2010)         
    scatter_calories_vs_obesity(df, year=None)         
    yearly_correlation_plot(yearly_corr)
    for country in ["United States", "Vietnam", "Japan", "United Kingdom"]:
        line_trend_for_country(df, country)

    print("[INFO] Analysis and visualization complete.")

if __name__ == "__main__":
    main()
