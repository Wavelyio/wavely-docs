#Multi Level Tenancy API

MLT has brought several unic endpoints, but in general, it uses same endoints.
<br>
To call API for subtnenant, you should add query parameter: <br>
**subTenantCompanyGlobalId**=`global id of subtenant company`

**Where MLT was implemented:**

* [Sim cards](/api/simcards-api/)
* [Sim cards groups](/api/simcard-groups/)
* [Sim cards diagnostics](/api/sim-card-diagnostics/)
* [Operator Profiles](/api/operator-profiles/)
* [Tags](/api/simcard-tags/)
* [Triggers]()
<!-- * [Invite owner](api/invite-owner/) -->

***

**Beside that,** there are endpoints for:
 
* Get subtenants of company
* Get sim cards of tenant itself and subtenants 

***

### Get subtenants of company

**Endpoint:** `GET /tenant/companies`

**Response payload**

Response is array of subtenants [Company](/docs/general-information/data-types#company) objects

***

### Get sim cards of tenant itself and subtenants 

**Endpoint:** `GET /simcards/subtenants`

**Response payload**

Returns [Page](/general-information/data-types/#Page(Type))([Simcard](/general-information/data-types/#SimCard))

***




