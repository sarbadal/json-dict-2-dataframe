sample1 = {
    "quiz": {
        "sport": {
            "q1": {
                "question": "Which one is correct team name in NBA?",
                "options": [
                    "New York Bulls",
                    "Los Angeles Kings",
                    "Golden State Warriros",
                    "Huston Rocket"
                ],
                "answer": "Huston Rocket"
            }
        },
        "maths": {
            "q1": {
                "question": "5 + 7 = ?",
                "options": [
                    "10",
                    "11",
                    "12",
                    "13"
                ],
                "answer": "12"
            },
            "q2": {
                "question": "12 - 8 = ?",
                "options": [
                    "1",
                    "2",
                    "3",
                    "4"
                ],
                "answer": "4"
            }
        }
    }
}

sample2 = {
    "fruit": "Apple",
    "size": "Large",
    "color": "Red"
}

sample3 = {"entities": {
    "hashtags": [{
      "text": "Angular",
      "indices": [103, 111]
    }],
    "symbols": [{"key": 11}],
    "user_mentions": [{"unknown_id": -9}],
    "urls": [{
      "url": "https://t.co/xFox78juL1",
      "expanded_url": "http://buff.ly/2sr60pf",
      "display_url": "buff.ly/2sr60pf",
      "indices": [79, 102]
    }]
  }
}

sample4 = [{
  "_id": {
    "$oid": "5968dd23fc13ae04d9000001"
  },
  "product_name": "sildenafil citrate",
  "supplier": "Wisozk Inc",
  "quantity": 261,
  "unit_cost": "$10.47"
}, {
  "_id": {
    "$oid": "5968dd23fc13ae04d9000002"
  },
  "product_name": "Mountain Juniperus ashei",
  "supplier": "Keebler-Hilpert",
  "quantity": 292,
  "unit_cost": "$8.74"
}, {
  "_id": {
    "$oid": "5968dd23fc13ae04d9000003"
  },
  "product_name": "Dextromathorphan HBr",
  "supplier": "Schmitt-Weissnat",
  "quantity": 211,
  "unit_cost": "$20.53"
}, {
  "_id": {
    "$oid": "5968dd23fc13ae04d9000004"
  },
  "product_name": "Dextromathorphan HBr",
  "supplier": "Schmitt-Weissnat",
  "quantity": 100,
  "unit_cost": "$21.53"
}]


x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann", "Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

x1 = {
    "medications":[{
            "aceInhibitors":[{
                "name":"lisinopril",
                "strength":"10 mg Tab",
                "dose":"1 tab",
                "route":"PO",
                "sig":"daily",
                "pillCount":"#90",
                "refills":"Refill 3"
            }],
            "antianginal":[{
                "name":"nitroglycerin",
                "strength":"0.4 mg Sublingual Tab",
                "dose":"1 tab",
                "route":"SL",
                "sig":"q15min PRN",
                "pillCount":"#30",
                "refills":"Refill 1"
            }],
            "anticoagulants":[{
                "name":"warfarin sodium",
                "strength":"3 mg Tab",
                "dose":"1 tab",
                "route":"PO",
                "sig":"daily",
                "pillCount":"#90",
                "refills":"Refill 3"
            }],
            "betaBlocker":[{
                "name":"metoprolol tartrate",
                "strength":"25 mg Tab",
                "dose":"1 tab",
                "route":"PO",
                "sig":"daily",
                "pillCount":"#90",
                "refills":"Refill 3"
            }],
            "diuretic":[{
                "name":"furosemide",
                "strength":"40 mg Tab",
                "dose":"1 tab",
                "route":"PO",
                "sig":"daily",
                "pillCount":"#90",
                "refills":"Refill 3"
            }],
            "mineral":[{
                "name":"potassium chloride ER",
                "strength":"10 mEq Tab",
                "dose":"1 tab",
                "route":"PO",
                "sig":"daily",
                "pillCount":"#90",
                "refills":"Refill 3"
            }]
        }
    ],
    "labs":[{
        "name":"Arterial Blood Gas",
        "time":"Today",
        "location":"Main Hospital Lab"
        },
        {
        "name":"BMP",
        "time":"Today",
        "location":"Primary Care Clinic"
        },
        {
        "name":"BNP",
        "time":"3 Weeks",
        "location":"Primary Care Clinic"
        },
        {
        "name":"BUN",
        "time":"1 Year",
        "location":"Primary Care Clinic"
        },
        {
        "name":"Cardiac Enzymes",
        "time":"Today",
        "location":"Primary Care Clinic"
        },
        {
        "name":"CBC",
        "time":"1 Year",
        "location":"Primary Care Clinic"
        },
        {
        "name":"Creatinine",
        "time":"1 Year",
        "location":"Main Hospital Lab"
        },
        {
        "name":"Electrolyte Panel",
        "time":"1 Year",
        "location":"Primary Care Clinic"
        },
        {
        "name":"Glucose",
        "time":"1 Year",
        "location":"Main Hospital Lab"
        },
        {
        "name":"PT/INR",
        "time":"3 Weeks",
        "location":"Primary Care Clinic"
        },
        {
        "name":"PTT",
        "time":"3 Weeks",
        "location":"Coumadin Clinic"
        },
        {
        "name":"TSH",
        "time":"1 Year",
        "location":"Primary Care Clinic"
        }
    ],
    "imaging":[{
        "name":"Chest X-Ray",
        "time":"Today",
        "location":"Main Hospital Radiology"
        },
        {
        "name":"Chest X-Ray",
        "time":"Today",
        "location":"Main Hospital Radiology"
        },
        {
        "name":"Chest X-Ray",
        "time":"Today",
        "location":"Main Hospital Radiology"
        }
    ]
}

x2 = {
  "destination_addresses": [
    "Washington, DC, USA",
    "Philadelphia, PA, USA",
    "Santa Barbara, CA, USA",
    "Miami, FL, USA",
    "Austin, TX, USA",
    "Napa County, CA, USA"
  ],
  "origin_addresses": [
    "New York, NY, USA"
  ],
  "rows": [{
    "elements": [{
        "distance": {
          "text": "227 mi",
          "value": 365468
        },
        "duration": {
          "text": "3 hours 54 mins",
          "value": 14064
        },
        "status": "OK"
      },
      {
        "distance": {
          "text": "94.6 mi",
          "value": 152193
        },
        "duration": {
          "text": "1 hour 44 mins",
          "value": 6227
        },
        "status": "OK"
      },
      {
        "distance": {
          "text": "2,878 mi",
          "value": 4632197
        },
        "duration": {
          "text": "1 day 18 hours",
          "value": 151772
        },
        "status": "OK"
      },
      {
        "distance": {
          "text": "1,286 mi",
          "value": 2069031
        },
        "duration": {
          "text": "18 hours 43 mins",
          "value": 67405
        },
        "status": "OK"
      },
      {
        "distance": {
          "text": "1,742 mi",
          "value": 2802972
        },
        "duration": {
          "text": "1 day 2 hours",
          "value": 93070
        },
        "status": "OK"
      },
      {
        "distance": {
          "text": "2,871 mi",
          "value": 4620514
        },
        "duration": {
          "text": "1 day 18 hours",
          "value": 152913
        },
        "status": "OK"
      }
    ]
  }],
  "status": "OK"
}

x3 = [
    {"Firstname": "John", "Lastname" : "Smith", "City" : "Boston", "State" : "MA", "Children": [
            {"Name" : "Callie", "Age" : 5},
            {"Name" : "Griffin", "Age" :3},
            {"Name" : "Luke", "Age" : 1}
        ]
    },
    {"Firstname": "Henry", "Lastname" : "Rhodes", "City" : "New York", "State" : "NY", "Children": [
            {"Name" : "Howard", "Age" : 15},
            {"Name" : "Robert", "Age" : 11}
        ]
    },
    {"Firstname": "Allison", "Lastname" : "Berman", "City" : "Los Angeles", "State" : "CA", "Children": [
            {"Name" : "Jeff", "Age" : 35},
            {"Name" : "Roxanne", "Age" :33},
            {"Name" : "Claudia", "Age" : 31},
            {"Name" : "Denzel", "Age" : 11}
        ]
    }
]

x4 = """{
  "squadName": "Super hero squad",
  "homeTown": "Metro City",
  "formed": 2016,
  "secretBase": "Super tower",
  "active": true,
  "members": [
    {
      "name": "Molecule Man",
      "age": 29,
      "secretIdentity": "Dan Jukes",
      "powers": [
        "Radiation resistance",
        "Turning tiny",
        "Radiation blast"
      ]
    },
    {
      "name": "Madame Uppercut",
      "age": 39,
      "secretIdentity": "Jane Wilson",
      "powers": [
        "Million tonne punch",
        "Damage resistance",
        "Superhuman reflexes"
      ]
    },
    {
      "name": "Eternal Flame",
      "age": 1000000,
      "secretIdentity": "Unknown",
      "powers": [
        "Immortality",
        "Heat Immunity",
        "Inferno",
        "Teleportation",
        "Interdimensional travel"
      ]
    }
  ]
}"""
