# GEOLOCATION API
Using this API, you are able to get geographical location of sim cards.

## Endpoint: Get latest company location

**Description**

Gets the latest location of the company simcard.

**Endpoint**

```
GET /geolocations/latest
```

**Request Payload**

| Field                    | Type   | Description                                       |
|--------------------------|--------|---------------------------------------------------|
| imsi                     | String | The simcard IMSI                                  |
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
| imsi       | String        | The simcard IMSI                                            |
| mcc        | String        | Mobile country code                                         |
| mnc        | String        | Mobile network code                                         |
| lac        | String        | Location area code                                          |
| cellId     | String        | Unique number of base transceiver station (cell identifier) |
| lat        | Double        | Latitude                                                    |
| lon        | Double        | Longitude                                                   |
| range      | Integer       | Range                                                       |
| createdAt  | LocalDateTime | Date and time of location creation                          |
| lastUpdate | LocalDateTime | Date and time of last location update                       |

## Endpoint: Get all company locations

**Description**

Gets all simcard locations of the company.

**Endpoint**

```
GET /geolocations
```

**Request Payload**

| Field                    | Type   | Description                                                              |
|--------------------------|--------|--------------------------------------------------------------------------|
| imsi                     | String | The simcard IMSI                                                         |
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
| imsi       | String        | The simcard IMSI                                            |
| mcc        | String        | Mobile country code                                         |
| mnc        | String        | Mobile network code                                         |
| lac        | String        | Location area code                                          |
| cellId     | String        | Unique number of base transceiver station (cell identifier) |
| lat        | Double        | Latitude                                                    |
| lon        | Double        | Longitude                                                   |
| range      | Integer       | Range                                                       |
| createdAt  | LocalDateTime | Date and time of location creation                          |
| lastUpdate | LocalDateTime | Date and time of last location update                       |
