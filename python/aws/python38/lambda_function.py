import json
import subprocess

def lambda_handler(event, context):

    # Replace 'your_command_here' with the actual shell command you want to run
    command = 'ls -R /opt/'

    try:
        # Run the command and capture the output
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, text=True)
    
        # Print the output
        print("Command output:")
        print(result.stdout)
        import fmi
    
    except subprocess.CalledProcessError as e:
        # If the command returns a non-zero exit code, an exception is raised
        print(f"Error executing command: {e}")
    
        # TODO implement
        # print(fmi)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
