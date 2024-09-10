# SecureScanner

SecureScanner is a comprehensive, Docker-based security scanning solution that integrates OpenSCAP for compliance checking. It's designed to work with various Linux distributions and security profiles.

## Features

- OpenSCAP integration for CIS compliance scanning
- Docker-based setup for consistent environments
- Support for multiple security profiles
- Automatic parsing and summarizing of scan results
- Easy content updates

## Prerequisites

- Docker
- Docker Compose

## Quick Start

1. Clone this repository:
```bash
$ git clone https://github.com/rpalermodrums/SecureScanner.git
$ cd SecureScanner
```

2. Build the Docker image:
```bash
$ docker build -t securescanner .
```

3. Run a scan:
```bash
$ docker run -v $(pwd)/results:/results securescanner /scap/run_scan.sh ospp scan_result
```

Replace `ospp` with the desired profile name.

4. View the results:
   The scan results will be available in the `results` directory.

## Usage

### Running a Scan

Use the `run_scan.sh` script to perform a scan:

```bash
$ docker run -v $(pwd)/results:/results securescanner /scap/run_scan.sh <profile> <output_prefix> [benchmark_file]
```

- `<profile>`: The name of the security profile to use (e.g., ospp, pci-dss)
- `<output_prefix>`: Prefix for output files
- `[benchmark_file]`: Optional. The benchmark file to use (default: ssg-ubuntu2004-ds.xml)

### Updating SCAP Content

To update the SCAP content to the latest version:

```bash
$ docker run securescanner /scap/update_content.sh
```

### Parsing Results

The `parse_results.py` script automatically runs after each scan, providing a summary of the results. You can also run it manually:

```bash
$ docker run -v $(pwd)/results:/results securescanner python3 /scap/parse_results.py /results/scan_result_results.xml
```

## Customization

- Modify the `Dockerfile` to add or remove packages as needed.
- Edit the `run_scan.sh` script to change default scan parameters.
- Update the `parse_results.py` script to customize result parsing and reporting.

## License

This project is licensed under the MIT License - see the LICENSE file for details.