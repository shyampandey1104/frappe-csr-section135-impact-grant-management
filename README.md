# Frappe Companies Act Sec 135 Mandatory 2% CSR & NGO Grant Management Engine

[![Frappe Framework](https://img.shields.io/badge/Frappe-v15.x-blue.svg)](https://frappeframework.com/)
[![Companies Act 2013](https://img.shields.io/badge/MCA-Section%20135%20CSR-purple.svg)]()
[![ESG Governance](https://img.shields.io/badge/ESG-Schedule%20VII%20Grants-teal.svg)]()
[![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen.svg)]()
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## 📌 Executive Overview & Real-World Client Problem

Under Section 135 of the Indian **Companies Act, 2013** and CSR Rules 2021:
1. Companies meeting statutory financial thresholds (Net Worth $\ge$ ₹500 Cr, Turnover $\ge$ ₹1,000 Cr, or Net Profit $\ge$ ₹5 Cr) must mandatorily spend **at least 2% of their average net profits** of the preceding 3 financial years on Schedule VII CSR activities.
2. **Unspent CSR Fund Penalties:** Any unspent CSR funds related to an ongoing project must be transferred to a special **Unspent CSR Bank Account** within 30 days of fiscal close, or to a Fund specified in Schedule VII (e.g. PMNRF) within 6 months. Failure exposes company directors to severe fines and criminal liability.
3. **NGO Due Diligence & MCA CSR-1 Validation:** Disbursing grants to implementing NGOs lacking a valid MCA Registration Number (Form CSR-1) or failing to verify milestone Utilization Certificates (UC) is an audit violation.

This Frappe application automates statutory 2% CSR budget calculations, NGO due diligence, milestone tranche disbursements, and MCA Annual CSR Report exports.

---

## 🏛️ System Architecture Flow

```mermaid
flowchart TD
    A["ERPNext Audited P&L Statements (Preceding 3 Years)"] -->|Calculate 3-Year Average Net Profit| B["Statutory 2% CSR Budget Calculator"]
    B -->|Mandatory CSR Allocation Target| C["CSR Committee Governance Board"]
    D["NGO Grant Application (Schedule VII Project)"] -->|Validate MCA Form CSR-1 Reg No| E{"NGO Due Diligence Pass?"}
    E -->|No| F["Reject Grant: Non-Compliant NGO"]
    E -->|Yes| G["Create Milestone Tranche Agreement"]
    G -->|Tranche 1 Disbursement| H["Bank Grant Transfer"]
    H -->|Receive Milestone Utilization Certificate (UC)| I["Verify UC & Impact Deliverables"]
    I -->|Release Subsequent Tranche| J["Statutory CSR Budget Fulfillment Tracking"]
    J -->|Unspent Amount Forecaster| K["Export MCA Annual CSR Board Report"]
```

---

## 🚀 Key Engineering Capabilities

- **Automated Statutory 2% Budget Computation:** Evaluates 3-year P&L financials and computes exact CSR liability under Section 135(5).
- **MCA Form CSR-1 Verification:** Enforces mandatory registration validation before any grant commitment can be approved.
- **Milestone-Based Tranche Disbursements:** Locks subsequent grant payments until audited Utilization Certificates (UC) are approved.
- **Unspent CSR Escrow Countdown:** Proactively alerts CFOs and CSR committees of impending statutory transfer deadlines.

---

## 📂 Frappe DocType Schema & Data Structure

```text
csr_section135_grant/
├── csr_section135_grant_core/
│   ├── doctype/
│   │   ├── csr_statutory_budget/
│   │   │   ├── csr_statutory_budget.json
│   │   │   ├── csr_statutory_budget.py
│   │   │   └── csr_statutory_budget.js
│   │   └── csr_grant_tranche/
│   │       └── csr_grant_tranche.json
│   └── workspace/
│       └── csr_section135_grant_workspace/
│           └── csr_section135_grant_workspace.json
```

---

## ⚡ Frappe Hooks & Whitelisted APIs

- **REST Endpoint:** `POST /api/method/csr_section135_grant.api.allocate_grant_tranche`
- **Whitelisted Method:** `@frappe.whitelist() def disburse_tranche_with_uc(tranche_id, disbursement_amount, uc_verified)`
- **Hooks Event:** `on_submit` of `Payment Entry` (CSR Grant) marks milestone fund utilization.

---

## 🛠️ Installation & Bench Setup

```bash
bench get-app https://github.com/shyampandey1104/frappe-csr-section135-impact-grant-management
bench --site erp.yourdomain.com install-app csr_section135_grant
bench --site erp.yourdomain.com migrate
python3 -m unittest discover tests
```

---

## 📄 License
MIT License. Built for Public Limited Companies, Corporate Foundations, and ESG Boards.
