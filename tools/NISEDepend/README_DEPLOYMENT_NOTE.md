# NISEDepend v1.0.0 deployment note

NISEDepend v1.0.0 was generated on 2026-07-05 as the complete Python workflow for EC clustering, KEGG module completeness, DEG essentiality, WormBase ParaSite C. elegans lethal phenotype mapping, KAAS/KASS query.ko support and parasite-host metabolic-dependence candidate tables.

The complete source archive is provided in the ChatGPT conversation as `NISEDepend_v1.0.0_20260705.zip` and should be extracted into this directory if direct GitHub connector upload of Python source files is blocked.

Main automatic URLs included:

- DEG eukaryotes: http://tubic.org/deg/public/download/DEG20.aa.gz
- DEG bacteria: http://tubic.org/deg/public/download/DEG10.aa.gz
- DEG archaea: http://tubic.org/deg/public/download/DEG30.aa.gz
- WormBase ParaSite C. elegans WBPS19 phenotypes GAF: https://ftp.ebi.ac.uk/pub/databases/wormbase/parasite/releases/WBPS19/species/caenorhabditis_elegans/PRJNA13758/caenorhabditis_elegans.PRJNA13758.WBPS19.phenotypes.gaf.gz

Recommended local deployment:

```bash
mkdir -p tools/NISEDepend
unzip NISEDepend_v1.0.0_20260705.zip -d tools/NISEDepend
```
