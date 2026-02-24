# GKE Cluster Terraform Configuration

This Terraform configuration creates a Google Kubernetes Engine (GKE) standard cluster for practicing application deployments.

## Architecture Overview

- **Cluster Type**: Standard GKE cluster (not Autopilot)
- **Network**: Default VPC
- **Region**: us-central1
- **Node Pool**: 2 x e2-medium nodes
- **Service Account**: Dedicated SA for GKE nodes with appropriate IAM roles
- **Features**: Cloud Logging and Monitoring enabled

## Prerequisites

1. **GCP Account**: Active Google Cloud Platform account
2. **GCP Project**: A GCP project with billing enabled
3. **gcloud CLI**: Installed and configured
   ```bash
   gcloud auth login
   gcloud config set project YOUR_PROJECT_ID
   ```
4. **Terraform**: Version >= 1.0 installed
   ```bash
   terraform version
   ```
5. **Required APIs**: Enable the following APIs in your GCP project:
   ```bash
   gcloud services enable container.googleapis.com
   gcloud services enable compute.googleapis.com
   gcloud services enable iam.googleapis.com
   ```

## Configuration Files

- **main.tf**: Main Terraform configuration with GKE cluster, node pool, and service account
- **variables.tf**: Variable definitions
- **outputs.tf**: Output values after deployment
- **terraform.tfvars**: Variable values (customize this file)

## Setup Instructions

### 1. Update terraform.tfvars

Edit `terraform.tfvars` and replace `YOUR_PROJECT_ID_HERE` with your actual GCP project ID:

```hcl
project_id = "your-actual-project-id"
```

You can also customize other values like:
- Cluster name
- Node count
- Machine type
- Labels and tags

### 2. Initialize Terraform

```bash
terraform init
```

### 3. Review the Plan

```bash
terraform plan
```

This will show you what resources will be created.

### 4. Apply the Configuration

```bash
terraform apply
```

Type `yes` when prompted to confirm.

### 5. Configure kubectl

After the cluster is created, configure kubectl to connect to your cluster:

```bash
gcloud container clusters get-credentials gke-app-cluster --region us-central1 --project YOUR_PROJECT_ID
```

Or use the command from Terraform output:
```bash
terraform output kubectl_config_command
```

### 6. Verify the Cluster

```bash
kubectl get nodes
kubectl cluster-info
kubectl get namespaces
```

## Features and Configuration

### Service Account
- A dedicated service account is created for GKE nodes
- Includes necessary IAM roles for logging, monitoring, and storage

### Node Pool Configuration
- **Default**: 2 nodes
- **Machine Type**: e2-medium (2 vCPU, 4GB RAM)
- **Disk**: 50GB standard persistent disk
- **Auto-repair**: Enabled
- **Auto-upgrade**: Enabled

### Optional Features

#### Enable Autoscaling
In `terraform.tfvars`, set:
```hcl
enable_autoscaling = true
min_node_count     = 1
max_node_count     = 5
```

#### Use Preemptible Nodes (Cost Savings)
In `terraform.tfvars`, set:
```hcl
preemptible_nodes = true
```
⚠️ Note: Preemptible nodes can be terminated at any time. Use for dev/test only.

#### Enable Network Policy
In `terraform.tfvars`, set:
```hcl
enable_network_policy = true
```

#### Enable HTTP Load Balancing
In `terraform.tfvars`, set:
```hcl
enable_http_load_balancing = true
```

## Outputs

After applying, you can view outputs:

```bash
terraform output
```

Key outputs include:
- `cluster_name`: Name of the cluster
- `cluster_endpoint`: Cluster API endpoint
- `service_account_email`: Email of the node service account
- `kubectl_config_command`: Command to configure kubectl

## Cost Estimation

Approximate monthly cost (us-central1):
- **2 x e2-medium nodes**: ~$50-60/month
- **Cluster management**: Free (no cluster management fee for standard clusters)
- **Storage & networking**: Variable based on usage

💡 **Cost Optimization Tips**:
- Use preemptible nodes for dev/test environments
- Enable autoscaling to scale down during off-hours
- Delete the cluster when not in use: `terraform destroy`

## Cleanup

To destroy all resources and avoid charges:

```bash
terraform destroy
```

Type `yes` when prompted to confirm.

## Troubleshooting

### Issue: APIs not enabled
```
Error: Error creating service account: googleapi: Error 403
```
**Solution**: Enable required APIs:
```bash
gcloud services enable container.googleapis.com compute.googleapis.com iam.googleapis.com
```

### Issue: Insufficient permissions
```
Error: Error creating cluster: Permission denied
```
**Solution**: Ensure your GCP account has the following roles:
- Kubernetes Engine Admin
- Service Account Admin
- Compute Admin

### Issue: Quota exceeded
```
Error: Quota 'CPUS' exceeded
```
**Solution**: Request quota increase in GCP Console or use smaller machine types/fewer nodes.

## Next Steps

After creating the cluster, you can:

1. **Deploy sample applications**:
   ```bash
   kubectl create deployment nginx --image=nginx
   kubectl expose deployment nginx --port=80 --type=LoadBalancer
   ```

2. **Install Helm** (Kubernetes package manager):
   ```bash
   curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
   ```

3. **Deploy monitoring tools** (Prometheus, Grafana)
4. **Practice CI/CD** with Cloud Build or GitHub Actions
5. **Explore GKE features** like Workload Identity, Config Connector, etc.

## References

- [GKE Documentation](https://cloud.google.com/kubernetes-engine/docs)
- [Terraform GKE Module](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/container_cluster)
- [Kubernetes Documentation](https://kubernetes.io/docs/)

## License

This configuration is provided as-is for educational and practice purposes.
