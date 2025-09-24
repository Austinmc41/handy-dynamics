terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "7.4.0"
    }
  }
}

provider "google" {
  # Configuration options
  project = var.project
  region  = var.region
}

resource "google_sql_database" "database" {
  name     = var.google_sql_db_name
  instance = google_sql_database_instance.instance.name
}

# See versions at https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance#database_version
resource "google_sql_database_instance" "instance" {
  name             = var.db_instance_name
  region           = var.region
  database_version = var.db_instance_version
  settings {
    tier = var.db_instance_tier
    edition = "ENTERPRISE"
  }

  deletion_protection = false
}

