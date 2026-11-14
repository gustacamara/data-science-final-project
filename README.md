# Sex- and Region-Specific Gene Expression Stability in the Aging Human Brain

Final project for **Data Science 2026/2 (PUCPR)**: a transcriptomic study using GTEx v11 data.

## Central hypothesis
Inter-individual gene expression variability is not uniformly distributed across the human brain. Different regions show distinct levels of transcriptomic stability, and these patterns may change with aging differently between men and women.

## Objectives
1. Identify genes with the highest and lowest inter-individual variability across brain regions.
2. Determine whether age and sex are associated with differences in mean expression and variability.
3. Compare transcriptomic heterogeneity across brain regions (more stable vs. more variable regions with aging, overall and by sex).
4. Build and compare machine learning models that classify brain region from gene expression profiles, investigating the effect of sex and age on performance and selected features.

## Data
We use gene expression data (TPM) from the GTEx Portal, release v11, covering 13 brain regions. In total there are 74,628 genes and 3,234 samples from 393 donors, with each region having between 181 and 300 samples.

The expression files can be found on the [Bulk tissue expression](https://gtexportal.org/home/downloads/adult-gtex/bulk_tissue_expression) page. Open the "GTEx Analysis V11" section, then "RNA-Seq" and "Gene TPMs by tissue". The brain files start with `gene_tpm_adult_gtex_v11_brain`.

Donor sex and age bracket come from `GTEx_Analysis_v11_Annotations_SubjectPhenotypesDS.txt`, which is already in the `datasets` folder. It was downloaded from the [Metadata](https://gtexportal.org/home/downloads/adult-gtex/metadata) page, under "GTEx Analysis V11" and "Metadata Files".

The `.gct` files are too large for GitHub, so they are not in the repository. After downloading, unzip them into the `datasets` folder. There is a command in `datasets/README.txt` that downloads all regions at once.

## Structure
```
datasets/   phenotype annotations and README (expression files are downloaded locally)
docs/       project description
```
