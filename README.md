# General Purpose HTTP Stress Tester

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
