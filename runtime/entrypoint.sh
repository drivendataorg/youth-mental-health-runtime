#!/bin/bash

set -euxo pipefail

main () {
    expected_filename=main.py

    cd /code_execution

    submission_files=$(zip -sf ./submission/submission.zip)
    if ! grep -q ${expected_filename}<<<$submission_files; then
        echo "Submission zip archive must include $expected_filename"
    return 1
    fi

    echo "Unpacking submission"
    unzip ./submission/submission.zip -d ./

    ls -alh

    echo "Running submission..."
    pixi run -e $CPU_OR_GPU python main.py

    echo "Exporting submission.csv result..."

    # Valid scripts must create a "submission.csv" file within the same directory as main
    if [ -f "submission.csv"]
    then
        echo "Script completed its run."
        cp submission.csv ./submission/submission.csv
    else
        echo "ERROR: Script did not produce a submission.csv file in the main directory."
        exit_code=1
    fi
}

main |& tee "/code_execution/submission/log.txt"
exit_code=${PIPESTATUS[0]}

# Copy for terminationMessagePath
cp /code_execution/submission/log.txt /tmp/log

exit $exit_code
