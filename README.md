# WELCOME
A typical boto3 request to assume IAM role looks like: 
```
response = client.assume_role(
    RoleArn='string',
    RoleSessionName='string',
    Policy='string',
    DurationSeconds=123,
    ExternalId='string',
    SerialNumber='string',
    TokenCode='string'
)
```
where `DurationSeconds` is the duration of the role session. It can go up to the maximum session duration setting for the role. **So if your IAM role is only setup to go up to an hour, you wouldn't be able to extend the duration of your sessions unless you update the settings on the IAM role itself.**

So, to avoid this, there is a concept called `RefreshableCredentials`  a botocore class acting like a container for credentials needed to authenticate requests. which, can automatically refresh the credentials!

`refresh_using` is a callable that returns a set of new credentials, taking the format of metadata. Remember that in Python, functions are first-class citizens. You can assign them to variables, store them in data structures, pass them as arguments to other functions, and even return them as values from other functions. So I just need a function that generates and returns metadata.