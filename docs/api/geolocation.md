# Geolocation
Using this API, you are able to get geographical location of SIM cards.

## Endpoint: Get latest location of a SIM

**Description**

Get the latest location of a SIM from the specified account.

**Endpoint**

```
GET /geolocations/latest
```

**Request Payload**

| Field                    | Type   | Description                                       |
|--------------------------|--------|---------------------------------------------------|
| imsi                     | String | The SIM card IMSI                                 |
| subTenantCompanyGlobalId | String | Optionally find activity for a sub-tenant company |

**Example**

```
{
	"imsi": "238429000230950",
	"subTenantCompanyGlobalId": "C-4bfe7c75-f68f-4b5c-8c5a-3dfc335ba003"
}
```

**Response Payload**

| Field      | Type          | Description                                                 |
|------------|---------------|-------------------------------------------------------------|
| imsi       | String        | The SIM card IMSI                                           |
| lat        | Double        | Latitude                                                    |
| lon        | Double        | Longitude                                                   |
| range      | Integer       | Range                                                       |
| createdAt  | LocalDateTime | Date and time of location creation                          |
| lastUpdate | LocalDateTime | Date and time of last location update                       |

## Endpoint: Get SIM card location history

**Description**

Get all SIM card locations between the specified start time and end time.

**Endpoint**

```
GET /geolocations
```

**Request Payload**

| Field                    | Type   | Description                                                              |
|--------------------------|--------|--------------------------------------------------------------------------|
| imsi                     | String | The SIM card IMSI                                                        |
| startUtcTime             | String | The start time (UTC) of the locations search, format:yyyy-MM-ddTHH:mm:ss |
| endUtcTime               | String | The end time (UTC) of the locations search, format:yyyy-MM-ddTHH:mm:ss   |
| subTenantCompanyGlobalId | String | Optionally find activity for a sub-tenant company                        |

**Example**

```
{
	"imsi": "238429000230950",
	"startUtcTime": "2022-10-20T10:00:00",
	"endUtcTime": "2022-10-21T21:59:59",
	"subTenantCompanyGlobalId": "C-4bfe7c75-f68f-4b5c-8c5a-3dfc335ba003"
}
```

**Response Payload**

| Field      | Type          | Description                                                 |
|------------|---------------|-------------------------------------------------------------|
| imsi       | String        | The SIM card IMSI                                           |
| lat        | Double        | Latitude                                                    |
| lon        | Double        | Longitude                                                   |
| range      | Integer       | Range                                                       |
| createdAt  | LocalDateTime | Date and time of location creation                          |
| lastUpdate | LocalDateTime | Date and time of last location update                       |
