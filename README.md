
# SecureScanner

SecureScanner is a comprehensive, cross-platform security scanning solution that integrates OpenSCAP for compliance checking and OpenVAS for vulnerability scanning. It's designed to work across Windows 10, Windows 11, and the latest macOS versions, utilizing Docker for consistent environments.

## Features

- OpenSCAP integration for CIS compliance scanning
- OpenVAS integration for vulnerability scanning
- Docker-based setup for cross-platform consistency
- Easy-to-use Python orchestrator script

## Prerequisites

- Docker
- Docker Compose
- Python 3.x

## Quick Start

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/SecureScanner.git
   cd SecureScanner
   ```

2. Run the orchestrator script:
   ```
   python orchestrator.py
   ```

3. Choose options from the menu to run OpenSCAP scans or set up OpenVAS.

## Directory Structure

```
SecureScanner/
├── docker-compose.yml
├── orchestrator.py
├── README.md
└── openscap/
    ├── Dockerfile
    └── run_scan.sh
```

## Usage

- To run an OpenSCAP scan, choose option 1 from the orchestrator menu.
- To set up and start OpenVAS, choose option 2 from the orchestrator menu.

## Customization

- Modify the `openscap/run_scan.sh` script to adjust OpenSCAP scan parameters.
- Edit the `docker-compose.yml` file to change container configurations.

## Security Considerations

- Always review and understand scripts before running them, especially those related to security.
- Change default credentials for OpenVAS immediately after setup.
- Ensure proper access controls are in place for scan results.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
