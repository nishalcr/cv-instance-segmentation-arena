import argparse
import logging
import os
import zipfile

import requests
from tqdm import tqdm

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def download_file_from_url(url, destination):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        total_size = int(response.headers.get("content-length", 0))
        block_size = 1024
        t = tqdm(total=total_size, unit="iB", unit_scale=True)
        with open(destination, "wb") as file:
            for data in response.iter_content(block_size):
                t.update(len(data))
                file.write(data)
        t.close()
        if total_size != 0 and t.n != total_size:
            logging.error("ERROR, something went wrong")
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to download {url}: {e}")
        raise


def unzip_file(zip_path, extract_to):
    try:
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(extract_to)
    except zipfile.BadZipFile as e:
        logging.error(f"Failed to unzip {zip_path}: {e}")
        raise


def download_and_unzip_coco_dataset(destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    base_url = "http://images.cocodataset.org/"
    datasets = {
        "train2017": "zips/train2017.zip",
        "val2017": "zips/val2017.zip",
        "test2017": "zips/test2017.zip",
        "annotations": "annotations/annotations_trainval2017.zip",
    }

    for key, filename in datasets.items():
        url = base_url + filename
        destination = os.path.join(destination_folder, filename)

        # Ensure the directory for the destination file exists
        os.makedirs(os.path.dirname(destination), exist_ok=True)

        logging.info(f"Downloading {os.path.basename(filename)}...")
        try:
            download_file_from_url(url, destination)
            logging.info(f"Downloaded {os.path.basename(filename)} to {destination}")
            logging.info(f"Unzipping {os.path.basename(filename)}...")
            unzip_file(destination, destination_folder)
            logging.info(f"Unzipped {os.path.basename(filename)} to {destination_folder}")

            # Remove the zip file after unzipping
            os.remove(destination)
            logging.info(f"Removed {os.path.basename(filename)} from {destination}")
        except Exception as e:
            logging.error(f"Failed to process {os.path.basename(filename)}: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download and unzip COCO dataset")
    parser.add_argument("-d", "--destination", type=str, required=True, help="Destination directory to save the dataset")
    args = parser.parse_args()

    download_and_unzip_coco_dataset(args.destination)
