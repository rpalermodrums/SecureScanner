
FROM ubuntu:20.04

RUN apt-get update && apt-get install -y \
    openscap-scanner \
    wget \
    unzip \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /scap

RUN wget https://github.com/ComplianceAsCode/content/releases/download/v0.1.64/scap-security-guide-0.1.64-oval-510.zip \
    && unzip scap-security-guide-0.1.64-oval-510.zip \
    && rm scap-security-guide-0.1.64-oval-510.zip

COPY run_scan.sh /scap/run_scan.sh
RUN chmod +x /scap/run_scan.sh

CMD ["/bin/bash"]
