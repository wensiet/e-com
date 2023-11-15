# ADD FORMS

curl -X 'POST' \
  'http://127.0.0.1:8000/api/add-order' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Comment",
  "field_name_1": "text",
  "field_name_2": "email"
}'

curl -X 'POST' \
  'http://127.0.0.1:8000/api/add-order' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "User",
  "field_name_1": "email",
  "field_name_2": "phone"
}'

curl -X 'POST' \
  'http://127.0.0.1:8000/api/add-order' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Order",
  "field_name_1": "phone",
  "field_name_2": "date"
}'

curl -X 'POST' \
  'http://127.0.0.1:8000/api/add-order' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "SMS",
  "field_name_1": "phone",
  "field_name_2": "text"
}'

