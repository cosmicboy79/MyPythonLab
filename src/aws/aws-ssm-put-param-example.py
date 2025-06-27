import json

with open("./aws-ssm-parameters.json") as file:
    data = json.load(file)
    for item in data["Parameters"]:
        cmd = f'aws ssm put-parameter --name "{item['Name']}" \
                --description "{item['Description']}" --value "{item['Value']}" \
                    --type "{item['Type']}" --overwrite'
        print(f'Executing AWS SSM command: {cmd}')
        # Execute the command to put the data in AWS Parameter Store
        # It is commented out in the example, but in order to execute
        # the following lines, AWS CLI must be installed first!
        # https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
        # import os
        # os.system(cmd)