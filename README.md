# cv-instance-segmentation-arena

A comprehensive benchmark and comparative analysis of leading computer vision models for instance segmentation. This project evaluates the performance, accuracy, and efficiency of various state-of-the-art instance segmentation models, including Mask R-CNN, Segment Anything Model (SAM), YOLOv8-seg/YOLOv9, YOLACT, and Mask DINO.

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Models Evaluated](#models-evaluated)
5. [Results](#results)
6. [Contributing](#contributing)
7. [License](#license)

## Introduction

This project aims to provide a detailed benchmark and comparative analysis of various instance segmentation models. By evaluating these models, we hope to offer insights into their performance, accuracy, and efficiency.

## Installation

To get started, clone the repository and install the required dependencies:

```bash
git clone https://github.com/yourusername/cv-instance-segmentation-arena.git
cd cv-instance-segmentation-arena
pip install -r requirements.txt
```

## Download Dataset

To download the COCO dataset, first run the `fetch_coco_data.sh` script:

```bash
bash scripts/fetch_coco_data.sh
```

After downloading, untar the files:

```bash
unzip train2017.zip
unzip val2017.zip
unzip test2017.zip
unzip annotations_trainval2017.zip
```

## Usage

To run the benchmark, use the following command:

```bash
python benchmark.py --config config.yaml
```

## Models Evaluated

- Mask R-CNN
- Segment Anything Model - (segment-anything-2/FastSAM)
- YOLOv8-seg/YOLOv9
- YOLACT/YOLOACT
- Mask DINO

## Results

The results of the benchmark will be displayed in a tabular format, highlighting the performance metrics of each model.

## Contributing

We welcome contributions! Please read our [contributing guidelines](CONTRIBUTING.md) for more details.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
