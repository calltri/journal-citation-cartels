mport construct_yearly_networks
import subprocess

# Quick and dirty script to run construct network over a set number of years
# call with python3 workflow/run-all-network 2000

if __name__ == "__main__":
    YEARS = [int(y) for y in sys.argv[1:]]

    for year in YEARS:
        subprocess.Popen(['python3', 'workflow/construct_yearly_networks.py', 'data/networks/paper_count_journals.csv', 'data/journal_networks', '2011', '2', 'data/journal_networks/nodes-2011.csv', 'data/journal_networks/edges-2011.csv'])
        subprocess.Popen(['python3', 'workflow/construct_yearly_networks.py', 'data/networks/paper_count.csv', 'data/networks', '2011', '9999', 'data/journal_networks/raw-nodes-2011.csv', 'data/journal_networks/raw-edges-2011.csv'])



