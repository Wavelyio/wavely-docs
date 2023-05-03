# Multi Level Tenancy

MLT has brought several unique endpoints, but in general, it uses same endpoints.
<br>
To call API for subtenant, you should add query parameter: <br>
**subTenantCompanyGlobalId**=`global id of subtenant company`

**Where MLT was implemented:**

* [SIM cards](/api/simcards)
* [SIM card groups](/api/simcard-groups)
* [SIM card diagnostics](/api/simcard-diagnostics)
* [Operator Profiles](/api/operator-profiles)
* [Tags](/api/simcard-tag)
* [Triggers]()
<!-- * [Invite owner](api/invite-owner/) -->

***

**Besides that,** there are endpoints for:
 
* Get subtenants of company
* Get SIM cards of tenant itself and subtenants

***

### Get subtenants of company

**Endpoint:** `GET /tenant/companies`

**Response payload**

Response is array of subtenants [Company](/general-information/data-types#company) objects

***

### Get SIM cards of tenant itself and subtenants

**Endpoint:** `GET /simcards/subtenants`

**Response payload**

Returns [Page](/general-information/data-types#page(type))([SimCard](/general-information/data-types/#simcard))

***




