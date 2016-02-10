# 
# Generate the publications list for the MIMIC website (http://mimic.physionet.org)
# 
# Requires:
# - biopython ("pip install biopython")

from Bio import Entrez

def search(query):
    handle = Entrez.esearch(db='pubmed', 
                            sort='relevance', 
                            retmax='40',
                            retmode='xml', 
                            term=query)
    results = Entrez.read(handle)
    return results

def fetch_details(id_list):
    ids = ','.join(id_list)
    handle = Entrez.efetch(db='pubmed',
                           retmode='xml',
                           id=ids)
    results = Entrez.read(handle)
    return results

 def main():
 	Entrez.email = 'mimic-support@physionet.org'

 	query = """((Celi[Author]) OR Ghassemi[Author]) AND MIT AND ((MIMIC AND ICU) OR (MIMIC-II OR "MIMIC II" or "MIMIC 2" or "MIMIC 3" OR MIMIC-III or "MIMIC III")"""

    results = search(query)
    id_list = results['IdList']
    papers = fetch_details(id_list)

    fn = "mimic_publications.html"
    with open(fn, "w") as mimic_publ_file:
    	header = """<!--\n\nList of MIMIC-related publications generated automatically from PubMed with the following query:\n\n""" + query + \
    	""" \n\n-->\n"""
    	mimic_publ_file.write(header + '\n')

    # Should write:
    # Author list. Title. Journal. Issue. DOI. PMID.

    with open(fn, "a") as mimic_publ_file:
	    for i, paper in enumerate(papers):
	    	authors = "%s" % (paper['MedlineCitation']['Article']['AuthorList'])
	        title = "%s" % (paper['MedlineCitation']['Article']['ArticleTitle'])
	        journal = "%s" % (paper['MedlineCitation']['Article']['Journal'])
	        issue = "%s" % (paper['MedlineCitation']['Article']['ArticleTitle'])
	        doi = ""
	        pmid = "%s" % (paper['MedlineCitation']['PMID'])
	        mimic_publ_file.write(title.encode('utf-8').strip() + '\n')
	        print(title)

    # Pretty print the first paper in full to observe its structure
    #import json
    #print(json.dumps(papers[0], indent=2, separators=(',', ':')))	


if __name__ == '__main__':
    main()