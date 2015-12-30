For api overview and usages, check out [this page](overview.md).

## GET ```/api/events/ ```

Gives the list of all the events.

```Status Code : 200 OK ```

```
{
    "links": {
        "first": "http://127.0.0.1:8000/api/events/?page=1",
        "last": "http://127.0.0.1:8000/api/events/?page=1",
        "next": null,
        "prev": null
    },
    "data": {
        "links": {
            "first": "http://127.0.0.1:8000/api/events/?page=1",
            "last": "http://127.0.0.1:8000/api/events/?page=1",
            "next": null,
            "prev": null
        },
        "meta": {
            "pagination": {
                "page": 1,
                "pages": 1,
                "count": 2
            }
        },
        "results": [
            {
                "name_of_the_event": "Tokens Of Love",
                "photo_of_the_area": null,
                "description_of_the_event": "Aisi",
                "location": "",
                "name_of_the_contact_person": "Preksha/Deepanjali",
                "phone_number_of_the_contact_person": "120938012"
            },
            {
                "name_of_the_event": "Test Event",
                "photo_of_the_area": null,
                "description_of_the_event": "sasdf",
                "location": "asdfsda",
                "name_of_the_contact_person": "asdfasd",
                "phone_number_of_the_contact_person": "asdfasdf"
            }
        ]
    },
    "meta": {
        "pagination": {
            "page": 1,
            "pages": 1,
            "count": 2
        }
    }
}
```

## GET ``` /api/notification/```

Gives the list of the notification w.r.t to events.

```Status Code : 200 OK ```

```{
    "links": {
        "first": "http://127.0.0.1:8000/api/notification/?page=1",
        "last": "http://127.0.0.1:8000/api/notification/?page=1",
        "next": null,
        "prev": null
    },
    "data": {
        "links": {
            "first": "http://127.0.0.1:8000/api/notification/?page=1",
            "last": "http://127.0.0.1:8000/api/notification/?page=1",
            "next": null,
            "prev": null
        },
        "meta": {
            "pagination": {
                "page": 1,
                "pages": 1,
                "count": 3
            }
        },
        "results": [
            {
                "event": {
                    "name_of_the_event": "Test Event",
                    "photo_of_the_area": null,
                    "description_of_the_event": "sasdf",
                    "location": "asdfsda",
                    "name_of_the_contact_person": "asdfasd",
                    "phone_number_of_the_contact_person": "asdfasdf"
                },
                "notification_text": "sadasd"
            },
            {
                "event": {
                    "name_of_the_event": "Tokens Of Love",
                    "photo_of_the_area": null,
                    "description_of_the_event": "Aisi",
                    "location": "Preksha",
                    "name_of_the_contact_person": "Preksha/Deepanjali",
                    "phone_number_of_the_contact_person": "120938012"
                },
                "notification_text": "Huuray"
            },
            {
                "event": {
                    "name_of_the_event": "Tokens Of Love",
                    "photo_of_the_area": null,
                    "description_of_the_event": "Aisi",
                    "location": "Preksha",
                    "name_of_the_contact_person": "Preksha/Deepanjali",
                    "phone_number_of_the_contact_person": "120938012"
                },
                "notification_text": "sdasdasd"
            }
        ]
    },
    "meta": {
        "pagination": {
            "page": 1,
            "pages": 1,
            "count": 3
        }
    }
}
```

