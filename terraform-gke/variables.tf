variable "project_id" {
  description = "The GCP project ID"
  type        = string
}

variable "region" {
  description = "The GCP region for the GKE cluster"
  type        = string
  default     = "us-central1"
}

variable "zones" {
  description = "List of zones within the region where nodes will be created"
  type        = list(string)
  default     = ["us-central1-a", "us-central1-b"]
}

variable "cluster_name" {
  description = "Name of the GKE cluster"
  type        = string
  default     = "gke-cluster"
}

variable "deletion_protection" {
  description = "Whether to enable deletion protection on the cluster"
  type        = bool
  default     = false
}

# Service Account Variables
variable "gke_service_account_name" {
  description = "Name of the service account for GKE nodes"
  type        = string
  default     = "gke-node-sa"
}

# Node Pool Variables
variable "node_pool_name" {
  description = "Name of the node pool"
  type        = string
  default     = "primary-node-pool"
}

variable "node_count" {
  description = "Number of nodes in the node pool"
  type        = number
  default     = 2
}

variable "machine_type" {
  description = "Machine type for the nodes"
  type        = string
  default     = "e2-medium"
}

variable "disk_size_gb" {
  description = "Disk size in GB for each node"
  type        = number
  default     = 50
}

variable "disk_type" {
  description = "Disk type for each node (pd-standard or pd-ssd)"
  type        = string
  default     = "pd-standard"
}

variable "preemptible_nodes" {
  description = "Whether to use preemptible nodes (cheaper but can be terminated)"
  type        = bool
  default     = false
}

# Autoscaling Variables
variable "enable_autoscaling" {
  description = "Enable autoscaling for the node pool"
  type        = bool
  default     = false
}

variable "min_node_count" {
  description = "Minimum number of nodes for autoscaling"
  type        = number
  default     = 1
}

variable "max_node_count" {
  description = "Maximum number of nodes for autoscaling"
  type        = number
  default     = 3
}

# Cluster Features
variable "enable_logging" {
  description = "Enable Cloud Logging"
  type        = bool
  default     = true
}

variable "enable_monitoring" {
  description = "Enable Cloud Monitoring"
  type        = bool
  default     = true
}

variable "enable_network_policy" {
  description = "Enable network policy (Calico)"
  type        = bool
  default     = true
}

variable "enable_http_load_balancing" {
  description = "Enable HTTP Load Balancing addon"
  type        = bool
  default     = false
}

# Maintenance Window
variable "maintenance_start_time" {
  description = "Start time for daily maintenance window (HH:MM format)"
  type        = string
  default     = "03:00"
}

# Labels and Tags
variable "cluster_labels" {
  description = "Labels to apply to the cluster"
  type        = map(string)
  default     = {}
}

variable "node_labels" {
  description = "Labels to apply to the nodes"
  type        = map(string)
  default     = {}
}

variable "node_tags" {
  description = "Network tags to apply to the nodes"
  type        = list(string)
  default     = []
}
