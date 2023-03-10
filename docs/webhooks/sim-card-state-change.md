# SIM card state change

Indicates that a SIM card has changed its IMSI state.

For example, a user activates or suspends the SIM card.

## Payload

| Field           | Type                                                                  | Description |
|-----------------|-----------------------------------------------------------------------|-------------|
| icc             | String                                                                |             |
| imsiState       | [ImsiState](/general-information/data-types/#imsistates)              |             |
| imsiStateReason | [ImsiStateReasons](/general-information/data-types/#imsistatereasons) |             |

**Example**

```json
{
	"icc": "89454284200010500060",
	"imsiState": "ACTIVE",
	"ImsiStateReasons": "USER_ACTION"
}
```