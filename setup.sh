#! /bin/bash
set -e

echo "Build and start Compose file"
docker compose up --build -d
echo "Wait 5s to ensure the application is up and running"
sleep 5
echo "Make a POST request via api:"
curl -s --header "Content-Type: application/json" --request POST --data '{"message":"Olá Inoa"}' http://devops.localhost/api/add  | jq '.[].message'
echo "Make a GET request to api"
curl -s http://devops.localhost/api/ | jq '.[].message'
if grep -qi microsoft /proc/version; then
  echo "To see the result, open: http://devops.localhost/api/"
else
  echo "Load the result on your default browser with the URL: http://devops.localhost/api/"
  nohup xdg-open http://devops.localhost/api/ > /dev/null 2>&1
fi