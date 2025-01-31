import pandas as pd
import argparse

def analyze_large_fibers(data):
    numeric_data = data.select_dtypes(include=['number'])
    summary = numeric_data.describe().transpose()
    print("\nLarge Fibers Summary:")
    print(summary)
    return summary

def analyze_c_fibers(data):
    numeric_data = data.select_dtypes(include=['number'])
    summary = numeric_data.describe().transpose()
    print("\nC Fibers Summary:")
    print(summary)
    return summary

def main(input_file):
    xls = pd.ExcelFile(input_file)
    print("Starting Analysis...")
    print("Available sheets:", xls.sheet_names)
    
    if 'Large Fibers' in xls.sheet_names:
        large_fiber_sheet = pd.read_excel(xls, sheet_name='Large Fibers')
        analyze_large_fibers(large_fiber_sheet)
    
    if 'C Fibers' in xls.sheet_names:
        c_fiber_sheet = pd.read_excel(xls, sheet_name='C Fibers')
        analyze_c_fibers(c_fiber_sheet)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze electrophysiology data from an Excel file.")
    parser.add_argument("--input", required=True, help="Path to the Excel file containing recordings.")
    args = parser.parse_args()
    main(args.input)
