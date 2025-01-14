# Conduction_analyzer Proposal

## Background and Motivation 

The objective of this project is to analyze electrophysiological recordings from the sciatic nerves of mice, focusing on the impact of ectopic clusters of voltage-gated sodium channels (NaCh) on conduction. My research investigates how these clusters, formed in hypomyelinated and demyelinated peripheral nervous system (PNS) models, may enhance conduction and mitigate conduction block. This tool is designed to automate the analysis of these recordings, enabling more efficient and accurate exploration of signal propagation dynamics under experimental conditions.

## What Does This Project Do?

This tool processes Excel files containing raw electrophysiological data from sciatic nerve recordings. It extracts key signal metrics (e.g., duration, peak amplitude), generates comparative visualizations between mice, and performs statistical analyses to identify differences in conduction properties.

## Input Data

The input data is provided in an Excel file containing two sheets:

- Sheet 1: Raw Recordings from Large Fibers

We get the peak amplitude control (from column B onwards, a column for each mouse) in response to a corresponding current (column A) given in stimulation.

- Sheet 2: Raw Recordings from C Fibers

We get the peak amplitude control (from column B onwards, a column for each mouse) in response to a corresponding duration of stimulus (column A) given.

## Analysis and Features

- Signal Metrics Extraction:

Calculate duration, peak amplitude, and other key signal characteristics for each recording.

Compare these metrics across equivalent columns (different mice) to identify differences.

- Group Comparisons:

Identify patterns that suggest differences in conduction efficiency due to experimental conditions.

- Visual Output:

Generate plots comparing signal characteristics across mice and groups.

Highlight trends and outliers in the data.

- Statistical Summaries:

Provide CSV output summarizing statistical analyses, including mean, standard deviation, and p-values.

## Output

Plots comparing signal duration and peak amplitude across mice and groups.

CSV files summarizing key metrics and statistical comparisons.

## Technical Instructions

### How to Download and Install

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd Conduction_Analyzer
   ```

2. **Set up the environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Run the analysis tool:**
   ```bash
   python analyze_data.py --input input_recordings.xlsx
   ```

### Dependencies
- `pandas`
- `numpy`
- `matplotlib`
- `scipy`

Install using:
```bash
pip install pandas numpy matplotlib scipy
```

### Running Tests
```bash
python -m unittest discover tests
```

## Future Improvements

- Support for advanced signal metrics (e.g., conduction velocity).
- GUI for user-friendly data analysis.
- Integration with machine learning for predictive analysis.

## Acknowledgment ##

This project was developed as part of the [Python programming course](https://github.com/szabgab/wis-python-course-2024-11)

By integrating this tool into research workflows, it will greatly streamline the analysis of electrophysiological recordings, enabling faster and more accurate insights into the beneficial effects of ectopic sodium channel clusters on conduction.


