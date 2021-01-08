# SIM card API
This is the API for invoice management. We currently expose the following action:

* Get invoice for a specified month in a year.

## Endpoint: Get invoice

**Description**

Get invoice for the specified month and year. 
If the month is current not-finished month, the invoice will be the most recent snapshot.

**Endpoint:** `GET /invoice/{year}/{month}`

**Request Query Parameters**

| Field        | Type    | Description                | Required |
| ------------ | ------- | -------------------------- | -------- |
| year         | Integer | Year for the invoice in ISO 8601 format      | Yes       |
| month        | String  | Month for invoice, fx "may"| Yes       |


**Response Payload**

[Invoice](/general-information/data-types/#BasicInvoice)

