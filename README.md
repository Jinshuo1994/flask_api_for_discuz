# Flask *restful* api for *discuz*

Thia project aims to add api for *discuz* using Flask. Finally, a whole brand new forum based on **Flask** will be built.

## Getting Started

APIs have already been implemented  
(full tests including boundary test in a separate section below)
1. log in with username and password  
(To ensure the stateless, token is used and sent to server from client every request. Details can be found
in my personal blog)
sample http request: `127.0.0.1:5000/login`params:`username=zhang&password=password` method:`POST`
sample response: 
```json
{
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InpoYW5nIiwiZXhwIjoxNTIzODU4MzAxfQ.icLDp0PTKjBaQ_njJQ7aqB2OvVuj5ytDw6yOZMMcXv0"
}
```

2. register with username, password, email
sample http request: `127.0.0.1:5000/register`params`username=zhang&password=password1&&email=testemail@gmail.com` method:`POST`

sample response:
```json
{
    "message": "zhang is registered successfully. You can use it to sign up now."
}
```

3. get user profiles
sample http request: `127.0.0.1:5000/profile`header`x-access-token:eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InpoYW5nIiwiZXhwIjoxNTIzODU5NTM3fQ.BBeUvz8Bh4jP2V7B65Nt-iX9fft_CRecB9jSgDK4Vms`   
method:`GET`

sample response:
```json
{
    "profile": {
        "gender": 1,
        "realname": "test_real_name",
        "username": "zhang"
    }
}
```

4. get user messages
sample http request: `127.0.0.1:5000/messages`header`x-access-token:eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InpoYW5nIiwiZXhwIjoxNTIzODU5NTM3fQ.BBeUvz8Bh4jP2V7B65Nt-iX9fft_CRecB9jSgDK4Vms`   
method:`GET`

sample response:
```json
{
    "messages for zhang": [
        {
            "content": "你好, Zhang 很高兴认识你",
            "dataline": "2018-04-16T01:57:05",
            "uid": 29,
            "username": "Nick"
        },
        {
            "content": "Hello. I am a graduate student studying at University of Maryland. What about you?",
            "dataline": "2018-04-16T01:58:54",
            "uid": 28,
            "username": "zhang"
        },
        {
            "content": "I am a freshman",
            "dataline": "2018-04-16T01:59:34",
            "uid": 29,
            "username": "Nick"
        },
        {
            "content": "你好, Zhang 很高兴认识你",
            "dataline": "2018-04-16T01:57:05",
            "uid": 29,
            "username": "Nick"
        },
        {
            "content": "Hello. I am a graduate student studying at University of Maryland. What about you?",
            "dataline": "2018-04-16T01:58:54",
            "uid": 28,
            "username": "zhang"
        },
        {
            "content": "I am a freshman",
            "dataline": "2018-04-16T01:59:34",
            "uid": 29,
            "username": "Nick"
        }
    ]
}
```

5. get posts by forum id  
(Since the default forum id is 2. This forum is used for test. Assume "log in" is required before access the forum)
sample http request: `127.0.0.1:5000/forum/2`header`x-access-token:eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InpoYW5nIiwiZXhwIjoxNTIzODU5NTM3fQ.BBeUvz8Bh4jP2V7B65Nt-iX9fft_CRecB9jSgDK4Vms`   
method:`GET`

sample response:
```json
{
            "author": "zhang",
            "authorid": 28,
            "message": "Hello everyone. I am happy to be here.",
            "subject": "my first post",
            "timeline": "2018-04-16T01:56:50",
            "useip": "192.168.232.1"
        },
        {
            "author": "zhang",
            "authorid": 28,
            "message": "[i=s] 本帖最后由 zhang 于 2018-4-16 14:07 编辑 [/i]\n\nHello, I am a [font=Arial]new graduate[/font] and seeking a roommate.\r\n",
            "subject": "find roommate",
            "timeline": "2018-04-16T02:06:07",
            "useip": "192.168.232.1"
        },
        {
            "author": "Nick",
            "authorid": 29,
            "message": "Is there anyone who wants to make up a team for the project?\r\n",
            "subject": "Partner",
            "timeline": "2018-04-16T02:10:12",
            "useip": "192.168.232.1"
        }
}
```

6. log out
sample http request: `127.0.0.1:5000/logout`header`x-access-token:eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InpoYW5nIiwiZXhwIjoxNTIzODU5NTM3fQ.BBeUvz8Bh4jP2V7B65Nt-iX9fft_CRecB9jSgDK4Vms`   
method:`POST`

sample response:
```json
{
    "message": "Log out successfully! Your token has expired"
}
```


### Installing
* Customize the database configuration  
Change `SQLALCHEMY_DATABASE_URI` in `config.py` to the real database uri.
* Install dependent packages:
```
pip install -r requirements.txt
```
* Start the Server (at 5000 port in default. How to change the port and permit external web access is detailed in blog)
```
python api.py
```

## Advanced Topics
### migrate the database  
Details are in my blog.
```
python manage.py db init    #do this only when Flask-migrate has not been initiated.
python manage.py db migrate
python manage.py db upgrade

```

## Tests
See in my personal [blog][1]

## Versioning

*v1.0.0*

## Authors

* **Jinshuo** - *Initial work*  
About me: I am a first year graduate student eagerly seeking summer intership for 2018 and *Software Develop* posisiton job for 2019.  

## Development Details
See details at my personal [blog][1]
(I am working on building up this tech blog)

[1]: https://jinshuo1994.github.io/



