import base64
import os

import yaml_creation as yc


def add_aws_credentials_to_job(yaml):

    try:
        key = base64.b64encode(os.environ["AWS_ACCESS_KEY_ID"].encode())
        secret_key = base64.b64encode(os.environ["AWS_SECRET_ACCESS_KEY"].encode())
        region = base64.b64encode(os.environ["AWS_DEFAULT_REGION"].encode())
    except KeyError:
        print("Set AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, and AWS_DEFAULT_REGION in your environment variables")

    i = yc.get_index_of_row_label(yaml, "data")
    key = f"  AWS_ACCESS_KEY_ID: {key}\n"
    secret_key = f"  AWS_DEFAULT_REGION: {secret_key}\n"
    region = f"  AWS_SECRET_ACCESS_KEY: {region}\n"

    yaml[i + 1] = key
    yaml[i + 2] = secret_key
    yaml[i + 3] = region

    return yaml


def create_secret_yaml():
    secret_yaml = yc.load_yaml_template(path="yaml_templates/secret_template.yaml")
    secret_yaml = add_aws_credentials_to_job(secret_yaml)
    yc.write_yaml_file(yaml=secret_yaml, path='secret.yaml')