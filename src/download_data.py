import gdown

url = "https://drive.google.com/drive/folders/1Zepr_Vq6nWiJYZHlOKAtF-6Xqq3oDvIY?usp=sharing"
output = "data.tgz"
gdown.download(url, output, quiet=False)
