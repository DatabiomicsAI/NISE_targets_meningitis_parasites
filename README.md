# Non-homologous isofunctional enzyme candidates in neurologically relevant helminths

This repository supports the public Databiomics research resource and manuscript:

**Non-homologous isofunctional enzyme candidates in neurologically relevant helminths**

The resource organizes AnEnPi-derived non-homologous isofunctional enzyme candidates, intergenomic parasite-human analogs, *Angiostrongylus cantonensis* intragenomic analogs, pathogen-specific EC candidates, diagnostic target hypotheses, migration/cycle-interruption hypotheses, FASTA downloads, processed tables, scripts, and a Streamlit/SQLite browser.

## Authors and correspondence

Leandro de Mattos Pereira, Carlos Graeff-Teixeira and Alessandra Loureiro Morassutti.

Contact: info@databiomics.com; mattosmp@gmail.com; almorassutti@gmail.com

## Public pages

Repository page:

https://databiomicsai.github.io/NISE_targets_meningitis_parasites/

Databiomics article page:

https://databiomics.com/New_articles/NISE_targets_meningitis_parasites/

Catalog page:

https://databiomics.com/New_articles/

## Repository organization

```text
article/                         Manuscript and preprint material
web/                             Static web resource source files
docs/                            GitHub Pages public site
data/processed/                  Processed CSV tables
data/sequences/                  FASTA files and FASTA index
figures/svg/                     Publication and web SVG figures
scripts/anenpi_python/           Python parser for AnEnPi-like outputs
app/                             Interactive Streamlit app
```

## How to update the resource

1. Add new processed CSV files under `data/processed/`.
2. Add FASTA files under `data/sequences/` or `data/sequences/by_ec/`.
3. Update `data/sequences/fasta_index.csv` with organism, protein ID, EC, source file and download path.
4. Rebuild the static page.
5. Rebuild the SQLite database with `python database/build_database.py`.
6. Validate the database with `python database/validate_database.py`.
7. Commit the updated page, tables, FASTA, scripts and README.

## Streamlit app

```bash
python -m pip install -r app/requirements.txt
streamlit run app/app.py
```

## How to cite

If you use these data, tables, FASTA files, scripts, figures, database, or web resource, please cite the associated article:

**Non-homologous isofunctional enzyme candidates in neurologically relevant helminths**

Provisional BibTeX:

```bibtex
@article{Pereira_NISE_helminths_2026,
  title = {Non-homologous isofunctional enzyme candidates in neurologically relevant helminths},
  author = {Pereira, Leandro de Mattos and Graeff-Teixeira, Carlos and Morassutti, Alessandra Loureiro},
  year = {2026},
  note = {Manuscript and public database resource in preparation}
}
```

## License

Data and code are released for academic and research use. Update this section with the final license selected for publication.
