import pandas as pd
import requests

# TODO: async

df = pd.read_csv('catalog.csv')

for r in df.itertuples():
    url = f"https://www.jcrew.com/s7-img-facade/{r[1]}?fmt=jpeg&qlt=90,0&resMode=sharp&op_usm=.1,0,0,0&crop=0,0,0,0&wid=128&hei=128"
    response = requests.get(url)
    try:
        file = open(f"images/{r[1]}.jpg", "wb")
        file.write(response.content)
        file.close()
    except Exception as e:
        print(f'not able to download {r[1]}')


