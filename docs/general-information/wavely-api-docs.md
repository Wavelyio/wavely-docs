# Wavely API Docs
This is the (evolving) documentation for the **Wavely API** for integration purposes.

The API is continuously being developed and once it reaches a certain feature state, versioning will be introduced.

To access this API, you need to have your designated API key and secret at the ready.

## Technical Details

The API expects JSON requests with the `Content-Type` header set to `application/json`.

# URL

The API is available at: `https://platform.wavely.io/externalsimcardapi`. Only HTTPS is available.

# Authentication

The API uses HTTP Basic Auth and expects one of your API key and secret pairs.

Every request against the API expects the *Authorization* header to be set. Otherwise the API will return a `401 – Unauthorized` response.

You have the ability to revoke specific credentials from your API management section, immediately invalidating the access using the credentials.

Only the owner and admin account types may view or modify the API credentials from your account.

## Authentication Example

Let's imagine that you have the following:

* API key: `7defeb3b-f03a-4cd8-a3c2-fea45a25abe4`
* API secret: `toyqdCALFai19uWofIDlxb6hp7ZhOlaf9sx5hTEK1GIOJKUR3y4wAkPTrzvSyHJz`

Then your basic auth header should look like this:
```
Authorization: Basic N2RlZmViM2ItZjAzYS00Y2Q4LWEzYzItZmVhNDVhMjVhYmU0OnRveXFkQ0FMRmFpMTl1V29mSURseGI2aHA3WmhPbGFmOXN4NWhURUsxR0lPSktVUjN5NHdBa1BUcnp2U3lISno=
```

# Contact

If you need some technical assistance, please e-mail **support@wavely.io**
