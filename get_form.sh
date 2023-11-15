echo "Enter f_name1 value:"
read -r f_name1

echo "Enter f_name2 value:"
read -r f_name2

curl -X 'POST' "http://127.0.0.1:8000/api/get_form?f_name1=$f_name1&f_name2=$f_name2" -H 'accept: application/json'
