
#!/bin/bash

# Detect OS (this will always be 'linux' in the container, but we'll keep it for consistency)
OS=$(uname -s | tr '[:upper:]' '[:lower:]')

# Set the appropriate benchmark file
if [ "$OS" == "linux" ]; then
    BENCHMARK="ssg-ubuntu2004-ds.xml"
elif [ "$OS" == "darwin" ]; then
    BENCHMARK="ssg-macos1015-ds.xml"
else
    echo "Unsupported OS"
    exit 1
fi

# Run OpenSCAP scan
oscap xccdf eval --profile xccdf_org.ssgproject.content_profile_cis \
    --results /results/openscap_results_$(date +%Y%m%d_%H%M%S).xml \
    --report /results/openscap_report_$(date +%Y%m%d_%H%M%S).html \
    /scap/$BENCHMARK

echo "Scan complete. Results and report are in the /results directory."
