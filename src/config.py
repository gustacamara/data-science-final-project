from enum import Enum
from pathlib import Path
ROOT_DIR = Path(__file__).resolve().parent.parent

DATASETS_DIR = ROOT_DIR / "datasets"
DOCS_DIR = ROOT_DIR / "docs"
NOTEBOOKS_DIR = ROOT_DIR / "notebooks"
APP_DIR = ROOT_DIR / "app"
REPORTS_DIR = ROOT_DIR / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"

PHENOTYPES_FILE = DATASETS_DIR / "GTEx_Analysis_v11_Annotations_SubjectPhenotypesDS.txt"
PHENOTYPES_DICTIONARY_FILE = DATASETS_DIR / "GTEx_Analysis_v11_Annotations_SubjectPhenotypesDD.xlsx"
FILE_PREFIX = "gene_tpm_adult_gtex_v11_brain_"
L1_REGULATOR_FILE = DATASETS_DIR / "L1_regulators.txt"

class BrainRegions(Enum):

    AMYGDALA = "amygdala"
    ANTERIOR_CINGULATE_CORTEX_BA24 = "anterior_cingulate_cortex_ba24"
    CAUDATE_BASAL_GANGLIA = "caudate_basal_ganglia"
    CEREBELLAR_HEMISPHERE = "cerebellar_hemisphere"
    CEREBELLUM = "cerebellum"
    CORTEX = "cortex"
    FRONTAL_CORTEX_BA9 = "frontal_cortex_ba9"
    HIPPOCAMPUS = "hippocampus"
    HYPOTHALAMUS = "hypothalamus"
    NUCLEUS_ACCUMBENS_BASAL_GANGLIA = "nucleus_accumbens_basal_ganglia"
    PUTAMEN_BASAL_GANGLIA = "putamen_basal_ganglia"
    SPINAL_CORD_CERVICAL_C1 = "spinal_cord_cervical_c-1"
    SUBSTANTIA_NIGRA = "substantia_nigra"

    @property
    def file(self):
        """Full path of this region's expression (.gct) file."""
        return DATASETS_DIR / f"{FILE_PREFIX}{self.value}.gct"

L1_REGULATORS_WITH_2_STEPS_FROM_MECP2 = ["MECP2", "DNMT3L", "DNMT3A", "EHMT2", "DNMT3B", "SETDB1"]
MORE_EXPRESSED_GENES = ["MT-CO1", "MT-RNR2"]
NOT_IN_GTEX = ["miR128-1", "TREX1", "PURE", "TROVE2"]
L1_REGULATORS = [gene for gene in L1_REGULATOR_FILE.read_text().split() if gene not in NOT_IN_GTEX]
