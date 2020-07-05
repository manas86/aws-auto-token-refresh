import boto3
from botocore.credentials import RefreshableCredentials
from botocore.session import get_session
from boto3 import Session

aws_region="eu-west-1"
sts_client = boto3.client("sts", region_name=aws_region)
role_name="dummy-role-1"
session_name="Session_name"

def _refresh():
    " Refresh tokens by calling assume_role again "
    params = {
        "RoleArn": role_name,
        "RoleSessionName": session_name,
        "DurationSeconds": 3600,
    }

    response = sts_client.assume_role(**params).get("Credentials")
    credentials = {
        "access_key": response.get("AccessKeyId"),
        "secret_key": response.get("SecretAccessKey"),
        "token": response.get("SessionToken"),
        "expiry_time": response.get("Expiration").isoformat(),
    }
    return credentials


session_credentials = RefreshableCredentials.create_from_metadata(
    metadata=_refresh(),
    refresh_using=_refresh,
    method="sts-assume-role",
)

# Now we can use this as long as possible 

session = get_session()
session._credentials = session_credentials
session.set_config_variable("region", aws_region)
autorefresh_session = Session(botocore_session=session)
ec2_client = autorefresh_session.client("ec2", region_name=aws_region)

