CREATE TABLE IF NOT EXISTS proteome_catalog (
  dataset TEXT PRIMARY KEY,
  organism TEXT,
  analysis_layer TEXT,
  accession_or_project TEXT,
  local_fasta_file TEXT,
  protein_sequence_count INTEGER,
  public_database_url TEXT,
  included_in_matrix TEXT
);

CREATE TABLE IF NOT EXISTS core_ecs (
  ec TEXT PRIMARY KEY,
  enzyme_name TEXT,
  present_in_all_analyzed_parasites TEXT,
  in_a_cantonensis_intragenomic_analogs TEXT,
  a_cantonensis_intergenomic_not_intragenomic TEXT,
  ec_fasta_file TEXT,
  kegg_ec_url TEXT,
  brenda_url TEXT
);

CREATE TABLE IF NOT EXISTS intergenomic_summary (
  sheet TEXT PRIMARY KEY,
  organism TEXT,
  validated_intergenomic_rows INTEGER,
  unique_ec_activities INTEGER,
  unique_sequence_ids INTEGER,
  unique_pdb_hits INTEGER
);
