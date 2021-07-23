import sys
import subprocess

# Quick and dirty script to run construct network over a set number of years
# call with python3 workflow/run_all_network.py 2000 2001 

if __name__ == "__main__":
    YEARS = [int(y) for y in sys.argv[1:]]

    for year in YEARS:
        subprocess.Popen(['python3', 'workflow/construct_yearly_networks.py', 'data/journal_networks/paper_count.csv', 'data/journal_networks', str(year), '2', 'data/journal_networks/nodes-{year}.csv'.format(year=year), 'data/journal_networks/edges-{year}.csv'.format(year=year)])
        subprocess.Popen(['python3', 'workflow/construct_yearly_networks.py', 'data/journal_networks/paper_count.csv', 'data/journal_networks', str(year), '9999', 'data/journal_networks/raw-nodes-{year}.csv'.format(year=year), 'data/journal_networks/raw-edges-{year}.csv'.format(year=year)])



