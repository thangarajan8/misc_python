from tqdm import tqdm
import requests

url = "https://community.tableau.com/servlet/JiveServlet/downloadBody/1236-102-2-15278/Sample%20-%20Superstore.xls"
for i in range(100000):
	r = requests.get(url, stream=True)
	# Total size in bytes.
	total_size = int(r.headers.get('content-length', 0))
	block_size = 1024 #1 Kibibyte
	t=tqdm(total=total_size, unit='iB', unit_scale=True)
	with open('test.dat', 'wb') as f:
	    for data in r.iter_content(block_size):
	        t.update(len(data))
	        f.write(data)
	t.close()
	if total_size != 0 and t.n != total_size:
	    print("ERROR, something went wrong")