import subprocess
import re

def get_pytest_success_percentage():
    result = subprocess.run(
        ['pytest',
         'src/openeo_test_suite/tests/general/test_compliance.py',
         '--openeo-backend-url=https://openeo-staging.datalakecube.eumetsat.data.destination-earth.eu/openeo/1.1.0/',
         '--tb=short',
         '--html=reports/general.html'],
        capture_output=True,
        text=True
    )

    # Parse output for "passed X failed Y" pattern
    passed = re.search(r'(\d+) passed(?:)?', result.stdout)
    failed = re.search(r'(\d+) failed(?:)?', result.stdout)
    passed = int(passed.group(1))
    failed = int(failed.group(1))
    total = passed + failed
    
    percentage = int((passed / total) * 100) if total > 0 else 100
    return percentage
    
if __name__ == "__main__":
    percentage = get_pytest_success_percentage()
    print(f"SUCCESS_PERCENTAGE={percentage}")
