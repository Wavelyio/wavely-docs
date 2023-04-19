# Operator profiles
This is the API for operator profile management.

* Get Operator profiles
* Get default operator profile
* Get specific operator profiles
* Clone an operator profile with modifications
* Update operator profiles
* Delete an operator profile
* Get available configurations for operator profiles

## API objects

### Profile
| Field         | Type                                                                                              | Description                                                                   |
|---------------|---------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| id            | Long                                                                                              | id of the operator profile                                                    |
| createdDate   | String                                                                                            | ISO 8601 datetime format                                                      |
| updatedDate   | String                                                                                            | ISO 8601 datetime format                                                      |
| name          | String                                                                                            | Name of the operator profile                                                  |
| description   | String                                                                                            | Accompanying description for the operator profile                             |
| identifier    | String                                                                                            | Global identifier for the operator profile, usefull for troubleshooting cases |
| actionMapping | [OperatorProfileActionMapping](../../general-information/data-types#operatorprofileactionmapping) | the action mapping if any, that the operator profile is used for.             |

### SlimmedOperatorProfile

| Field                  | Type                                    | Description                                            |
|------------------------|-----------------------------------------|--------------------------------------------------------|
| simcardCount           | Long                                    | The number of SIM cards that use this operator profile |
| companyOperatorProfile | [Profile](../operator-profiles#profile) | Profile meta data                                      |

### FullOperatorProfile

| Field                  | Type                                                                                                              | Description                                                                                 |
|------------------------|-------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| simcardCount           | Long                                                                                                              | The number of SIM cards that use this operator profile                                      |
| companyOperatorProfile | [Profile](../operator-profiles#profile)                                                                           | Profile meta data                                                                           |
| config                 | Map(String, List([ConnectivityCapabilityType](../../general-information/data-types#connectivitycapabilitytypes))) | The "String" key represents the alpha2 country code where the list of services are enabled. |

## Endpoint: Get Operator profiles

**Description**

Get all current operator profiles.

**Endpoint:** `GET /operatorprofiles`

**Response Payload**

List([SlimmedOperatorProfile](../operator-profiles/#slimmedoperatorprofile))

## Endpoint: Get default operator profile

**Description**

Get currently default operator profile

**Endpoint:** `GET /operatorprofiles/default`

**Response Payload**

List([FullOperatorProfile](../operator-profiles/#fulloperatorprofile))

## Endpoint: Get specific operator profiles

**Description**

Get list of specific operator profiles

**Endpoint:** `GET /operatorprofiles/{operatorProfileIds}`

**Response Payload**

List([FullOperatorProfile](../operator-profiles/#fulloperatorprofile))

## Endpoint: Create new operator profile

**Description**

Create a new operator profile

**Endpoint:** `POST /operatorprofiles`

**Request Payload**

| Field         | Type                                                                                                              | Description                                                                                 |
|---------------|-------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| name          | String                                                                                                            | The number of SIM cards that use this operator profile                                      |
| description   | String                                                                                                            | Profile meta data                                                                           |
| actionMapping | [OperatorProfileActionMapping](../../general-information/data-types#operatorprofileactionmapping)                 | The "String" key represents the alpha2 country code where the list of services are enabled. |
| config        | Map(String, List([ConnectivityCapabilityType](../../general-information/data-types#connectivitycapabilitytypes))) | The "String" key represents the alpha2 country code where the list of services are enabled. |

**Response Payload**

[FullOperatorProfile](../operator-profiles/#fulloperatorprofile)

## Endpoint: Clone existing operator profile

**Description**

Clone an existing operator profile with some changes applied at creation.

**Endpoint:** `PATCH /operatorprofiles/{operatorProfileId}`

**Request Payload**

| Field        | Type                                                                                                              | Description                                               |
|--------------|-------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| name         | String                                                                                                            | The number of SIM cards that use this operator profile    |
| removeConfig | Map(String, List([ConnectivityCapabilityType](../../general-information/data-types#connectivitycapabilitytypes))) | Configurations to remove from the cloned operator profile |
| addConfig    | Map(String, List([ConnectivityCapabilityType](../../general-information/data-types#connectivitycapabilitytypes))) | Configurations to add to the cloned operator profile      |

**Response Payload**

[FullOperatorProfile](../operator-profiles/#fulloperatorprofile)


## Endpoint: Update existing operator profiles

**Description**

Update configuration for existing profiles.

**Endpoint:** `PATCH /operatorprofiles`

**Request Payload**

| Field       | Type                                                                                                              | Description                                         |
|-------------|-------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| id          | Long                                                                                                              | Id of the operator profile to apply the updates to  |
| name        | String                                                                                                            | Update the name if specified                        |
| description | String                                                                                                            | Update the description if specified                 |
| config      | Map(String, List([ConnectivityCapabilityType](../../general-information/data-types#connectivitycapabilitytypes))) | New configurations to apply to the operator profile |

**Response Payload**

List([SlimmedOperatorProfile](../operator-profiles/#slimmedoperatorprofile))

## Endpoint: Delete an operator profile

**Description**

Delete an operator profile if it exists. 
An operator profile can only be deleted if it is not currently in use by any SIM cards.

**Endpoint:** `DELETE /operatorprofiles/{operatorProfileId}`

**Endpoint:** `GET /allowedconfigs`

**Response Payload**

| Field   | Type                                                                                                              | Description                                    |
|---------|-------------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| configs | Map(String, List([ConnectivityCapabilityType](../../general-information/data-types#connectivitycapabilitytypes))) | Available configurations for operator profiles |
