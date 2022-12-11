import requests
import sys
import pprint
import json


user_access_token = "eyJhbGciOiJIUzI1NiIsImV4cGlyZXNJbiI6IjMwbSIsImtpZCI6InNpbTIiLCJ0eXAiOiJKV1QifQ" \
                    ".eyJlbWFpbCI6ImFsZXhAZXhhbXBsZS5jb20iLCJyb2xlcyI6InVzZXIiLCJleHAiOjE2NzA3ODE5Njd9" \
                    ".42EAX0Mdykoc2iaqIyYQ5-aUTx4JIYt3_VJRyclrUb0 "

res = requests.get('http://localhost:8080/v1/users', headers={'Authorization': f'Bearer {user_access_token}'})

assert res.status_code == 200
pprint.pprint(
    json.loads(res.content.decode())
)