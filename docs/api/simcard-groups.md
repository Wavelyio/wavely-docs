# Sim card groups API
This is the API for operator sim card group management.
A sim card can be part of only one group at a time.

* Get sim card groups
* Get sim card groups by name
* Get sim card group by id
* Delete sim card group by id
* Add sim cards to group
* Remove sim card from group

## API objects

### SimCardGroup
Field        	| Type          | Description
------------ 	| ------------- | ------------
globalId 		| String        | id of the sim card group
name 	        | String        | Name of the group
createdDate 	| String        | ISO 8601 datetime format
simCardCount 	| Integer       | Number of sim cards assigned to the group

## Endpoint: Get sim card groups

**Description**

Get all current sim card groups.

**Endpoint:** `GET /simcardgroups`

**Response Payload**

List([SimCardGroup](/api/simcard-groups/#simcardgroup))

## Endpoint: Get sim card group by name

**Description**

Get sim card groups by their name.

**Endpoint:** `GET /simcardgroups`

**Query parameters**

Field        	| Type          | Description
------------ 	| ------------- | ------------
name 		    | String        | Name to query for

**Response Payload**

List([SimCardGroup](/api/simcard-groups/#simcardgroup))

## Endpoint: Get sim card group by id

**Description**

Get sim card group by its id.

**Endpoint:** `GET /simcardgroups/{simCardGroupGlobalId}`

**Response Payload**

[SimCardGroup](/api/simcard-groups/#simcardgroup)

## Endpoint: Delete sim card group by id

**Description**

Delete sim card group by id

**Endpoint:** `DELETE /simcardgroups/{simCardGroupGlobalId}`

## Endpoint: Add sim card to group

**Description**

Add a collection of sim cards to a sim card group. Moving them if they already belong to a different group.

**Endpoint:** `POST /simcardgroups/{simCardGroupGlobalId}/simcards`

**Request Payload**

Field        	| Type          | Description
------------ 	| ------------- | ------------
iccList 		| List(String)  | List of icc numbers for sim cards to add to the group.

## Endpoint: Remove sim card from group

**Description**

Remove a sim card from a sim card group

**Endpoint:** `DELETE /simcardgroups/{simCardGroupGlobalId}/simcards/{icc}`
