# SIM card tag
This is the API for operator SIM card tag management.
A SIM card can have multiple tags at a time unlike SIM card groups.

* Get SIM card tags
* Create SIM card tag
* Get SIM card tag
* Update SIM card tag
* Delete SIM card tag
* Update tagged SIM cards for tag

## API objects

### SimCardTag
| Field        | Type   | Description              |
|--------------|--------|--------------------------|
| globalId     | String | id of the tag            |
| tag          | String | Name of the tag          |
| createdDate  | String | ISO 8601 datetime format |
| updatedDate  | String | ISO 8601 datetime format |

### DetailedSimCardTag
| Field          | Type                                                           | Description              |
|----------------|----------------------------------------------------------------|--------------------------|
| globalId       | String                                                         | id of the tag            |
| tag            | String                                                         | Name of the tag          |
| createdDate    | String                                                         | ISO 8601 datetime format |
| updatedDate    | String                                                         | ISO 8601 datetime format |
| taggedSimCards | List([SimCard](../../general-information/data-types/#simcard)) | List of tagged SIM cards |

## Endpoint: Get SIM card tags

**Description**

Get all current SIM card tags.

**Endpoint:** `GET /simcardtags`

**Response Payload**

[Page](../../general-information/data-types/#page)([SimCardTag](../simcard-tags/#simcardtag))

## Endpoint: Create new SIM card tag

**Description**

Create a new SIM card tag

**Endpoint:** `POST /simcardtags`

**Request Payload**

| Field | Type   | Description         |
|-------|--------|---------------------|
| tag   | String | Name of the new tag |


**Response Payload**

[SimCardTag](../simcard-tags/#simcardtag)

## Endpoint: Get SIM card tag

**Description**

Get SIM card tag by its id.

**Endpoint:** `GET /simcardtags/{globalId}`

**Response Payload**

[DetailedSimCardTag](../simcard-tags/#detailedsimcardtag)

## Endpoint: Update SIM card tag

**Description**

Update metadata for a SIM card tag.

**Endpoint:** `PATCH /simcardtags/{globalId}`

**Request Payload**

| Field   | Type   | Description                                                            |
|---------|--------|------------------------------------------------------------------------|
| newName | String | New name of the tag. This corresponds to the "tag" property of the tag |

## Endpoint: Delete SIM card tag

**Description**

Delete SIM card tag by id. This will also remove the tag from all SIM cards that had that tag.

**Endpoint:** `DELETE /simcardtags/{globalId}`

## Endpoint: Update tagged SIM cards for tag

**Description**

Tag and untag SIM cards for a specific SIM card.

**Endpoint:** `PATCH /simcardtags/{globalId}/simcards`

**Request Payload**

| Field            | Type         | Description                                 |
|------------------|--------------|---------------------------------------------|
| simCardsToAdd    | List(String) | List of icc numbers for SIM cards to tag.   |
| simCardsToRemove | List(String) | List of icc numbers for SIM cards to untag. |
