import sys
import subprocess

# Quick and dirty script to run journal construction over a set number of years
# call with python3 workflow/run_all_detection.py 2000 2001 

if __name__ == "__main__":
    YEARS = [int(y) for y in sys.argv[1:]]

    for year in YEARS:
        subprocess.Popen(['python3', 'workflow/detect_cartels.py', 'data/journal_networks', '0.15', '0.01', 'data/journal_community/aggregated-community.csv', 'data/journal_cartels/cartels-{year}.csv'.format(year=year)])


