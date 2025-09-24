variable "project" {
  description = "Project"
  default     = "handy-bot"
}

variable "region" {
  description = "Region"
  default     = "us-east1"
}

variable "google_sql_db_name" {
  description = "My Google Cloud SQL DB Name"
  default     = "handy-bot-db"
}

variable "db_instance_name" {
  description = "My DB Instance Name"
  default     = "my-database-instance"
}

variable "db_instance_version" {
  description = "My DB Instance Version"
  default     = "POSTGRES_17"
}

variable "db_instance_tier" {
  description = "My DB Instance Machine Tier"
  default     = "db-f1-micro"
}

