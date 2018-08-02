#!/bin/bash

if [ $1 != "production" ] ;
then
  echo env must be production
  exit
fi

ecr_login="$(aws ecr get-login)"
str_to_rm=" -e none"
eval "$(echo "$ecr_login" | sed "s@$str_to_rm@@")"

docker build -t crp-website:$1 .;
docker tag crp-website:$1 832531170141.dkr.ecr.us-east-2.amazonaws.com/crp-website:$1;

docker push 832531170141.dkr.ecr.us-east-2.amazonaws.com/crp-website:$1;

~/src/ecs-deploy/./ecs-deploy -c bep-projects -n crp-website -i 832531170141.dkr.ecr.us-east-2.amazonaws.com/crp-website:$1;
