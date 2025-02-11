import boto3

client = boto3.client('cognito-idp', region_name='ap-south-1')

response = client.initiate_auth(
    AuthFlow='USER_PASSWORD_AUTH',
    AuthParameters={
        'USERNAME': 'b1135dda-a061-70c2-bb19-91310871c99b',
        'PASSWORD': 'Dhinesh007#'
    },
    ClientId='your-cognito-app-client-id'
)

id_token = response['AuthenticationResult']['IdToken']
print(id_token)
