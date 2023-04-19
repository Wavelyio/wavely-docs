# SIM card groups API
This is the API for operator SIM card group management.
A SIM card can be part of only one group at a time.

* Get SIM card groups
* Get SIM card groups by name
* Get SIM card group by id
* Delete SIM card group by id
* Add SIM cards to group
* Remove SOM card from group

## API objects

### SimCardGroup
| Field        | Type    | Description                               |
|--------------|---------|-------------------------------------------|
| globalId     | String  | id of the SIM card group                  |
| name         | String  | Name of the group                         |
| createdDate  | String  | ISO 8601 datetime format                  |
| simCardCount | Integer | Number of SIM cards assigned to the group |

## Endpoint: Get SIM card groups

**Description**

Get all current SIM card groups.

**Endpoint:** `GET /simcardgroups`

**Response Payload**

List([SimCardGroup](../simcard-groups/#simcardgroup))

## Endpoint: Get SIM card group by name

**Description**

Get SIM card groups by their name.

**Endpoint:** `GET /simcardgroups`

**Query parameters**

| Field | Type   | Description       |
|-------|--------|-------------------|
| name  | String | Name to query for |

**Response Payload**

List([SimCardGroup](../simcard-groups/#simcardgroup))

## Endpoint: Get SIM card group by id

**Description**

Get SIM card group by its id.

**Endpoint:** `GET /simcardgroups/{simCardGroupGlobalId}`

**Response Payload**

[SimCardGroup](../simcard-groups/#simcardgroup)

## Endpoint: Delete SIM card group by id

**Description**

Delete SIM card group by id

**Endpoint:** `DELETE /simcardgroups/{simCardGroupGlobalId}`

## Endpoint: Add SIM card to group

**Description**

Add a collection of SIM cards to a SIM card group. Moving them if they already belong to a different group.

**Endpoint:** `POST /simcardgroups/{simCardGroupGlobalId}/simcards`

**Request Payload**

| Field   | Type         | Description                                            |
|---------|--------------|--------------------------------------------------------|
| iccList | List(String) | List of icc numbers for SIM cards to add to the group. |

## Endpoint: Remove SIM card from group

**Description**

Remove a SIM card from a SIM card group

**Endpoint:** `DELETE /simcardgroups/{simCardGroupGlobalId}/simcards/{icc}`
