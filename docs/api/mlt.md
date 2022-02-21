#Multi Level Tenancy API

MLT has brought several unic endpoints, but in general, it uses similair endoints, so description of them suits as well to MLT endpoints. The only difference for MLT is that all endpoints get extra query parameter **subTenantGuid**=`global id of company`

**Where MLT was implemented:**

* [Sim cards](/api/simcards-api/)
* [Sim cards groups](/api/simcard-groups/)
* [Sim cards diagnostics](/api/sim-card-diagnostics/)
* [Operator Profiles](/api/operator-profiles/)
* [Tags](/api/simcard-tags/)
* [Triggers]()
* [Invite owner](api/invite-owner/)

***

Unic API calls for MLT:

* Get subtenants of company
* Get sim cards of tenant itself and subtenants 

API expanded by MLT

* create and edit company account

***

### Get subtenants of company

**Endpoint:** `GET /tenant/companies`

**Response payload**

Response is array of [Company](/docs/general-information/data-types#company) objects

***

### Get sim cards of tenant itself and subtenants 

**Endpoint:** `GET /simcards/subtenants`

**Response payload**

Returns [Page](/general-information/data-types/#Page(Type))([Simcard](/general-information/data-types/#SimCard))

***

### Creating/Editing of account
It's an admin endpoints, that were expanded by new properties:

**Endpoints:** `POST /admin/companies` 
<br> and `PATCH /admin/companies`

**Response payload**

It returns [Company](/docs/general-information/data-types#company) object
of created/edited company. 

**Which MLT params has appeared in payload from client:**

| prop | type | description |
| ---- | ---- | ------------|
| parentTenantGuid | String | global id of parent company |
| parentTenant | Object | object of parent tenant company |
| hasParent | String | String representing a boolen |


> **parentTenant** and **hasParent** exist in payload in a sake of living in 
> redux-form(\*) values and being available for providing UI changes
> they do not handling on backend, backend require only **parentTenantGuid** prop(**)
>
> \* perhaps it should be refactored and omitted <br>
> \*\* but if there is no **parentTenantGuid** from client in POST request (create company),
> backend will take **globalId** of parent from **parentTenant** object




