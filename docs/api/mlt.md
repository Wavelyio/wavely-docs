#Multi Level Tenancy API

MLT has brought several unic endpoints, but in general, it uses similair endoints, so description of them suits as well to MLT endpoints. The only difference for MLT is that all endpoints get extra query parameter **subTenantGuid**=`global id of company`

**Where MLT was implemented:**

* [Sim cards](/api/simcards-api/)
* [Sim cards groups](/api/simcard-groups/)
* [Sim cards diagnostics](/api/sim-card-diagnostics/)
* [Operator Profiles](/api/operator-profiles/)
* Tags (api doesn't exist)
* [Triggers]()


### /Get subtenants of company

**Endpoint:** `GET /tenant/companies`

**Response payload**

Response is array of [Company](/docs/general-information/data-types#company) objects


### /Get sim cards of tenant itself and subtenants 

**Endpoint:** `GET /simcards/subtenants`

**Response payload**

Returns [Page](/general-information/data-types/#Page(Type))([Simcard](/general-information/data-types/#SimCard))


