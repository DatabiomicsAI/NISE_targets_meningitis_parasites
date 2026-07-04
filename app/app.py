#!/usr/bin/env python3
from pathlib import Path
import pandas as pd
import streamlit as st

st.set_page_config(page_title="NISE targets", layout="wide")
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "processed"
FASTA_DIR = ROOT / "data" / "sequences" / "by_ec"
FIG_DIR = ROOT / "figures" / "svg"
TABLES = {
    "Proteome catalog": "proteome_catalog.csv",
    "Core ECs": "core_all_parasites.csv",
    "Intergenomic summary": "intergenomic_summary.csv",
    "Hypothesis table": "diagnostic_and_migration_hypotheses.csv",
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

labels = [
    "Parasites & Vectors manuscript",
    "Preprint version",
    "Hypothesis framework",
    "Diagnostic EC strategy",
    "CNS tropism inhibition",
    "Parasite exit or relocation hypothesis",
    "Supplementary conceptual figures",
    "Tables",
    "FASTA by EC",
    "Documentation",
]
tabs = st.tabs(labels)

with tabs[0]:
    st.subheader("Parasites & Vectors manuscript")
    st.write("Clean submission and review-copy files are included in the final release package. The repository hosts source tables, figures and scripts.")
    st.markdown("Repository: https://github.com/DatabiomicsAI/NISE_targets_meningitis_parasites")

with tabs[1]:
    st.subheader("Preprint version")
    st.write("The preprint version is generated from the same scientific content without editorial comments.")

with tabs[2]:
    st.subheader("Hypothesis framework")
    fig = FIG_DIR / "Figure_2_EC_diagnostic_and_CNS_tropism_hypothesis.svg"
    if fig.exists():
        st.image(str(fig))
    st.write("This figure separates EC-based diagnostic specificity from non-lethal intervention hypotheses targeting migration, tropism, persistence and cycle modulation.")

with tabs[3]:
    st.subheader("Diagnostic EC strategy")
    st.write("Complete ECs specific to one parasite among the seven analyzed datasets are treated as candidate molecular diagnostic markers. These require independent sample validation.")

with tabs[4]:
    st.subheader("CNS tropism inhibition")
    st.write("Candidate enzymes linked to migration, host-interface remodeling, motility or tissue adaptation are treated as hypotheses for reducing CNS entry or persistence.")

with tabs[5]:
    st.subheader("Parasite exit or relocation hypothesis")
    st.write("This is a cautious, hypothesis-only framework for testing whether pathway modulation can change localization or reduce damage in sensitive tissues. It requires direct experimental validation.")

with tabs[6]:
    st.subheader("Supplementary conceptual figures")
    for name in ["Supplementary_Figure_S1.svg", "Supplementary_Figure_S2.svg", "Supplementary_Figure_S3.svg", "Supplementary_Figure_S4.svg", "Supplementary_Figure_S5.svg"]:
        p = FIG_DIR / name
        if p.exists():
            st.markdown(f"### {name}")
            st.image(str(p))
            st.download_button("Download SVG", p.read_text().encode(), file_name=name, key=name)

with tabs[7]:
    for label, filename in TABLES.items():
        st.subheader(label)
        path = DATA / filename
        if path.exists():
            df = pd.read_csv(path)
            q = st.text_input(f"Search {label}", key=filename)
            if q:
                mask = df.astype(str).apply(lambda col: col.str.contains(q, case=False, na=False)).any(axis=1)
                df = df[mask]
            st.dataframe(df, use_container_width=True, height=400)
            st.download_button("Download CSV", df.to_csv(index=False).encode(), file_name=filename, key="dl_" + filename)
        else:
            st.warning(f"Missing table: {path}")

with tabs[8]:
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

with tabs[9]:
    st.markdown("""
    Add CSV tables to `data/processed/` and FASTA files to `data/sequences/by_ec/`.
    Rebuild the SQLite database with `python database/build_database.py`.
    The static GitHub Pages site is available under `docs/index.html`.
    """)
