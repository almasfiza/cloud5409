
import hashlib
import json
import urllib3

def lambda_handler(event, context):
 
    # input_string = event["input"]
    # input_object = json.loads(input_string)  # Convert the "input" string into a JSON object
    value = event["value"]
  
    hashed_value = hashlib.md5(value.encode('utf-8')).hexdigest()

    send_result_to_api(event['course_uri'], event["action"], hashed_value, value, context)
    return {
        'statusCode': 200,
        'body': json.dumps('Hashing operation completed.')
    }

def send_result_to_api(api_url, method, hashed_value, original_value, context):
    http = urllib3.PoolManager()

    payload = {
        'banner': 'B00933336',
        'result': hashed_value,
        'arn': context.invoked_function_arn,
        'action': method,
        'value': original_value
    }

    headers = {'Content-Type': 'application/json'}
    encoded_data = json.dumps(payload).encode('utf-8')
    
    print("Payload being sent to the API:", json.dumps(payload, indent=2))

    response = http.request('POST', api_url, body=encoded_data, headers=headers)

    if response.status != 200:
        print(f"Failed to send result to API. Status code: {response.status}, Response: {response.data}")
