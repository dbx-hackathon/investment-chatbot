source/pull_data

folder for storing code for pulling data from youtube

===

key authentication:

POST https://language.googleapis.com/v1/documents:analyzeEntities?key=API_KEY


video search:

curl \
  'https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=100&q=stock%20investment&key=AIzaSyD5eAKGB7ZIzZQevscrNyTyUgPO2FEb1IE' \
  --header 'Accept: application/json' \
  --compressed