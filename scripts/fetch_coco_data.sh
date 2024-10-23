#!/bin/bash

# Ensure wget are installed
for cmd in wget; do
    if ! command -v $cmd &>/dev/null; then
        echo "$cmd could not be found. Please install $cmd and try again."
        exit 1
    fi
done

# Navigate to the parent directory of the scripts folder
cd "$(dirname "$0")/.." || {
    echo "Failed to change directory"
    exit 1
}

# Base directory for the COCO dataset
BASE_DIR="dataset/coco"

# Ensure the base directory exists
mkdir -p "$BASE_DIR"

# Function to download a file if it doesn't already exist
download_file() {
    local url=$1
    local output_file=$2

    if [ -f "$output_file" ]; then
        echo "$output_file already exists. Skipping download."
    else
        echo "Downloading $output_file..."
        wget --progress=bar:force "$url" -O "$output_file"
    fi
}

# Array of URLs and their corresponding output files
FILES=(
    "http://images.cocodataset.org/zips/train2017.zip $BASE_DIR/train2017.zip"
    "http://images.cocodataset.org/zips/val2017.zip $BASE_DIR/val2017.zip"
    "http://images.cocodataset.org/zips/test2017.zip $BASE_DIR/test2017.zip"
    "http://images.cocodataset.org/annotations/annotations_trainval2017.zip $BASE_DIR/annotations_trainval2017.zip"
)

# Download and unzip files one after the other
for file in "${FILES[@]}"; do
    url=$(echo $file | awk '{print $1}')
    output_file=$(echo $file | awk '{print $2}')
    download_file "$url" "$output_file"
done

echo "All downloads completed."
