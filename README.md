#### This project address the problem detailed here
https://gist.github.com/sarahwiemero/0aa5ff2d24196c65880936bbe80f6c52

### Components
- MongoDB (database to store employee information and groups)
- Flask (web application)
- Angular JS / Bootstrap (front-end)
- Data (Random data of 200 employees)


### Workflow
- UI (Generate Groups) --> Flask (kicks of group generator code) --> MongoDB (groups stored in mongo)

- UI (Group lookup) --> Flask (kicks of MongoDB query) ---> MongoDB returns result ---> Displayed on UI


### Future scope
- Integration with Slack to notify groups once generated
- Alternatively, send emails once groups are generated


![alt text](https://github.com/joshishwetha/apartmentlist/blob/master/apartment_list_ui.png)
