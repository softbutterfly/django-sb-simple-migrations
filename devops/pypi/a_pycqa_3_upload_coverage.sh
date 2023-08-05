#! /bin/sh
BASE_DIR="$( cd "$( dirname "$0" )" > /dev/null 2>&1 && pwd )"

. "$BASE_DIR/setup_variables.sh"

echo "SoftButterfly CI: Report coverage for environment ${CI_JOB_NAME##*:}"

if [ "$REPORT_COVERAGE" = true ]; then
    echo "* Coverage report is enabled"

    echo "* Downloading coday report uploader."
    curl -Ls --output codacy_report_uploader.sh https://coverage.codacy.com/get.sh
    chmod +x codacy_report_uploader.sh

    echo "* Uploading reports"
    ./codacy_report_uploader.sh
else
    echo "* Coverage report is disabled."
fi
