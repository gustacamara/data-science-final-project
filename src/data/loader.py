import pandas as pd
from src.config import BrainRegions, PHENOTYPES_FILE, L1_REGULATOR_FILE


def load_region(region, nrows):
    return pd.read_csv(region.file, sep="\t", skiprows=2, nrows=nrows)


def load_all_regions(nrows=20_000):
    return {region: load_region(region, nrows) for region in BrainRegions}


def load_phenotypes():
    return pd.read_csv(PHENOTYPES_FILE, sep="\t")

if __name__ == "__main__":
    regions = load_all_regions()
    for region, df in regions.items():
        print(region.value, df.shape)

    phenotypes = load_phenotypes()
    print(phenotypes.shape)
    print(phenotypes.head())
