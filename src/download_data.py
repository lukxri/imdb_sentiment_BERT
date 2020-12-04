import gdown
import os
import tarfile

# TODO try https://discuss.pytorch.org/t/how-does-one-download-a-data-set-from-a-file-automatically-with-pytorch/74262/5 and remove uneccessary requirements

HOME_DIR = os.path.expanduser("~")
DATA_DIR = os.path.join(HOME_DIR, "data")


def download():

    if not os.path.exists(os.path.join(DATA_DIR, "pytorch_model.bin")):
        print("Model not found in data directory. Will start downloading data.")
        url = "https://drive.google.com/uc?id=1xYFa62ZEai2Ix_ZJBaV8_H6S1LOiWcy6"
        output = os.path.join(DATA_DIR, "data.tar.xz")
        gdown.download(url, output, quiet=False)

        if output.endswith("tar.xz"):
            print("Will start extracting data.")
            tar = tarfile.open(output, "r:xz")
            tar.extractall(DATA_DIR)
            tar.close()
            print("Done extracting data. Will remove tar.xz file now.")
            os.remove(output)
        os.chdir(DATA_DIR)
        os.rename("model.bin", "pytorch_model.bin")
    else:
        print("Files already present. No new files will be downloaded.")


if __name__ == "__main__":
    download()
