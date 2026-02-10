terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "7.18.0"
    }
  }
}

provider "google" {
  project = "de-zoomcamp-project-486915"
  region  = "europe-west2"
}

resource "google_storage_bucket" "demo-bucket" {
  name          = "de-zoomcamp-project-486915-terra-bucket"
  location      = "EU"
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