from tqdm import tqdm
import requests

url = "https://chromedriver.storage.googleapis.com/84.0.4147.30/chromedriver_win32.zip"
so_for = 0
for i in range(100000):
    r = requests.get(url, stream=True)
    total_size = int(r.headers.get('content-length', 0))
    block_size = 1024 #1 Kibibyte
    t=tqdm(total=total_size, unit='iB', unit_scale=True)
    with open('test2.dat', 'wb') as f:
	    for data in r.iter_content(block_size):
	        t.update(len(data))
	        f.write(data)
    t.close()
    so_for += total_size/1000000000
    print(f'So far downloaded {so_for} GB')
    if total_size != 0 and t.n != total_size:
	    print("ERROR, something went wrong")
        
    