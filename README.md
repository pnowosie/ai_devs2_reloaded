# ai_devs2_reloaded

Repo for the course https://www.aidevs.pl


## Prerequisites

- InteliJ Http Client plugin and `ijhttp` CLI client
- Python / Bun (will see)


## Getting started

### 1. Credentials

Open `http-client.example.json` & fill in specified values, next save a file as: `http-client.private.env.json`


### 2. Run hello api initial task

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
