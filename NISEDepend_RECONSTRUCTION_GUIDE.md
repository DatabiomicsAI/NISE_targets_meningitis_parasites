# NISEDepend v1.0.0 local reconstruction guide

Version: 1.0.0
Date: 2026-07-05
Archive location in this repository: tools/NISEDepend_archive/NISEDepend_v1.0.0_20260705.zip.b64.part00
Expected ZIP SHA256: 56fb434ecdb248adc2f9292236ecf08efc26143b85b4a3fba45e10e47020c7ac

## Purpose

This guide explains how to recover the complete NISEDepend source package from the base64 ZIP archive stored in the repository. NISEDepend is the workflow for EC clustering, KEGG module completeness, KAAS query.ko support, DEG essentiality, C. elegans lethal phenotype mapping and parasite-host metabolic-dependence candidate tables.

## Local reconstruction steps

1. Clone the repository.
2. Enter the archive directory: tools/NISEDepend_archive.
3. Convert the base64 text file back to a ZIP file.
4. Extract the ZIP into tools/NISEDepend.
5. Check the SHA256 checksum of the recovered ZIP against the checksum above.

## Linux or macOS commands

Run these commands from the repository root:

    cd tools/NISEDepend_archive
    base64 --decode NISEDepend_v1.0.0_20260705.zip.b64.part00 > NISEDepend_v1.0.0_20260705.zip
    sha256sum NISEDepend_v1.0.0_20260705.zip
    mkdir -p ../NISEDepend
    unzip -o NISEDepend_v1.0.0_20260705.zip -d ../NISEDepend

On macOS, if sha256sum is not available, use:

    shasum -a 256 NISEDepend_v1.0.0_20260705.zip

## Expected result

After extraction, the directory tools/NISEDepend should contain the full NISEDepend v1.0.0 package, including README files, configuration templates, example data, scripts and the Python package.

## First run after extraction

Create the environment:

    cd ../NISEDepend/NISEDepend_v1.0.0_20260705
    conda env create -f environment.yml
    conda activate nisedepend

Prepare references automatically:

    bash scripts/run_auto_reference_preparation.sh data/reference_auto eukaryota,bacteria,archaea

Run the full workflow with the example organism table:

    bash scripts/run_full_nisedepend_workflow.sh configs/organisms.example.tsv runs/nisedepend_v1

## Automatic reference sources included

- KEGG REST module list and KO-to-EC mapping.
- UniProt/Swiss-Prot enzyme reference files.
- DEG eukaryotic essential proteins: DEG20.aa.gz.
- DEG bacterial essential proteins: DEG10.aa.gz.
- DEG archaeal essential proteins: DEG30.aa.gz.
- WormBase ParaSite WBPS19 C. elegans PRJNA13758 phenotype GAF file.

## Notes

If the checksum does not match, delete the reconstructed ZIP and regenerate it from the base64 part file. Do not edit the base64 file manually.