import pytest
import re


def linux_version(version_string):
    print(version_string)

    # Read the content of the log file
    with open('output.log', 'r') as file:
        log_content = file.read()


    pattern = r"OS Version\s*:\s*(.*)"

    # Search for the pattern in the text
    match = re.search(pattern, log_content)

    # Check if a match was found and print the result
    if match:
        os_version = match.group(1)
        print(f"OS Version: {os_version}")
        status = True
    else:
        print("OS Version not found.")
        status = False

    return status

@pytest.fixture()
def search_for_linux_version(request):
    versionString = request.param
    return linux_version(versionString)


@pytest.mark.parametrize('search_for_linux_version', ["OS Version\s*:"], indirect=['search_for_linux_version'])
def test_search_for_linux_version(search_for_linux_version):
    assert search_for_linux_version == True
