# green-pipeline
Green Pipeline



```
gcloud beta container --project "greenops-demo-env" clusters create "greenops-cluster" --zone "europe-north1-b" --no-enable-basic-auth --cluster-version "1.25.8-gke.1000" --release-channel "regular" --machine-type "e2-small" --image-type "COS_CONTAINERD" --disk-type "pd-balanced" --disk-size "100" --metadata disable-legacy-endpoints=true --scopes "https://www.googleapis.com/auth/devstorage.read_only","https://www.googleapis.com/auth/logging.write","https://www.googleapis.com/auth/monitoring","https://www.googleapis.com/auth/servicecontrol","https://www.googleapis.com/auth/service.management.readonly","https://www.googleapis.com/auth/trace.appenyd" --num-nodes "3" --logging=SYSTEM,WORKLOAD --monitoring=SYSTEM --enable-ip-alias --network "projects/greenops-demo-env/global/networks/k8s-vpc" --subnetwork "projects/greenops-demo-env/regions/europe-north1/subnetworks/k8s-subnet" --no-enable-intra-node-visibility --default-max-pods-per-node "110" --security-posture=standard --workload-vulnerability-scanning=disabled --no-enable-master-authorized-networks --addons HorizontalPodAutoscaling,HttpLoadBalancing,GcePersistentDiskCsiDriver --enable-autoupgrade --enable-autorepair --max-surge-upgrade 1 --max-unavailable-upgrade 0 --no-enable-managed-prometheus --resource-usage-bigquery-dataset "greenpipeline_metering" --enable-network-egress-metering --enable-resource-consumption-metering --enable-shielded-nodes --node-locations "europe-north1-b"
```

``` 
kubectl delete namespaces -l testonly=true
```