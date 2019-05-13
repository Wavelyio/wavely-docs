# Data Types

## SimCard

Simple representation of a single sim card in our system.

| Field            | Type             |
| :--------------- | :--------------- |
| icc              | String           |
| msisdn           | String           |
| state            | SimCardState     |
| operatorName     | String           |
| dataSessionState | DataSessionState |

## ImsiStates

Enumeration, may have the following values:

* OPEN
* ACTIVE
* SUSPENDED
* TERMINATED
* DISCARDED

## ImsiStateReasons

Enumeration, may have the following values:

* NONE
* DISALLOWED_IMEI
* USER_ACTION
* CREDIT_LIMIT_EXCEEDED
* CREDIT_LIMIT_EXCEEDED_CEASED
* TRIGGER
* OTHER
* ADMIN_USER_ACTION


## DataSessionState

Enumeration, may have the following values:

* CONNECTED
* NOT_CONNECTED
* HEARTBEAT

## SimCardActions

Enumeration, may have the following values:

* SUSPEND
* ACTIVATE
* TERMINATE
* RESET