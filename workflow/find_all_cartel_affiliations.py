import numpy as np
import pandas as pd
import utils
from scipy import sparse
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import matplotlib.colors as colors
from matplotlib import cm
import os
import plot-all-cartels as pac

if __name__ == "__main__":
    CARTEL_DIR = sys.argv[1]
    YEARS = [int(y) for y in sys.argv[2:]]
    
    
    graph = utils.get_db()
    all_citations = pd.DataFrame()

    # For each year make plots
    for year in YEARS:
        citation_group_table = pac.plotload_valid_cartel(year, CARTEL_DIR)

        # Skip years that have nothing
        if citation_group_table.empty:
            continue

        # Set the name of each node
        citation_group_table["name"] = citation_group_table["mag_affiliation_name"].apply(lambda x : str(pac.get_affiliation_name(graph, x)))
        all_citations.append(citation_group_table)

    all_citations.to_csv("{root}/all_affiliations.csv".format(root=CARTEL_DIR), sep="\t")