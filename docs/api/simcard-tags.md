# Sim card tag API
This is the API for operator sim card tag management.
A sim card can have multiple tags at a time unlike sim card groups. 

* Get sim card tags
* Create sim card tag
* Get sim card tag
* Update sim card tag
* Delete sim card tag
* Update tagged sim cards for tag

## API objects

### SimCardTag
Field        	| Type          | Description
------------ 	| ------------- | ------------
globalId 		| String        | id of the tag
tag 	        | String        | Name of the tag
createdDate 	| String        | ISO 8601 datetime format
updatedDate 	| String        | ISO 8601 datetime format

### DetailedSimCardTag
Field        	| Type                                                      | Description
------------ 	| -------------                                             | ------------
globalId 		| String                                                    | id of the tag
tag 	        | String                                                    | Name of the tag
createdDate 	| String                                                    | ISO 8601 datetime format
updatedDate 	| String                                                    | ISO 8601 datetime format
taggedSimCards 	| List([SimCard](/general-information/data-types/#simcard)) | List of tagged sim cards

## Endpoint: Get sim card tags

**Description**

Get all current sim card tags.

**Endpoint:** `GET /simcardtags`

**Response Payload**

[Page](/general-information/data-types/#page)([SimCardTag](/api/simcard-tags/#simcardtag))

## Endpoint: Create new sim card tag

**Description**

Create a new sim card tag

**Endpoint:** `POST /simcardtags`

**Request Payload**
Field        	| Type          | Description
------------ 	| ------------- | ------------
tag 		    | String        | Name of the new tag

**Response Payload**
[SimCardTag](/api/simcard-tags/#simcardtag)

## Endpoint: Get sim card tag

**Description**

Get sim card tag by its id.

**Endpoint:** `GET /simcardtags/{globalId}`

**Response Payload**

[DetailedSimCardTag](/api/simcard-tags/#detailedsimcardtag)

## Endpoint: Update sim card tag

**Description**

Update metadata for a sim card tag.

**Endpoint:** `PATCH /simcardtags/{globalId}`

**Request Payload**

Field        	| Type          | Description
------------ 	| ------------- | ------------
newName 		| String        | New name of the tag. This corresponds to the "tag" property of the tag


## Endpoint: Delete sim card tag

**Description**

Delete sim card tag by id. This will also remove the tag from all sim cards that had that tag.

**Endpoint:** `DELETE /simcardtags/{globalId}`

## Endpoint: Update tagged sim cards for tag

**Description**

Tag and untag sim cards for a specific sim card.

**Endpoint:** `PATCH /simcardtags/{globalId}/simcards`

**Request Payload**
Field        	    | Type          | Description
------------ 	    | ------------- | ------------
simCardsToAdd 	    | List(String)  | List of icc numbers for sim cards to tag.
simCardsToRemove    | List(String)  | List of icc numbers for sim cards to untag.
