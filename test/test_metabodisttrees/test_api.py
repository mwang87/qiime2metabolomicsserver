import requests

target_url = "http://localhost:5024/processmetabodisttree"


files = {'manifest': open("qiime2_manifest.tsv", 'r'), \
    'metadata': open("qiime2_metadata.tsv", 'r'), \
    'quantification': open("bucket.tsv", 'r'), \
    'classyfireresult': open("ClassyFireResults_Network.txt", 'r')}

r_post = requests.post(target_url, files=files, data={"type":"classical"})
print(r_post.json())