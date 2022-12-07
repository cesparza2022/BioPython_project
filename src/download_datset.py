import wget
import zipfile

url = 'http://aging.brain-map.org/api/v2/well_known_file_download/502999992'
filename = wget.download(url, out = 'D:/biopython/python_class/data/')

with zipfile.ZipFile('D:/biopython/python_class/data/', 'r') as zip_ref:
    zip_ref.extractall('D:/biopython/python_class/data/')
