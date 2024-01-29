import requests

img = "https://img33.imgslib.link//manga/psychic/chapters/2801732/img-20240129-134233-851_2u1K.jpg"
p = requests.get(img)
out = open("img.jpg", "wb")
out.write(p.content)
out.close()