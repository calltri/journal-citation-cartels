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
sys.path.append(os.path.abspath(os.path.join("libs/cidre")))
from cidre import cidre, filters, draw


def load_valid_cartel(year, cartel_dir):
    """Loads a cartel for a given year, returning an empty dataframe if none are there"""
    fileName = "{root}/cartels-{year}.csv".format(root=cartel_dir, year=year)
    if not os.path.exists(fileName):
        return pd.DataFrame()
    
    cartel_table = pd.read_csv(
        fileName, sep="\t"
    )
    cartel_table["year"] = year
    return cartel_table

# python workflow/plot-all-cartels.py data/cartels data/figs data/networks 2000 2001 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018
if __name__ == '__main__':
    CARTEL_DIR = sys.argv[1]
    PLOT_DIR = sys.argv[2]
    NETWORK_DIR = sys.argv[3]
    YEARS = [int(y) for y in sys.argv[4:]]
    theta = 0.15
    # For each year make plots
    for year in YEARS:
        citation_group_table = load_valid_cartel(year, CARTEL_DIR)

        # Skip years that have nothing
        if citation_group_table.empty:
            continue

        W, A_gen, nodes = utils.load_network(year, NETWORK_DIR)

        # Load the class for drawing a cartel
        dc = draw.DrawCartel()

        # Set up the canvas
        fig, axes = plt.subplots(figsize=(10,10))
        sns.set_style("white")
        sns.set(font_scale = 1.2)
        sns.set_style("ticks")

        # Set the name of each node
        citation_group_table["name"] = citation_group_table["node_id"].apply(lambda x : str(x))

        for cid, cartel in citation_group_table.groupby("group_id"):
            dc.draw(
                W,
                cartel.node_id.values.tolist(),
                cartel.donor_score.values.tolist(),
                cartel.recipient_score.values.tolist(),
                theta,
                cartel.name.values.tolist(),
                ax=axes,
            )
            plt.savefig("{root}/{year}-{cid}-cartel-plots.png".format(root=PLOT_DIR, year=year, cid=cid))
