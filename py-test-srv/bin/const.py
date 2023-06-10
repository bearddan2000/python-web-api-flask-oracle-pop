URL = 'http://py-srv:5000'

GET_ALL_URL = URL + '/pop'

GET_BY_FILTER_URL = URL + '/pop/name/Labrador'

STATIC = {  
    "results": [
    {
      "color": "brown",
      "id": 1,
      "name": "RC Cola"
    },
    {
      "color": "clear",
      "id": 2,
      "name": "Sprite"
    },
    {
      "color": "brown",
      "id": 3,
      "name": "Verners"
    },
    {
      "color": "green",
      "id": 4,
      "name": "Mt. Lightening"
    }
  ]
}

DELETE_URL = URL + '/pop/id/1'

INSERT_URL = URL + '/pop/name/Lemonade/color/Pink'

SMOKE_URL = URL + '/'

SMOKE = {"results": {"hello": "world"}}

UPDATE_URL = URL + '/pop/id/2'
