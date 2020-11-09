# Data types

## Page(Type)
The page response that the API will produce in case it supports pagination.
Page types are parameterised by the returned type, this is similar to something like List(String)

| Field            | Type                  |
| ---------------- | --------------------- |
| content          | List(Underlying type) |
| totalPages       | Integer               |
| last             | Boolean               |
| totalElements    | Integer               |
| size             | Integer               |
| number           | Integer               |
| numberOfElements | Integer               |
| first            | Boolean               |

## SimCard

Simple representation of a single SIM card in our system.

| Field             | Type                                                                      |
| ---------------   | ---------------                                                           |
| icc               | String                                                                    |
| msisdn            | String                                                                    |
| state             | [ImsiStates](/general-information/data-types#imsistates)                  |
| dataSessionState  | [DataSessionStates](/general-information/data-types#datasessionstates)    |
| networkSpeed      | [NetworkSpeed](/general-information/data-types#networkspeed)              |

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

## DataSessionStates

Enumeration, may have the following values:

* CONNECTED
* NOT_CONNECTED
* HEARTBEAT

## SimCardActions

Enumeration, may have the following values:

* SUSPEND
* ACTIVATE
* RESET

## RadioAccessTechnology

Enumeration, may have the following values:

Value        | Description          
------------ | ------------- 
UTRAN | 3G
GERAN | 2G
WLAN | String
GAN | String
HSPA_EVOLUTION | 3G or 4G
E_UTRAN | LTE or 4G 

## QCI

Enumeration, may have the following values:

Value        | Description          
------------ | ------------- 
QCI_1 | Conversational Voice
QCI_2 | Conversational Video (Live Streaming)
QCI_3 | Real Time Gaming, V2X messages
QCI_4 | Non-Conversational Video (Buffered Streaming)
QCI_5 | Mission Critical user plane Push To Talk voice (e.g., MCPTT)
QCI_6 | Non-Mission-Critical user plane Push To Talk voice
QCI_65 | Mission Critical user plane Push To Talk voice (e.g., MCPTT)
QCI_66 | Non-Mission-Critical user plane Push To Talk voice
QCI_69 | Mission Critical delay sensitive signalling (e.g., MC-PTT signalling)
QCI_7 | Voice, Video (Live Streaming), Interactive Gaming
QCI_70 | Mission Critical Data (e.g. example services are the same as QCI 6/8/9)
QCI_75 | V2X messages
QCI_79 | V2X messages
QCI_8 | Video (Buffered Streaming) TCP-Based (for example, www, email, chat, ftp, p2p and the like)
QCI_9 | Video (Buffered Streaming) TCP-Based (for example, www, email, chat, ftp, p2p and the like). Typically used as default bearer.

## Directions

Enumeration, may have the following values:

Value        | Description          
------------ | ------------- 
INCOMING | Incoming traffic
OUTGOING | Outgoing traffic
DEFAULT  | This value is only used if we are unable to determine in which direction traffic is flowing. 

## CallForwardingRuleStatus

Enumeration, may have the following values:

Value           | Description          
------------    | ------------- 
PENDING_CREATE  | Creation is underway
PENDING_UPDATE  | Update is underway
CREATED         | Creation or update finalized
FAILED          | Creation or update failed

## NetworkSpeed

Enumeration, may have the following values:

Value           | Description          
------------    | ------------- 
FULL            | No throttling is applied
KBIT_32         | 32 Kbit speed maximum throughput
KBIT_64         | 64 Kbit speed maximum throughput
KBIT_128        | 128 Kbit speed maximum throughput
KBIT_256        | 256 Kbit speed maximum throughput
KBIT_512        | 512 Kbit speed maximum throughput
MBIT_1          | 1 Mbit speed maximum throughput
MBIT_2          | 2 Mbit speed maximum throughput
MBIT_5          | 5 Mbit speed maximum throughput

## CompanyOperatorProfileActionMapping

Determines whether a profile is used for certain actions. E.g. when activating sim cards.

Value           | Description          
------------    | ------------- 
ACTIVATE        | Determines the "default" operator profile used when activating sim cards
SUSPEND         | Determines the profile used when suspend is used. This is controlled by the platform.

## ConnectivityCapabilityTypes

Defines what is enabled in a profile.

Value           | Description          
------------    | ------------- 
INGOING_VOICE   | Ingoing voice service enabled
OUTGOING_VOICE  | Outgoing voice service enabled
INGOING_SMS     | Ingoing sms service enabled
OUTGOING_SMS    | Outgoing sms service enabled
DATA            | Data service enabled
SMPP_SMS        | SMPP service enabled