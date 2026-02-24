output "cluster_name" {
  description = "Name of the GKE cluster"
  value       = google_container_cluster.primary.name
}

output "cluster_id" {
  description = "ID of the GKE cluster"
  value       = google_container_cluster.primary.id
}

output "cluster_endpoint" {
  description = "Endpoint of the GKE cluster"
  value       = google_container_cluster.primary.endpoint
  sensitive   = true
}

output "cluster_ca_certificate" {
  description = "Public certificate authority of the cluster"
  value       = google_container_cluster.primary.master_auth[0].cluster_ca_certificate
  sensitive   = true
}

output "cluster_location" {
  description = "Location of the GKE cluster"
  value       = google_container_cluster.primary.location
}

output "cluster_region" {
  description = "Region of the GKE cluster"
  value       = var.region
}

output "node_pool_name" {
  description = "Name of the primary node pool"
  value       = google_container_node_pool.primary_nodes.name
}

output "node_pool_id" {
  description = "ID of the primary node pool"
  value       = google_container_node_pool.primary_nodes.id
}

output "service_account_email" {
  description = "Email of the service account used by GKE nodes"
  value       = google_service_account.gke_nodes.email
}

output "service_account_name" {
  description = "Name of the service account used by GKE nodes"
  value       = google_service_account.gke_nodes.name
}

output "kubectl_config_command" {
  description = "Command to configure kubectl"
  value       = "gcloud container clusters get-credentials ${google_container_cluster.primary.name} --region ${var.region} --project ${var.project_id}"
}

output "cluster_master_version" {
  description = "The Kubernetes master version"
  value       = google_container_cluster.primary.master_version
}

output "network" {
  description = "The network the cluster is running on"
  value       = google_container_cluster.primary.network
}

output "subnetwork" {
  description = "The subnetwork the cluster is running on"
  value       = google_container_cluster.primary.subnetwork
}
