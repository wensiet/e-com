## Find forms by fields (e-com)

### Stack
- Python 3.9
- FastAPI
- MongoDB
- Uvicorn
- Docker
- Bash

### How to install
- Clone repository to your machine.
  ```bash
  git clone https://github.com/wensiet/e-com.git
  ```
- Run docker container
  ```bash
  docker-compose up --build
  ```
- The app is now available at http://127.0.0.1:8000

### How to use
- After the installation, you can go to http://127.0.0.1:8000/docs, there you can try the routes

OR
- Run the bash file, to add new forms in the database
  ```bash
  bash add_test_forms.sh
  ```
- After this, run another bash file and enter fields, that you want to scan
  ```bash
  bash get_form.sh
  ```


### Endpoints
- [/api/add-order](http://127.0.0.1:8000/api/add-order)
- - Method: ```POST```
- - Response example:
```json
{
  "msg": "OK"
}
```
- [/api/get_form](http://127.0.0.1:8000/api/get_form)
- - Method: ```POST```
- - Response examples:
```json
{
  "name": "Test",
  "field_name_1": "text",
  "field_name_2": "email"
}
```

```json
{
  "f_name1": "phone",
  "f_name2": "email"
}
```