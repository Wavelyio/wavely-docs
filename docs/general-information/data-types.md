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

## Company
Representation of company

| Field            | Type                  |
| ---------------- | --------------------- |
| accountManager   | List(AccountManager)  |
| accountManagerId | Integer               |
| alias            | String                |
| branding         | String                |
| createdDate      | String                |
| globalId         | String                |
| hasSubTenants    | Boolean               |
| id               | Integer               |
| name             | String                |
| parentTenantGuid | String                |
| updatedDate      | String                |
| vatNumnber       | String                |

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
* USER_WEB_ACTION
* USER_API_ACTION
* USER_TRIGGER
* SYSTEM_TRIGGER
* ADMIN_USER_ACTION
* OTHER

## DataSessionStates

Enumeration, may have the following values:

* CONNECTED
* NOT_CONNECTED
* HEARTBEAT

## SimCardActions

Enumeration, may have the following values:

* ACTIVATE
* SUSPEND
* RESET
* THROTTLE
* UNTHROTTLE

## SimCardTypes

Enumeration, may have the following values:

* STANDALONE
* VIRTUAL
* ESIM

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

## Network

Describes as telecommunications network:

| Field            | Type             |
| --------------- | --------------- |
| country              | Any alpha-2 country code            |
| tadig           | String           |
| plmn | String |

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

## BasicInvoice

Simple representation of an invoice

| Field             | Type                                                                      |
| ---------------   | ---------------                                                           |
| invoiceNumber               | Long                                                                    |
| startDate            | ISO 8601 Date                                                                    |
| endDate             | ISO 8601 Date                  |
| currencyCode  | String    |
| invoiceLines      | List([InvoiceLine](/general-information/data-types#BasicInvoiceLineDTO))   


## BasicInvoiceLine

Simple representation of an invoice line

| Field             | Type                                                                      |
| ---------------   | ---------------                                                           |
| quantity               | Number                                                                    |
| fromType            | [BillableType](/general-information/data-types#BillableType) |
| toType            | [BillableType](/general-information/data-types#BillableType) |
| fromCountry             | [CountryCode](/general-information/data-types#CountryCode) |
| toCountry             | [CountryCode](/general-information/data-types#CountryCode) |
| direction  | [Directions](/general-information/data-types#Directions) |
| productName      | String |
| chargeableName      | String |
| chargeablePackageName      | String |
| description      | String |


## DataUsageByCompany

| Field             | Type                                                                      |
| ---------------   | ---------------                                                           |
| totalValue               | Number                                                                    |
| year            | Number |
| month            | String |

## DataUsageBySimCardCollections

| Field             | Type                                                                      |
| ---------------   | ---------------                                                           |
| simCardCollectionGlobalId               | UUID                                                                    |
| totalValue               | Number                                                                    |
| year            | Number |
| month            | String |


## BillableType
Enumeration, may have the following values:

Value                   |
------------            |
VOICE                           |
SMS                             |
DATA                            |
SMPP_SMS                        |
MMS                             |
HTTP                            |
SUBSCRIPTION_BASE               |
SUBSCRIPTION_ACTIVE             |
CREDIT                          |
DEBIT                           |
DEBUG                           |
DEFAULT                         |
ALPHANUMERIC_SMS                |
CHARGEABLE_PACKAGE              |
SMPP_SUBSCRIPTION               |
STATIC_IP_SUBSCRIPTION          |
VPN_SUBSCRIPTION                |
CLOSED_NETWORK_SUBSCRIPTION     |     
SLA_PREMIUM_SUBSCRIPTION        |  
SETUP_AND_ALLOCATION            |
PHONE_NUMBER_ALLOCATION         | 

## CountryCode

Enumeration of country codes in ISO 3166-1 format, fx. "DK" and "FI"

## UserAccount

| Field            | Type                  |
| ---------------- | --------------------- |
| companyRoles     | List(String)          |
| email            | String                |
| firstName        | String                |
| globalId         | String                |
| createdDate      | String                |
| lastLoginDate         | String                |
| lastName    | String               |
| phoneNumber               | String               |

## Contract

Fields with String and Integer values

| Field      | 
| ---------- | 
| activationDate | 
| approverAccountId | 
| authorAccountId | 
| commitmentStartDate | 
| contractType | 
| createdDate | 
| description | 
| endDate | 
| globalId | 
| minimumCommitmentPerMonth | 
| name | 
| startDate | 
| uniqueGlobalId | 
| updatedDate | 
| version | 

## Invite

Fields with String, Integer and Arrays value

| Field      | Type |
| ---------- | ---- |
| companyId | Integer |
| companyRoles | Array |
| createdDate | String |
| email | String |
| firstName | String |
| id | String |
| inviteToken | String | 
| inviteTokenExpiryDate | String |
| invitedByAccountGlobalId | String |
| lastName | String |
| phoneNumber | String |
| resources | Array |


