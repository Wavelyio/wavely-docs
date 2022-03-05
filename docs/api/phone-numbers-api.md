# Phone numbers
This is the API for phone numbers management in Asterisk

* Get all phone numbers
* Add phone number to company
* Add phone number to sub company  
* Remove phone number from company

## API objects

### PhoneNumber

Field               | Type                                       | Description
------------------- | -------------------------------------------| -------------------------------
phoneNumber         | String                                     | Phone number value
createdDate         | ISO 8601 DateTime UTC                      | Date when phone number is created


## Endpoint: Get phone numbers

**Description**

Get all phone numbers of company

**Endpoint** `GET /phonenumbers`

**Response Payload**

List([PhoneNumber](/api/phone-numbers-api/#phonenumber))

**Example response**

```
[
    {
        "phoneNumber": "+4511111111",
        "createdDate": "2022-02-16T08:37:09.453659"
    },
    {
        "phoneNumber": "+4522222222",
        "createdDate": "2022-02-16T08:37:09.644123"
    },
    {
        "phoneNumber": "+4533333333",
        "createdDate": "2022-02-17T12:43:26.640417"
    }
]
```

## Endpoint: Add phone number to a company

**Description**

Add phone number to company or sub tenant customer

**Endpoint:** `POST /phonenumbers`

**Request query parameters**

| Field             | Type   | Description                      | Required |
|-------------------|--------|----------------------------------|----------|
| subTenantGlobalId | String | UUID of your sub tenant customer | No       |

**Request payload**

| Field       | Type   | Description                                 |
|-------------|--------|---------------------------------------------|
| phoneNumber | String | Phone number you want to create in Asterisk |

**Response payload**

[PhoneNumber](/api/phone-numbers-api/#phonenumber)

**Response example**

```
{
    "phoneNumber": "+4522222222",
    "createdDate":  "2022-02-17T12:43:26.640417"
}
```

## Endpoint: Delete phone numbers from a company

**Description**

Remove phone number from your company

**Endpoint:** `DELETE /phonenumbers`

**Request Payload**

Field             | Type          | Description
------------      | ------------  | ------------
msisdn            | String        | Value of phone number which is going to be removed

