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
  - Processor details (including cores and threads)
  - Motherboard information
  - RAM capacity
  - Storage devices (including used and free space)
  - Graphics card(s) information
  - Display specifications
  - Audio devices
- Allows users to select specific sections to include in the report
- Generates a well-formatted Markdown file with timestamp in filename
- Cross-platform compatibility (Windows, macOS, Linux)
- Concurrent execution for faster data collection
- Progress indicator during specification gathering

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
python run-system_specs_generator.py
```

The script will display a progress indicator while gathering system specifications. Then, follow the on-screen prompts to select which sections to include in your report and choose where to save the output file. The generated file will have a timestamp in the format "YYYYMMDD_HHMM" appended to its name.

## Output Example

The generated Markdown file will look similar to this:

```markdown
# System Specifications

## Overview
- **Model:** LENOVO 20EQCT01WW
- **OS:** Microsoft Windows 10 Pro (10.0, Build 19045)

## Processor
- **Model:** Intel(R) Core(TM) i7-6700HQ CPU @ 2.60GHz
- **Frequency:** 2.60 GHz
- **Cores:** 4
- **Threads:** 8

## Motherboard
- **Manufacturer:** LENOVO
- **Model:** 20EQCT01WW

## RAM
- 32.00 GB

## Storage
- **Device:** C:
- **Total:** 465.76 GB
- **Used:** 420.18 GB
- **Free:** 45.58 GB

## Graphics Card
- **Name:** NVIDIA Quadro M1000M
- **Memory:** 4096 MB

## Display
- **Name:** Intel(R) HD Graphics 530
- **Resolution:** 1920x1080

## Audio
- Realtek High Definition Audio
- Steam Streaming Microphone
- Steam Streaming Speakers
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.