import requests
import couchdb
import json

user = "admin"
password = "admin"
couchserver = couchdb.Server("http://%s:%s@127.0.0.1:5984/" % (user, password))


dbname = "meals"
if dbname in couchserver:
    db = couchserver[dbname]
else:
    db = couchserver.create(dbname)


# url = "https://api.edamam.com/search"
# querystring = {"q":"pasta","app_id":"id","app_key":"key","from":"0","to":"100"}

# payload = ""
# headers = {
#     'Authorization': "Basic ************************"}

# response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
# print(response.json())

# with open('recipes.json', 'w') as outfile:
#     json.dump(response.json(), outfile)


with open('recipes.json') as json_file:
    data = json.load(json_file)
    # print(data['hits']) 
    for p in data['hits']:
        label = (p['recipe']['label'])
        ingredients = (p['recipe']['ingredients'])

        doc_id, doc_rev = db.save({'key': 'value'})

        docs = [{'Name': label}, {'Ingredients': ingredients}]
        for (success, doc_id, revision_or_exception) in db.update(docs):
            print(success, docid, revision_or_exception)