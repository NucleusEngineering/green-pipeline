#! /bin/bash

# determine which node port the service was exposed on
get_nodeport() {
    kubectl get service stocksim-svc --namespace=test-$SHORT_SHA -o=jsonpath='{.spec.ports[0].targetPort}' 
}

until [[ -n "$(get_nodeport)" ]]; do
    echo "querying for nodeport"
    sleep 3
done

echo "$(get_nodeport)" > _nodeport # save port for use in next step

# grab the IP of the load balancer
get_nodeip() {
    kubectl get service stocksim-svc --namespace=test-$SHORT_SHA --output jsonpath='{.status.loadBalancer.ingress[0].ip}'
}

until [[ -n "$(get_nodeip)" ]]; do
    echo "querying for nodeip"
    sleep 3
done

echo $(get_nodeip) > _nodeip # save ip for use in next step