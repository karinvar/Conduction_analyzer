import pandas as pd
import argparse
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def rename_columns(signal_columns):
    """Rename columns from 'Peak amplitude control 0-5' to 'Mouse #1-6'."""
    return {col: f"Mouse #{i+1}" for i, col in enumerate(signal_columns)}

def calculate_signal_metrics(data, x_column, signal_columns):
    """Calculate peak amplitude and perform statistical analysis."""
    renamed_columns = rename_columns(signal_columns)
    data = data.rename(columns=renamed_columns)
    
    metrics = {}
    for col in renamed_columns.values():
        signal = data[col]
        metrics[col] = {
            "Peak Amplitude (mean)": np.mean(signal),
            "Peak Amplitude (std)": np.std(signal),
            "Max Amplitude": np.max(signal),
        }
    
    return pd.DataFrame(metrics).transpose()

def plot_signal_comparison(data, x_column, signal_columns, title, filename):
    """Generate a plot comparing signal characteristics across mice."""
    renamed_columns = rename_columns(signal_columns)
    data = data.rename(columns=renamed_columns)
    
    plt.figure(figsize=(8, 6))
    for col in renamed_columns.values():
        plt.plot(data[x_column], data[col], marker='o', linestyle='-', label=col)
    
    plt.xlabel(x_column)
    plt.ylabel("Peak Amplitude")
    plt.title(title)
    plt.legend()
    plt.grid()
    plt.savefig(filename)
    plt.close()  # Close the figure to prevent execution pause

def perform_statistical_tests(data, signal_columns):
    """Perform t-tests between mice recordings."""
    renamed_columns = rename_columns(signal_columns)
    data = data.rename(columns=renamed_columns)
    
    p_values = {}
    cols = list(renamed_columns.values())
    for i in range(len(cols)):
        for j in range(i + 1, len(cols)):
            mouse1, mouse2 = cols[i], cols[j]
            t_stat, p_val = stats.ttest_ind(data[mouse1], data[mouse2], nan_policy='omit')
            p_values[f"{mouse1} vs {mouse2}"] = p_val
    
    return pd.DataFrame(list(p_values.items()), columns=["Comparison", "p-value"])

def analyze_large_fibers(data):
    x_column = "Current"
    signal_columns = [col for col in data.columns if "Peak amplitude control" in col]
    
    metrics = calculate_signal_metrics(data, x_column, signal_columns)
    stats_results = perform_statistical_tests(data, signal_columns)
    
    plot_signal_comparison(data, x_column, signal_columns, "Large Fibers Signal Comparison", "large_fibers_plot.png")
    
    return metrics, stats_results

def analyze_c_fibers(data):
    x_column = "Duration (sec)"
    signal_columns = [col for col in data.columns if "Peak amplitude control" in col]
    
    metrics = calculate_signal_metrics(data, x_column, signal_columns)
    stats_results = perform_statistical_tests(data, signal_columns)
    
    plot_signal_comparison(data, x_column, signal_columns, "C Fibers Signal Comparison", "c_fibers_plot.png")
    
    return metrics, stats_results

def main(input_file):
    xls = pd.ExcelFile(input_file)
    print("Starting Analysis...\nAvailable sheets:", xls.sheet_names)
    
    results = {}
    
    if 'Large Fibers' in xls.sheet_names:
        large_fiber_sheet = pd.read_excel(xls, sheet_name='Large Fibers')
        results["Large Fibers"] = analyze_large_fibers(large_fiber_sheet)

    if 'C Fibers' in xls.sheet_names:
        c_fiber_sheet = pd.read_excel(xls, sheet_name='C Fibers')
        results["C Fibers"] = analyze_c_fibers(c_fiber_sheet)

    # Save results as Excel files
    with pd.ExcelWriter("analysis_results.xlsx") as writer:
        for sheet_name, (metrics_df, stats_df) in results.items():
            metrics_df.to_excel(writer, sheet_name=f"{sheet_name}_metrics")
            stats_df.to_excel(writer, sheet_name=f"{sheet_name}_stats")
    print("Saved results to analysis_results.xlsx")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze electrophysiology data from an Excel file.")
    parser.add_argument("--input", required=True, help="Path to the Excel file containing recordings.")
    args = parser.parse_args()
    main(args.input)
