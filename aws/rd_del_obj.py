import boto
import boto.s3.connection
import uuid

def main():

    conn = boto.connect_s3(
        aws_access_key_id = access_key,
        aws_secret_access_key = secret_key,
        host = 's3.amazonaws.com',
        #is_secure=False,               # uncommmnt if you are not using ssl
        calling_format = boto.s3.connection.OrdinaryCallingFormat(),
        )

    #bucket = conn.get_bucket("asset.ama.here.com")
    #bucket = conn.get_bucket("raw.rcp.ama.here.com")
    #bucket = conn.get_bucket("minor.rcp.ama.here.com")
    bucket = conn.get_bucket("rcp_d_major")
    #bucket = conn.get_bucket("rcp_d_minor")

    k = '7d12aae6'  # rob test in R&D
    #k = 'd7250e49'  # rob test in prod
    #k = '05dfc24a'  # previous, valid prod upload
    I = bucket.list(prefix = k)
    L = list(I)

    for _ in L:
        key = bucket.lookup(_)
        print _, key.size
        #print _


    bucket.delete_keys(L, quiet = True)


if __name__ == "__main__":
    main()

