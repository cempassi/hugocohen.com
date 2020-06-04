#!/bin/bash

make -C Frontend
docker build -t cempassi/vimeo-app-backend ./Backend 
docker build -t cempassi/vimeo-app-frontend ./Frontend 
docker push cempassi/vimeo-app-frontend
docker push cempassi/vimeo-app-backend
