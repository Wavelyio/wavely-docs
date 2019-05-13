# Sim card state change

Indicates that a sim card has changed its IMSI state.

For example, the sim card was activated by a user.

## Payload

Field        | Type          | Description
------------ | ------------- | ------------
icc | String |
imsiState | ImsiStates |
imsiStateReason | ImsiStateReasons |

**Example**

```json
{
	"icc": "89454284200010500060",
	"imsiState": "ACTIVE",
	"ImsiStateReasons": "USER_ACTION"
}
```