# Don't fear the Makefile

.PHONY: helloapi


helloapi:
	ijhttp -e aidev -v ./http-client.env.json -p ./http-client.private.env.json ./hello_api/helloapi.http
