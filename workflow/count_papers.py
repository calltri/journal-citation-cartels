import pandas as pd
import sys
import utils

PAPER_COUNT_FILE = sys.argv[1]

if __name__ == "__main__":

    # connect to the database
    graph = utils.get_db()

    # Compute the paper count first
    # TODO get only unique relationships
    field = "psychology"
    query = """ 
    MATCH (p:Paper)-[:field_of_study]->(f:FieldsOfStudy)
    WHERE f.NormalizedName="%s" 
    WITH p
    MATCH (p)-[:published_from]->(j:Affiliations)
    return j.AffiliationId as id, count(DISTINCT p) as pcount, p.Year as year
    """ % (
        field,
    )
    
    df = graph.run(query).to_data_frame()

    df.to_csv(PAPER_COUNT_FILE, sep="\t")
