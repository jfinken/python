import boto
import boto.s3.connection
import uuid


""" prod
NOTE: this app has to be run on a instance due to the role-assumption.  That
means the instance must have STS * privileges as well.
"""

class StsService:
    def __init__(self,
                 role_arn="NEED_ARN",
                 session_name=None):
        if session_name is None:
            session_name = str(uuid.uuid4()).replace("-", "")
        self.session_name = session_name
        self.role_arn = role_arn

    def connect_s3(self):
        sts = boto.connect_sts()

        assumed_role = sts.assume_role(self.role_arn, self.session_name)

        print assumed_role
        
        temp_creds = assumed_role.credentials
        access = temp_creds.access_key
        secret = temp_creds.secret_key
        token = temp_creds.session_token

        # create connection to S3
        return boto.connect_s3(aws_access_key_id=access, aws_secret_access_key=secret, security_token=token)

def main():
    sts_service = StsService()
    conn = sts_service.connect_s3()

    import argparse
 
    parser = argparse.ArgumentParser()
    parser.add_argument('--bucket')
    parser.add_argument('--key')
    args = parser.parse_args()

    bucket = conn.get_bucket(args.bucket)

    k = args.key
    I = bucket.list(prefix = k)
    L = list(I)

    for _ in L:
        print _

if __name__ == "__main__":
    main()

