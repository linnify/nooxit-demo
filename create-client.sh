#!/usr/bin/env bash

docker exec --detach -it --entrypoint=/bin/bash hydra "hydra clients create -n \"Linnify App\" --endpoint http://hydra:4445 --id linnify-app --secret LinnifySecret --grant-types authorization_code --response-types code --scope openid,email,username,groups,offline_access --token-endpoint-auth-method client_secret_basic --callbacks \"http://127.0.0.1:8000/auth/callback,http://127.0.0.1:8000/docs/oauth2-redirect\""
