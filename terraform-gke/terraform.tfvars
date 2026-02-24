# GCP Project Configuration
project_id = "project-69f6f6fe-42ac-4d0e-8cd"  # Replace with your GCP project ID

# Cluster Configuration
cluster_name        = "gke-app-cluster"
region              = "us-central1"
zones               = ["us-central1-a", "us-central1-b"]  # Limit to 2 zones to reduce quota usage
deletion_protection = false  # Set to true for production

# Service Account
gke_service_account_name = "gke-node-sa"

# Node Pool Configuration
node_pool_name   = "primary-node-pool"
node_count       = 2
machine_type     = "e2-medium"
disk_size_gb     = 50
disk_type        = "pd-standard"
preemptible_nodes = true  # Set to true for cost savings (not recommended for production)

# Autoscaling (currently disabled - set enable_autoscaling to true to enable)
enable_autoscaling = false
min_node_count     = 1
max_node_count     = 3

# Cluster Features
enable_logging             = true
enable_monitoring          = true
enable_network_policy      = true  # Enable Calico network policy for better security
enable_http_load_balancing = false

# Maintenance Window
maintenance_start_time = "03:00"  # 3 AM

# Labels for the cluster (Add your custom labels)
cluster_labels = {
  environment = "development"
  managed-by  = "terraform"
  purpose     = "app-deployment-practice"
}

# Labels for nodes (Add your custom labels)
node_labels = {
  environment = "development"
  node-type   = "application"
}

# Network tags for nodes (Add your custom tags)
node_tags = [
  "gke-node",
  "app-cluster"
]
