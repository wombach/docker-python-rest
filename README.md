# docker-python-rest

This is a set of APIs for different services.

## Run standalone
Make sure you have python 3.x installed and install dependancies
```
pip install pipenv
pipenv install --system --skip-lock
```

Define variables in config.json, or as environment variables:
```
cat <<EOT >> config.json
{
    "ES_URL": "https://test.westeurope.azure.elastic-cloud.com:9243/",
    "ES_INDEX": "testindex"
}
EOT
```

Run the app
```
pipenv run python app.py
```
## Building / Running in docker
Create a new version of the container
```
make build
```

Run the container
```
make run
```

Stop the container
```
make kill
```

Run container with development vars
```
docker run --detach -p 8080:8080 --env ES_INDEX="testindex" --env ES_URL="https://test.westeurope.azure.elastic-cloud.com:9243/" nxtgen-equipment-api
```

management of access token
https://ginnyfahs.medium.com/github-error-authentication-failed-from-command-line-3a545bfd0ca8