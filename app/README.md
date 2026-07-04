# Streamlit app

This folder contains the Streamlit browser for the NISE targets resource.

Run locally:

```bash
python -m pip install -r app/requirements.txt
streamlit run app/app.py
```

The app reads processed CSV files from `data/processed/` and FASTA files from `data/sequences/by_ec/`.

To add new tables:

1. Add a CSV file to `data/processed/`.
2. Add it to the `TABLES` dictionary in `app/app.py`.
3. Restart Streamlit.

To add new FASTA files:

1. Add files to `data/sequences/by_ec/` using names such as `EC_2_7_4_9.fasta`.
2. Update `data/sequences/fasta_index.csv`.

Please cite the article and repository when using the data.
