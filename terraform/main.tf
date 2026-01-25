terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "7.16.0"
    }
  }
}

provider "google" {
  credentials = "/Users/alberto/keyGPA.json"
  project     = "voltaic-talent-485417-p2"
  region      = "us-central1"
}

resource "google_storage_bucket" "demo-bucket-de-workshop" {
  name          = "demo-bucket-de-workshop-123456"
  location      = "US"
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}