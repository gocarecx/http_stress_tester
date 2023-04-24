import sys
import json
import time
import requests
import random
import configparser
from concurrent.futures import ThreadPoolExecutor, as_completed

if len(sys.argv) != 3:
	print("Usage: python3 script.py numReqs timePeriod")
	sys.exit(1)

# Read sensitive data from .env file
config = configparser.ConfigParser()
config.read('.env')
url = config.get('DEFAULT', 'url')
authorization = config.get('DEFAULT', 'authorization')

num_reqs = int(sys.argv[1])
time_period = int(sys.argv[2])

headers = {
	"Authorization": authorization,
	"Content-Type": "application/json", }

def generate_data():
	account_no = str(random.randint(100000000, 999999999))
	amount = "{:.2f}".format(random.uniform(1, 100))

	# Read the payload template from the config
	payload_template = json.loads(config.get('DEFAULT', 'payload_template'))

	# Replace placeholders with random data
	payload = {key: value.replace("ACCOUNT_NO_PLACEHOLDER", account_no).replace("AMOUNT_PLACEHOLDER", amount) for key, value in payload_template.items()}
	return payload

def make_request(i):
	data = generate_data()
	start_time = time.time()
	response = requests.post(url, headers=headers, data=json.dumps(data))
	end_time = time.time()

	rate_limit_info = f"Rate limit: {response.headers.get('x-ratelimit-limit', 'N/A')}, Remaining: {response.headers.get('x-ratelimit-remaining', 'N/A')}, Reset: {response.headers.get('x-ratelimit-reset', 'N/A')}"
	return f"Request {i}: Status code {response.status_code}, Time taken {end_time - start_time:.2f} seconds, Response body: {response.text}, {rate_limit_info}"

def process_results(executor, task):
	result = task.result()
	print(result)

if __name__ == "__main__":
	print(f"Sending {num_reqs} requests in {time_period} seconds...")

	max_concurrent_workers = num_reqs // time_period if num_reqs > time_period else 1
	sleep_time = (time_period / num_reqs) if num_reqs > time_period else 1

	with ThreadPoolExecutor(max_workers=max_concurrent_workers) as executor:
		for i in range(num_reqs):
			future = executor.submit(make_request, i)
			future.add_done_callback(lambda task: process_results(executor, task))
			if i != num_reqs - 1:
				time.sleep(sleep_time)

	print("Stress test completed.")

