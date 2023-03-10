# Customers
This is the API to add your sub company in Asterisk

## API objects

### Customer

| Field        | Type                  | Description                   |
|--------------|-----------------------|-------------------------------|
| globalId     | String                | UUID of customer              |
| customerName | String                | Name of customer              |
| createdDate  | ISO 8601 DateTime UTC | Date when customer is created |

## Endpoint: Create new customer

**Description**

Create new customer in Asterisk

**Endpoint** `POST /voiceservice/customers`

**Request Payload**

| Field        | Type   | Description         |
|--------------|--------|---------------------|
| globalId     | String | UUID of sub company |
| customerName | String | Name of sub company |

**Response Payload**

[Customer](/api/voiceservice-customers/#customers)

**Example response**

```
{
  "globalId": "C-9b6e4aa1-3654-410d-8763-39b9a7036078",
  "customerName": "Customer #1",
  "createdDate": "2020-12-12T22:33:44"
}
```


