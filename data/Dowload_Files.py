import wget
url = 'http://aging.brain-map.org/api/v2/well_known_file_download/502999992'
filename = wget.download(url, out = "BioPython_project/data/")
