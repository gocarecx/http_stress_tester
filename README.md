# General Purpose HTTP Stress Tester.

This general-purpose HTTP stress tester allows you to stress test HTTP endpoints by sending a specified number of requests evenly distributed over a given 
period.

## Features
- Flexible payload specification using a `.env` file
- Customizable settings for the number of parallel workers
- Customizable sending rate and time duration
- Support for custom headers, such as Authorization
- Displays response details and rate-limiting information for each request

## Setup

1. Clone this repository or download the `http_stress_tester.py` script.
2. Create a `.env` file with your settings, such as URL, headers, and payload:
    ```ini
    [DEFAULT]
    url = https://your-url-here
    authorization = "Your-authorization-header"
    payload_template = {"key1": "value1", "key2": "ACCOUNT_NO_PLACEHOLDER", "key3": "value3", "amount": "AMOUNT_PLACEHOLDER"}
    ```
3. Replace the values in the `.env` file with the required information for your test. For the payload, you can use `ACCOUNT_NO_PLACEHOLDER` and 
`AMOUNT_PLACEHOLDER` as placeholders for account numbers and amounts, which will be replaced with random values during runtime.

4. Make sure you have Python 3 installed on your system.

## Usage

Run the script from the command line with two arguments: the number of requests (numReqs) and the time duration in seconds (timePeriod):

```bash
python3 http_stress_tester.py numReqs timePeriod
```

For example, the following command sends 10 requests evenly distributed over 10 seconds:

```bash
python3 http_stress_tester.py 10 10
```

Similarly, the following command sends 30 requests evenly distributed over 10 seconds:

```bash
python3 http_stress_tester.py 30 10
```

## Output

The script outputs the response of each call as the calls are made. For each request, it displays the status code, time taken for the request, response 
body, rate limit, remaining requests count, and rate limit reset timestamp.

## Customization

To customize the script further, such as changing the number of parallel workers, adjust the `max_concurrent_workers` variable in the script.

## Python Installation

Before using the script, you need to have Python installed on your system. Here are the installation instructions for both macOS and Windows:

### macOS

You can install Python on macOS using Homebrew, a popular package manager for macOS:

1. If you don't have Homebrew installed, you can install it by following the instructions at [brew.sh](https://brew.sh/).

2. Once you have Homebrew installed, you can install Python by running this command in your terminal:

    ```bash
    brew install python
    ```

3. After the installation is complete, you can verify that Python is installed correctly:

    ```bash
    python3 --version
    ```

### Windows

For Windows, you can install Python from the official website or using the Microsoft Store.

#### Using the Official Website

1. Go to the official Python website at [Python Releases for Windows](https://www.python.org/downloads/windows/) and download the installer for the latest 
Python 3 version.

2. Run the downloaded installer.

3. During installation, make sure the "Add Python to PATH" checkbox is selected before clicking the "Install Now" button.

4. Once the installation is complete, you can verify that Python is installed correctly:

    - Press `Win + R` to open the Run dialog.
    - Type `cmd` and press `Enter`.
    - In the command prompt, enter the following command:

      ```cmd
      python --version
      ```

#### Using Microsoft Store

1. Open the Microsoft Store in Windows.

2. Search for Python and select the latest Python 3 release.

3. Click "Get" to install it.

4. After the installation is complete, you can verify that Python is installed correctly:

    - Press `Win + R` to open the Run dialog.
    - Type `cmd` and press `Enter`.
    - In the command prompt, enter the following command:

      ```cmd
      python --version
      ```

