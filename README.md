# ai_devs2_reloaded

Repo for the course https://www.aidevs.pl

## Special Thanks

Stolen `AIDevsTasks` code with :heart: love from [SpicySoftware/AIDevsTasks](https://github.com/SpicySoftware/AIDevsTasks)

## Prerequisites

- InteliJ Http Client plugin and `ijhttp` CLI client
- Python >= 3.10, `py` (python launcher) will be handy


## Getting started

### 1. Credentials

Open `http-client.example.json` & fill in specified values, next save a file as: `http-client.private.env.json`

**Install python dependencies:**
```bash
py -3.11 -m venv .venv
py -m pip install -r requirements.txt
```


### 2. Run task with Python framework

```bash
py main.py helloapi
```

It will find, load and execute `helloapi` module from `./tasks` directory.

**Sample output:**
```
╰─ py main.py helloapi 

Trying to import task module: tasks.helloapi
Module 'tasks.helloapi' imported successfully!
=> TASK [200]
{'code': 0,
 'cookie': 'aidevs_9d3129a2',
 'msg': 'please return value of "cookie" field as answer'}

=> ANSWER [200]
{'code': 0, 'msg': 'OK', 'note': 'CORRECT'}

✅       Success: Task( helloapi ) has been resolved
```


### 3. Run hello api task with IJ HTTP Client

```bash
make helloapi
```

**Sample output:**
```
ijhttp -e aidev -p ./http-client.private.env.json ./hello_api/helloapi.http
┌─────────────────────────────────────────────────────────────────────────────┐
│                      Running IntelliJ HTTP Client with                      │
├──────────────────────┬──────────────────────────────────────────────────────┤
│        Files         │ helloapi.http                                        │
├──────────────────────┼──────────────────────────────────────────────────────┤
│  Public Environment  │                                                      │
├──────────────────────┼──────────────────────────────────────────────────────┤
│ Private Environment  │ task-api-url,                                        │
│                      │ task-api-key,                                        │
│                      │ openai-api-key                                       │
└──────────────────────┴──────────────────────────────────────────────────────┘
Request 'Authenticate' POST https:/ ...

...
3 requests completed, 0 have failed tests
RUN SUCCESSFUL
```
