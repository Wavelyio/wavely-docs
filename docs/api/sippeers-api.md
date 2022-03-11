# SIP peers
This is the API for retrieving Asterisk SIP peers

## API objects

### SIPPeer

Field               | Type                                       
------------------- | -------------------------------------------
customerId          | Integer                                    
disabled            | Boolean                                    
name                | String                                     
context             | String                                      
deny                | String                                       
permit              | String                                       
secret              | String                                       
transport           | String                                       
host                | String                                       
nat                 | String                                       
peerType            | String                                       
defaultIp           | String                                       
dtmfmode            | String                                       
insecure            | String                                       
qualify             | String                                       
disallow            | String                                       
allow               | String                                       
fullContact         | String                                       
ipAddress           | String                                       
port                | String                                       
defaultUser         | String                                       
directMedia         | String                                       
outboundProxy       | String                                       
rtpTimeout          | Integer                                      
rtpHoldTimeout      | Integer                                     
disallow            | String                                       
lastms              | Integer                                      
regServer           | String                                       
regSeconds          | Integer                                      
userAgent           | String                                       
callbackExtension   | String                                       
createdDate         | String                                     


## Endpoint: Get phone numbers

**Description**

Get all SIP peers configured for company

**Endpoint** `GET /asterisk/sippeers`

**Response Payload**

List([SIPPeer](/api/phone-numbers-api/#sippeer))

**Example response**

```
[
    {
        "customerId": 1,
        "disabled": false,
        "name": "telenor_out",
        "context": "incoming",
        "deny": "",
        "permit": "",
        "secret": null,
        "transport": "UDP",
        "host": "10.8.32.11",
        "nat": "NO",
        "peerType": "PEER",
        "defaultIp": "0.0.0.0",
        "dtmfmode": "RFC2833",
        "insecure": "NO",
        "qualify": null,
        "disallow": "ALL",
        "allow": "ALAW_ULAW",
        "fullContact": "",
        "ipAddress": "10.8.32.11",
        "port": "5060",
        "defaultUser": "",
        "directMedia": "NO",
        "outboundProxy": null,
        "rtpTimeout": 60,
        "rtpHoldTimeout": 60,
        "lastms": 0,
        "regServer": "",
        "regSeconds": 0,
        "userAgent": null,
        "callbackExtension": "",
        "createdDate": "2022-02-17T13:18:22.553229"
    }
]
```

