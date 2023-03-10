# SIM cards assigned

Indicates that a SIM card has been assigned to your account. Triggers for each assigned SIM card.

## Payload

**Response Payload**

| Field       | Type                                                          | Description                                                                                  |
|-------------|---------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| icc         | String                                                        | The ICC of the SIM card                                                                      |
| msisdn      | String                                                        | E164 MSISDN, e.g. *+4593709603*                                                              |
| state       | [ImsiStates](/general-information/data-types/#imsistates)     | The current state of the SIM card                                                            |
| pin1        | String                                                        |                                                                                              |
| pin2        | String                                                        |                                                                                              |
| puk1        | String                                                        |                                                                                              |
| puk2        | String                                                        |                                                                                              |
| simCardType | [SimCardTypes](/general-information/data-types/#simcardtypes) | The type of the SIM card                                                                     |
| matchingId  | String                                                        | A SIM card with type ESIM will have this value, which is needed for downloading ESIM profile |

**Example**

```json
{
    "icc": "89454209864904920296",
    "imsiState": "ACTIVE",
    "pin1": "1234",
    "pin2": "4321",
    "puk1": "123123",
    "puk2": "321321",
    "simCardType" : "STANDALONE",
    "matchingId" : "XYZ"
}
```
