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
- Source: [GTEx Portal, release v11](https://gtexportal.org/home/downloads/adult-gtex/bulk_tissue_expression) (gene TPM, 13 brain regions).
- 74,628 genes; 3,234 samples from 393 donors; 13 classes (181–300 samples each).
- Subject phenotypes (sex, age bracket): `datasets/GTEx_Analysis_v11_Annotations_SubjectPhenotypesDS.txt`.
- The `.gct` expression files are not versioned due to size; download them into `datasets/`. See `datasets/README.txt`.

## Structure
```
datasets/   phenotype annotations + README (expression files downloaded locally)
docs/       project description
```
