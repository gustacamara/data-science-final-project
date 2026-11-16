import pandas as pd
from src.config import BrainRegions, PHENOTYPES_FILE, L1_REGULATOR_FILE, PROCESSED_DIR


def load_region(region, nrows):
    return pd.read_csv(region.file, sep="\t", skiprows=2, nrows=nrows)


def load_all_regions(nrows=20_000):
    return {region: load_region(region, nrows) for region in BrainRegions}


def load_phenotypes():
    return pd.read_csv(PHENOTYPES_FILE, sep="\t")


SPLITS = ("train", "val", "test")


def save_split(name, X, y, info):
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    X.to_pickle(PROCESSED_DIR / f"X_{name}.pkl")
    y.to_pickle(PROCESSED_DIR / f"y_{name}.pkl")
    info.to_pickle(PROCESSED_DIR / f"info_{name}.pkl")


def load_split(name):
    return tuple(pd.read_pickle(PROCESSED_DIR / f"{kind}_{name}.pkl") for kind in ("X", "y", "info"))


def load_splits():
    return {name: load_split(name) for name in SPLITS}

if __name__ == "__main__":
    regions = load_all_regions()
    for region, df in regions.items():
        print(region.value, df.shape)

    phenotypes = load_phenotypes()
    print(phenotypes.shape)
    print(phenotypes.head())
