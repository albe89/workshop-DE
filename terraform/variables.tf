
variable "project" {
  description = "The project ID to create resources in."
  default     = "voltaic-talent-485417-p2"

}

variable "credentials" {
  description = "The service account key file."
  default     = "/Users/alberto/keyGPA.json"

}

variable "region" {
  description = "The region of the BigQuery dataset to create."
  default     = "us-central1"

}
variable "location" {
  description = "The location of the BigQuery dataset to create."
  default     = "US"

}

variable "bq_data_set_name" {
  description = "The name of the BigQuery dataset to create."
  default     = "demo_dataset"

}

variable "gsc_bucket_name" {
  description = "The name of the GCS bucket to create."
  default     = "demo-bucket-de-workshop-123456"

}

variable "gcs_storage_class" {
  description = "The storage class of the GCS bucket."
  default     = "STANDARD"

}