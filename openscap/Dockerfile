FROM ubuntu:20.04

RUN apt-get update && apt-get install -y \
    libopenscap8 \
    wget \
    unzip \
    ssg-debderived \
    python3 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /scap

COPY run_scan.sh /scap/run_scan.sh
COPY parse_results.py /scap/parse_results.py
COPY update_content.sh /scap/update_content.sh

RUN chmod +x /scap/run_scan.sh /scap/update_content.sh

CMD ["/bin/bash"]
