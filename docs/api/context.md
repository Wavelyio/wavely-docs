# Contexts
This is the API for contexts management.

* Get all contexts
* Add phone number to context
* Remove phone number from context

## API objects

### Context

Field               | Type                                       | Description
------------------- | -------------------------------------------| -------------------------------
name                | String                                     | Name of context
createdDate         | ISO 8601 DateTime UTC                      | Date when context is created
extensionDTOList    | List([Extension](/api/context/#extension)) | List of extensions for context

### Extension

Field               | Type                  | Description
------------------- | --------------------- | -----------------------------------------------
context             | String                | Dialplan name
extension           | String                | Pattern which defines coverage of dialplan
priority            | String                | Value of priority for action
app                 | String                | Asterisk dialplan application to execute
appData             | String                | Parameters for application
createdDate         | ISO 8601 DateTime UTC | Date when extension is created


## Endpoint: Get contexts

**Description**

Get all contexts

**Endpoint** `GET /asterisk/contexts`

**Response Payload**

List([Context](/api/context/#context))

**Example response**

```
[
    {
        "name": "asdads",
        "createdDate": "2022-02-11T15:14:38.142698",
        "extensionDTOList": [
            {
                "context": "asdads",
                "extension": "_+X.",
                "priority": "1",
                "app": "Dial",
                "appdata": "SIP/${EXTEN}@asd,20",
                "createdDate": "2022-02-17T10:58:19.002502"
            },
            {
                "context": "asdads",
                "extension": "_+X.",
                "priority": "2",
                "app": "Dial",
                "appdata": "SIP/${EXTEN}@asd,20",
                "createdDate": "2022-02-17T10:58:19.100778"
            }
        ]
    },
    {
        "name": "test",
        "createdDate": "2022-02-17T10:58:51.562599",
        "extensionDTOList": []
    }
]
```

## Endpoint: Add phone numbers to a context

**Description**

Add phone number to a specific context

**Endpoint:** `PUT /asterisk/contexts/{contextName}/phonenumbers`

**Path parameter**

Field           | Type          | Description
------------    | ------------  | ------------
contextName     | String        | Name of context phone number is attaching to


**Request Payload**

Field             | Type          | Description
------------      | ------------  | ------------
phoneNumbersList  | List(String)  | List of phone numbers to add to the context


## Endpoint: Delete phone numbers from a context

**Description**

Remove phone number from a specific context

**Endpoint:** `DELETE /asterisk/contexts/{contextName}/phonenumbers`

**Path parameter**

Field           | Type          | Description
------------    | ------------  | ------------
contextName     | String        | Name of context phone number is detaching from


**Request Payload**

Field             | Type          | Description
------------      | ------------  | ------------
phoneNumbersList  | List(String)  | List of phone numbers to remove from the context

