# ige-cytokine-behavior-analysis

> ⚠️ **This project uses entirely synthetic (mock) data.** All values were
> generated programmatically to have realistic statistical properties and
> biologically plausible patterns, based loosely on published immunology
> literature. No real patient data, real clinical measurements, or real
> study results are included anywhere in this repository. Findings here
> should not be interpreted as real clinical or biomarker discoveries.

> ## Project Overview
This repository demonstrates a full data analysis pipeline — correlation
analysis, regression, machine learning, and biomarker identification —
applied to simulated IgE, cytokine, and behavior/disease outcome data.

## Contents
- `data/` — mock datasets (behavior analysis + disease classification)
- `01_load_data.ipynb` through `10_ml_publication.ipynb` — behavior analysis pipeline
- `11_clinical_disease_groups.ipynb` — multi-group disease classification analysis
- `src/plot_style.py` — reusable publication figure styling
- `results/` — saved figures

## Methods Used
Spearman/partial correlation with FDR correction, OLS and Lasso regression,
Random Forest and XGBoost predictive modeling, permutation importance and
SHAP for biomarker identification, Kruskal-Wallis for multi-group comparison.

## How to Reproduce
1. Clone this repo
2. `pip install -r requirements.txt`
3. Run notebooks in numerical order