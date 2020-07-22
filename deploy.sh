#!/bin/bash

make -C Frontend
docker build -t cempassi/vimeo-app-backend ./Backend 
docker build -t cempassi/vimeo-app-frontend ./Frontend 
docker push cempassi/vimeo-app-frontend
docker push cempassi/vimeo-app-backend
ssh root@'178.62.83.69' 'cd site_hugo; ./refresh.sh'
