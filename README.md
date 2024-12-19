# Testing the App with Token :
You can test your webhook using curl with the correct token:

``` bash
curl -X POST http://localhost:5000/webhook \
-H "Authorization: Bearer your-secret-token" \
-H "Content-Type: application/json" \
-d '{"key": "value"}'
```


# Testing the app with api key :

``` bash
curl -X POST http://localhost:5000/webhook \
-H "X-API-Key: your-api-key" \
-H "Content-Type: application/json" \
-d '{"key": "value"}'
```

# Testing the app with jwt :

Generate Token:

You can generate a token for testing using the create_token function.

Usage:

``` bash
curl -X POST http://localhost:5000/webhook \
-H "Authorization: Bearer <generated-token>" \
-H "Content-Type: application/json" \
-d '{"key": "value"}'
``` 
