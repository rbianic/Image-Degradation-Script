# Image Degradation Script

A Python script for degrading images with various effects such as Gaussian noise, blur, and pixelation.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [License](#license)

## Introduction

This script provides a simple way to degrade images for testing or experimentation purposes. It currently supports three degradation types: Gaussian noise, blur, and pixelation.

## Features

- Apply Gaussian noise to images.
- Blur images with a specified level.
- Pixelate images for a stylized effect.

## Getting Started

### Prerequisites

Make sure you have Python and the required libraries installed. You can install the necessary libraries using:

```bash
pip install opencv-python numpy
```

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/rbianic/image-degradation-script.git
   ```

2. Run the script:

   ```bash
   python3 degrade_image.py path/to/your/image.jpg 25 gaussian
   ```

## Usage

Provide examples and instructions on how to use the script with different degradation types and levels.

### Example:

```bash
python degrade_image.py path/to/your/image.jpg 25 gaussian
```

This command applies Gaussian noise with a degradation level of 25 to the specified image.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For questions or feedback, feel free to reach out to [RBianic](mailto:public@fkgm.fr).
