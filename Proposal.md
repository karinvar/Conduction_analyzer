# Conduction_analyzer Proposal

**Background and Motivation**

The objective of this project is to analyze electrophysiological recordings from the sciatic nerves of mice, focusing on the impact of ectopic clusters of voltage-gated sodium channels (NaCh) on conduction. My research investigates how these clusters, formed in hypomyelinated and demyelinated peripheral nervous system (PNS) models, may enhance conduction and mitigate conduction block. This tool is designed to automate the analysis of these recordings, enabling more efficient and accurate exploration of signal propagation dynamics under experimental conditions.

**Input Data**

The input data is provided in an Excel file containing two sheets:

- Sheet 1: Raw Recordings

Columns represent various parameters recorded for each mouse.

Each mouse has multiple columns corresponding to distinct parameters, such as signal amplitude and duration.

- Sheet 2: Experimental Metadata

Information about experimental conditions and mouse groups.

**Analysis and Features**

- Signal Metrics Extraction:

Calculate duration, peak amplitude, and other key signal characteristics for each recording.

Compare these metrics across equivalent columns (parameters) between mice to identify differences.

- Group Comparisons:

Utilize metadata from Sheet 2 to group recordings and perform statistical comparisons.

Identify patterns that suggest differences in conduction efficiency due to experimental conditions.

- Visual Output:

Generate plots comparing signal characteristics across mice and groups.

Highlight trends and outliers in the data.

- Statistical Summaries:

Provide CSV output summarizing statistical analyses, including mean, standard deviation, and p-values.

**Output**

Plots comparing signal duration and peak amplitude across mice and groups.

CSV files summarizing key metrics and statistical comparisons.

**Future Improvements**

Add support for additional electrophysiological metrics (e.g., latency, conduction velocity).

Interactive GUI for easier data exploration.

Integration with machine learning models to predict conduction outcomes based on input parameters.

**Acknowledgment**

This project was developed as part of the Python programming course. [https://github.com/szabgab/wis-python-course-2024-11]

By integrating this tool into research workflows, it will greatly streamline the analysis of electrophysiological recordings, enabling faster and more accurate insights into the beneficial effects of ectopic sodium channel clusters on conduction.

