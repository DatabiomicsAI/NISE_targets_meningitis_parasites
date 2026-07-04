#!/usr/bin/env python3
from pathlib import Path
import pandas as pd
import streamlit as st

st.set_page_config(page_title="NISE targets", layout="wide")
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "processed"
FASTA_DIR = ROOT / "data" / "sequences" / "by_ec"
TABLES = {
    "Proteome catalog": "proteome_catalog.csv",
    "Core ECs": "core_all_parasites.csv",
    "Intergenomic summary": "intergenomic_summary.csv",
}

st.title("Non-homologous isofunctional enzyme candidates in neurologically relevant helminths")
st.markdown("Interactive browser for the public NISE targets resource.")

with st.sidebar:
    st.header("How to cite")
    st.write("Please cite the associated article and this repository when using the data.")
    st.header("Contact")
    st.write("info@databiomics.com")
    st.write("mattosmp@gmail.com")
    st.write("almorassutti@gmail.com")

tabs = st.tabs(list(TABLES.keys()) + ["FASTA by EC", "Documentation"])
for tab, (label, filename) in zip(tabs[:-2], TABLES.items()):
    with tab:
        path = DATA / filename
        if path.exists():
            df = pd.read_csv(path)
            q = st.text_input(f"Search {label}", key=filename)
            if q:
                mask = df.astype(str).apply(lambda col: col.str.contains(q, case=False, na=False)).any(axis=1)
                df = df[mask]
            st.dataframe(df, use_container_width=True, height=600)
            st.download_button("Download CSV", df.to_csv(index=False).encode(), file_name=filename)
        else:
            st.warning(f"Missing table: {path}")

with tabs[-2]:
    ec = st.text_input("EC number, e.g. 2.7.4.9")
    if ec:
        fname = "EC_" + ec.replace(".", "_") + ".fasta"
        fpath = FASTA_DIR / fname
        if fpath.exists():
            text = fpath.read_text(errors="replace")
            st.text_area("FASTA", text, height=500)
            st.download_button("Download FASTA", text.encode(), file_name=fname)
        else:
            st.info("FASTA not available in repository for this EC yet.")

with tabs[-1]:
    st.markdown("""
    Add CSV tables to `data/processed/` and FASTA files to `data/sequences/by_ec/`.
    Restart the Streamlit app to browse the new data. The static GitHub Pages site
    is available under `docs/index.html`.
    """)
