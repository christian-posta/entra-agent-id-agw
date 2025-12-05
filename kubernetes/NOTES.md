Get the blueprint's access token:

```bash
curl -v localhost:5000/AuthorizationHeaderUnauthenticated/graph
```

Once this is fixed, this will work:
https://github.com/AzureAD/microsoft-identity-web/issues/3643

```bash
curl -v "localhost:5000/AuthorizationHeaderUnauthenticated/graph?optionsOverride.RequestAppToken=true"
```

Get the token for the agent's identity:
```bash
curl -v "localhost:5000/AuthorizationHeaderUnauthenticated/graph?AgentIdentity=58326923-8cbc-4ef2-a30b-9c2a9684dbb1"
```

Get token as agent user identity (if agent has a user identity)

```bash
# Using UPN
curl -v "localhost:5000/AuthorizationHeaderUnauthenticated/graph?AgentIdentity=58326923-8cbc-4ef2-a30b-9c2a9684dbb1&AgentUsername=myagent@contoso.com"

# Using OID
curl -v "localhost:5000/AuthorizationHeaderUnauthenticated/graph?AgentIdentity=58326923-8cbc-4ef2-a30b-9c2a9684dbb1&AgentUserId=<user-oid-guid>"
```

Calling the graph API as Agent Identity:
```bash
curl -v -X POST "localhost:5000/DownstreamApiUnauthenticated/graph?AgentIdentity=58326923-8cbc-4ef2-a30b-9c2a9684dbb1" \
  -H "Content-Type: application/json"
```

Additional reference:


### Available Endpoints

| Endpoint | Method | Auth Required | Description |
|----------|--------|---------------|-------------|
| `/healthz` | GET | No | Health check |
| `/Validate` | GET | Yes (Bearer) | Validates incoming token, returns claims |
| `/AuthorizationHeader/{apiName}` | GET | Yes (Bearer) | Gets token using caller's identity (OBO) |
| `/AuthorizationHeaderUnauthenticated/{apiName}` | GET | No | Gets token using Blueprint's app identity |
| `/DownstreamApi/{apiName}` | POST | Yes (Bearer) | Proxies API call with caller's identity |
| `/DownstreamApiUnauthenticated/{apiName}` | POST | No | Proxies API call with Blueprint's identity |