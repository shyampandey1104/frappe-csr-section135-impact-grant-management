# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "csr_section135_grant"
app_title = "Frappe Csr Section135 Impact Grant Management"
app_publisher = "Shyamkumar Pandey"
app_description = "Frappe Csr Section135 Impact Grant Management - Enterprise Multi-DocType Solution for Frappe & ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/csr_section135_grant/css/csr_section135_grant.bundle.css"
app_include_js = "/assets/csr_section135_grant/js/csr_section135_grant.bundle.js"

# Document Events
# ---------------
doc_events = {
    "Frappe Csr Section135 Impact Grant Management Entry": {
        "validate": "csr_section135_grant.services.validator.EnterpriseValidationEngine.validate_compliance_rules",
        "on_submit": "csr_section135_grant.services.integration_service.EnterpriseIntegrationService.verify_remote_status"
    }
}

# Scheduled Background Tasks
# --------------------------
scheduler_events = {
    "hourly": [
        "csr_section135_grant.tasks.hourly_sync"
    ],
    "daily": [
        "csr_section135_grant.tasks.daily_reconciliation"
    ],
    "weekly": [
        "csr_section135_grant.tasks.weekly_digest"
    ]
}
