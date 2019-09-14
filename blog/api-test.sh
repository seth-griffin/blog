#!/usr/bin/env bash

curl -i -X POST -H "Content-Type:application/json" http://localhost:3000/api/v1/article -d '{"title":"Programming in NodeJS", "published": true, "category":"Node","body":"This is a non-comprehensive introduction to coding in NodeJS using the MEAN stack", "author": "Seth Griffin", "postedOn": "05/22/2018", "updatedOn": "05/22/2018"}'

Update Article 

curl -i -X PUT -H "Content-Type:application/json" http://localhost:3000/api/v1/article/5b0371ca91e3c77e4394db99 -d '{"title":"Programming in NodeJs","Category":"NodeJS","content":"This is a non-comprehensive introduction to coding in NodeJs using the MEAN stack"}'

Delete Article

curl -v -X DELETE http://localhost:3000/api/v1/article/5b0378feae3e0c01d2d95059

Create Category

curl -i -X POST -H "Content-Type:application/json" http://localhost:3000/api/v1/category -d '{"name":"Node", "Description": "Articles about NodeJS"}'

Update Category

curl -i -X PUT -H "Content-Type:application/json" http://localhost:3000/api/v1/category/5b037713ae3e0c01d2d95058 -d '{"name":"NodeJs","Description":"Articles about Node"}'

Delete Category

curl -v -X DELETE http://localhost:3000/api/v1/category/5b037713ae3e0c01d2d95058

curl -i -X POST -H "Content-Type:application/json" http://localhost:3000/api/v1/article -d '{"title":"Programming in NodeJS", "published": true, "category":"Node","body":"This is a non-comprehensive introduction to coding in NodeJS using the MEAN stack", "author": "Seth Griffin", "postedOn": "05/22/2018", "updatedOn": "05/22/2018"}'
