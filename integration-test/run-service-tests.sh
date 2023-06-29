#! /bin/bash

curl -X GET -G http://$(cat _nodeip):$(cat _nodeport) -d stock=GOOG -d iterations=100
curl -X GET -G http://$(cat _nodeip):$(cat _nodeport) -d stock=AAPL -d iterations=100

curl -X GET -G http://$(cat _nodeip):$(cat _nodeport) -d stock=GOOG -d iterations=1000
curl -X GET -G http://$(cat _nodeip):$(cat _nodeport) -d stock=AAPL -d iterations=1000

curl -X GET -G http://$(cat _nodeip):$(cat _nodeport) -d stock=GOOG -d iterations=10000
curl -X GET -G http://$(cat _nodeip):$(cat _nodeport) -d stock=AAPL -d iterations=10000

curl -X GET -G http://$(cat _nodeip):$(cat _nodeport) -d stock=GOOG -d iterations=100000
curl -X GET -G http://$(cat _nodeip):$(cat _nodeport) -d stock=AAPL -d iterations=100000

