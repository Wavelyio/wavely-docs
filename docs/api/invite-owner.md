#Invite owner
Introducing API calls which exist in invite owner section

* Get companies 
* Get single company info 
* Get simcards count of company
* Get accounts of company
* Get invites of company
* Get contracts of company
* Invite owner
* Resend invite
* Remove invite
* Check if email is busy
* Delete Owner

## Get companies 
Getting list of companies to select 

**Endpoint:** `GET /admin/companies`
<br>
**MLT Endpoint:** `GET /tenant/companies`

**Response payload**

Returns [Page](../../general-information/data-types/#page(type))([Company](../../general-information/data-types/#company))

***

## Get company info

**Endpoint:** `GET admin/companies/${companyGlobalId}`
<br>
**MLT Endpoint:** `GET company?subTenantGuid=${subTenantGuid}`

**Response payload** 

Returns [Company](../../general-information/data-types/#company)

***

## Get simcards count of company

**Endpoint:** `GET admin/companies/${companyGlobalId}/simcards/count`
<br>
**MLT Endpoint:** `GET company/simcards/${companyGlobalId}/count`

**Response payload** 

Returns number of simcards:Integer

***

## Get accounts of company
Get account for find owner one and load his data to form

**Endpoint:** `GET /admin/companies/${companyGlobalId}/accounts`
<br>
**MLT Endpoint:** `GET company/accounts?subTenantGuid=${subTenantGuid}`

**Response payload**

returns Array of ([User](../../general-information/data-types/#useraccount))

***

## Get invites of company
Getting invites

**Endpoint:** `GET admin/companies/${companyGlobalId}/invites`
<br>
**MLT Endpoint:** `GET company/accounts/invites?subTenantGuid=${subTenantGuid}`

**Response payload**

returns Array of ([Invite](../../general-information/data-types/#invite))

***

## Get contracts of company
Get account for find owner one and load his data to form

**Endpoint:** `GET /admin/companies/${companyGlobalId}/contracts`
<br>
**MLT Endpoint:** `GET companies/contract/list?subTenantGuid=${subTenantGuid}`

**Response payload**

returns Array of ([Contract](../../general-information/data-types/#contract))

***

## Invite owner

**Endpoint:** `GET `
<br>
**MLT Endpoint:** `GET ?subTenantGuid=${subTenantGuid}`

**Response payload**

returns 

***

## Resend Invite

**Endpoint:** `POST admin/companies/${companyGlobalId}/invites/${inviteId}/resend`
<br>
**MLT Endpoint:** `POST /company/accounts/invites/${inviteId}/resend`

**Response payload**

returns 

***

## Remove Invite


**Endpoint:** `DELETE /admin/companies/${companyGlobalId}/invites/${inviteId}`
<br>
**MLT Endpoint:** `DELETE /company/accounts/invites/${inviteId}`

**Response payload**

returns deleted [Invite](../../general-information/data-types/#invite) 

***

## Check if email is busy

**Endpoint:** `GET /admin/companies/${companyGlobalId}/accounts/check-email?email=${email}`
<br>
**MLT Endpoint:** `GET /company/accounts/check-email?subTenantGuid=${subTenantGuid}&email=${email}`

***

## Delete owner

**Endpoint:** `GET admin/companies/${companyGlobalId}/accounts/${accountGlobalId}/ownership`
<br>
**MLT Endpoint:** `GET company/accounts/${accountGlobalId}/ownership?subTenantGuid=${subTenantGuid}`

***


