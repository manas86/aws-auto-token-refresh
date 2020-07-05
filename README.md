# WELCOME
A typical boto3 request to assume IAM role looks like: 
'''
response = client.assume_role(
    RoleArn='string',
    RoleSessionName='string',
    Policy='string',
    DurationSeconds=123,
    ExternalId='string',
    SerialNumber='string',
    TokenCode='string'
)
'''
