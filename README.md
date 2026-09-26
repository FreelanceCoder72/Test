# DineIQ Analytics — MenuMatrix Dining Intelligence

Big Data + Data Science restaurant intelligence platform (TEEHVIZ '26).

## Tech Stack
Streamlit • PySpark / Spark SQL / MLlib • Pandas / Scikit-learn • Plotly • Parquet

## Project Layout
```
DineIQ_Final_Delivery/
└── app/                        ← everything runs from inside here
    ├── app.py                  ← Streamlit entry point (Home)
    ├── pages/                  ← 12 dashboard pages (Executive, Menu, Customer,
    │                              Wastage, Forecast, Dual Pipeline, Market Basket,
    │                              Location, Recommendations, What-If, Anomaly,
    │                              Promotions & Pricing)
    ├── analytics/               ← core pandas/sklearn analysis modules
    ├── python_pipeline/          ← scikit-learn ML pipeline (menu classification)
    ├── spark_pipeline/           ← lightweight Spark-simulation fallback used
    │                              *inside* the Streamlit app (works even where a
    │                              real Spark/JVM isn't available, e.g. Streamlit Cloud)
    ├── spark_jobs/               ← standalone, real PySpark jobs (evidence that the
    │                              pipeline was built & validated against actual Spark)
    │     ├── spark_ingestion.py      (SRS Steps 3, 18 — CSV → Parquet ingestion)
    │     ├── spark_sql_analysis.py   (SRS Steps 6, 9, 16, 19 — Spark SQL analytics)
    │     └── spark_mllib_model.py    (SRS Step 12 — MLlib model training)
    ├── data_generator/            ← synthetic dataset generator
    ├── data/raw/                  ← the CSV dataset (orders, order_items, menu_items, …)
    ├── models/                    ← trained model artifacts (.pkl / Spark model dir)
    ├── config/settings.py         ← paths, color palette, class/segment definitions
    ├── utils/ui_helpers.py        ← shared Streamlit UI helpers/theme
    ├── tests/test_smoke.py        ← smoke tests (data integrity + pipeline sanity)
    └── requirements.txt
```

## 1. Run the Streamlit App (what you'll demo/present)
This is the main deliverable — a multi-page Streamlit dashboard. It does **not**
need a real Spark installation; it uses the `analytics/` (pandas) engine and the
`spark_pipeline/` simulated fallback.

```bash
cd DineIQ_Final_Delivery/app
python -m venv venv

# activate the venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS/Linux

pip install -r requirements.txt

# optional — only if you want to regenerate the dataset from scratch
python -m data_generator.generate_dataset

streamlit run app.py
```
Then open **http://localhost:8501** in your browser. Use the left sidebar to move
between the 12 pages.

## 2. Run the Real Spark Jobs (Big-Data evidence, SRS Steps 3/6/9/12/16/18/19)
These three scripts are separate from the app and prove the pipeline was designed
against actual Apache Spark (PySpark), not just the pandas fallback. They need a
machine with Java + PySpark installed (Streamlit Cloud/most laptops-by-default do
**not** have this — that's exactly why the app itself uses the lightweight
fallback in `spark_pipeline/` instead).

```bash
cd DineIQ_Final_Delivery/app
pip install pyspark          # additional, only needed for this part

spark-submit spark_jobs/spark_ingestion.py        # CSV -> Parquet
spark-submit spark_jobs/spark_sql_analysis.py     # Spark SQL queries (top dishes, peak hours, channel mix)
spark-submit spark_jobs/spark_mllib_model.py      # trains LR / DecisionTree / RandomForest / GBT, keeps the best

# no cluster / no spark-submit on PATH? plain python also works in local[*] mode:
python spark_jobs/spark_ingestion.py
python spark_jobs/spark_sql_analysis.py
python spark_jobs/spark_mllib_model.py
```
Outputs: Parquet files under `data/parquet/`, console analytics, and the trained
Spark model under `models/spark_menu_model/`.

## 3. Run the Tests
```bash
cd DineIQ_Final_Delivery/app
pip install pytest
pytest tests/ -v
```

## Notes
- All dashboard "What-If"/simulation outputs are clearly labeled as **estimates**,
  not actual results.
- If a page shows "no data available," make sure you ran the app from inside the
  `app/` folder (not the project root) so relative data paths resolve correctly.
