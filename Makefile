# Don't fear the Makefile

.PHONY: helloapi


helloapi:
	ijhttp -e aidev -p ./http-client.private.env.json ./hello_api/helloapi.http
