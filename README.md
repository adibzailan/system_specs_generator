# System Specifications Generator

A Python script to generate a detailed Markdown report of your computer's hardware specifications.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Output Example](#output-example)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project provides a Python script that gathers comprehensive information about your computer's hardware and generates a detailed Markdown report. It's inspired by system information tools like Razer Cortex, offering a lightweight and customizable alternative.

## Features

- Collects detailed system information including:
  - Overview (Model, OS)
  - Processor details
  - Motherboard information
  - RAM capacity
  - Storage devices and capacity
  - Graphics card(s) information
  - Display specifications
  - Audio devices
- Allows users to select specific sections to include in the report
- Generates a well-formatted Markdown file
- Cross-platform compatibility (Windows, macOS, Linux)

## Requirements

- Python 3.6+
- Required Python packages:
  - psutil
  - GPUtil
  - wmi (Windows only)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/adibzailan/system-specs-generator.git
   cd system-specs-generator
   ```

2. Install required packages:
   ```
   pip install psutil GPUtil wmi
   ```

## Usage

Run the script from the command line:

```
python system_specs_generator.py
```

Follow the on-screen prompts to select which sections to include in your report and choose where to save the output file.

## Output Example

The generated Markdown file will look similar to this:

```markdown
# System Specifications

## Overview
- **Model:** LENOVO 20EQCT01WW
- **OS:** Microsoft Windows 10 Pro (10.0, Build 19045)

## Processor
- **Model:** Intel(R) Core(TM) i7-6700HQ CPU @ 2.60GHz 4/8
- **Frequency:** 2.60 GHz

## Motherboard
- **Manufacturer:** LENOVO
- **Model:** 20EQCT01WW

## RAM
- 32 GB

## Storage
- **Device:** WDC WDS500G1B0A-00H9H0
- **Total:** 465.8 GB
- **Type:** Fixed hard disk media

## Graphics Card
- **Name:** NVIDIA Quadro M1000M
- **Memory:** 4 GB
- **Name:** Intel(R) HD Graphics 530
- **Memory:** 1 GB

## Display
- **Name:** Lenovo LEN40BA
- **Resolution:** 1920x1080
- **Size:** 15.3 inch

## Audio
- Realtek High Definition Audio
- Steam Streaming Microphone
- Steam Streaming Speakers
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
