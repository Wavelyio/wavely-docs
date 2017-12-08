# About
This is the (evolving) documentation for the **AxonMobile SimCard API** for integration purposes.

The API is continuously being developed and once it reaches a certain feature state, versioning will be introduced.

To access this API, you need to have your designated API key and secret at the ready.

## Technical Details

The API expects JSON requests with the `Content-Type` header set to `application/json`.

# URL

The API is available at: `https://preprod.axonmobileiot.com/simcardexternalapi`

# Authentication

The API simply uses HTTP basic auth and expects your API key and secret.

Every request against the API expects the HTTP basic auth header to be set. Otherwise the API will return `401 – Unauthorized`.

## Authentication Example

Let's imagine that you have the following:

* API key: `7defeb3b-f03a-4cd8-a3c2-fea45a25abe4`
* API secret: `toyqdCALFai19uWofIDlxb6hp7ZhOlaf9sx5hTEK1GIOJKUR3y4wAkPTrzvSyHJz`

Then your basic auth header should look like this:
```
Authorization: Basic N2RlZmViM2ItZjAzYS00Y2Q4LWEzYzItZmVhNDVhMjVhYmU0OnRveXFkQ0FMRmFpMTl1V29mSURseGI2aHA3WmhPbGFmOXN4NWhURUsxR0lPSktVUjN5NHdBa1BUcnp2U3lISno=
```

# Contact

If you need some technical assistance, please e-mail **someone@greenwavesystems.com**
