#! /bin/bash

curl -X GET -G http://$(cat _nodeip):$(cat _nodeport) -d stock=GOOG
curl -X GET -G http://$(cat _nodeip):$(cat _nodeport) -d stock=AAPL

curl -X GET -G http://$(cat _nodeip):$(cat _nodeport) -d stock=GOOG -d iterations=5000000
curl -X GET -G http://$(cat _nodeip):$(cat _nodeport) -d stock=AAPL -d iterations=5000000

curl -X GET -G http://$(cat _nodeip):$(cat _nodeport) -d stock=GOOG -d iterations=10000000
curl -X GET -G http://$(cat _nodeip):$(cat _nodeport) -d stock=AAPL -d iterations=10000000

curl -X GET -G http://$(cat _nodeip):$(cat _nodeport) -d stock=GOOG -d iterations=100000000
curl -X GET -G http://$(cat _nodeip):$(cat _nodeport) -d stock=AAPL -d iterations=100000000

