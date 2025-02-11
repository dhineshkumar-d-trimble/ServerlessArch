import boto3
import hmac
import hashlib
import base64

# Replace these values with your own
username = 'dhineshkumard'
password = 'Dhinesh007#'
client_id = '7g7esub8aq2ntu05nu1eh7err4'
client_secret = '1b1qd3mudm3dfa8c23dafm8h0oeh5jbur0i929q2kaug6p1ansaf'
region = 'ap-south-1'

def get_secret_hash(username, client_id, client_secret):
    message = username + client_id
    dig = hmac.new(client_secret.encode('utf-8'), message.encode('utf-8'), hashlib.sha256).digest()
    return base64.b64encode(dig).decode()

client = boto3.client('cognito-idp', region_name=region)

response = client.initiate_auth(
    AuthFlow='USER_PASSWORD_AUTH',
    AuthParameters={
        'USERNAME': username,
        'PASSWORD': password,
        'SECRET_HASH': get_secret_hash(username, client_id, client_secret)
    },
    ClientId=client_id
)

id_token = response['AuthenticationResult']['IdToken']
print(id_token)
