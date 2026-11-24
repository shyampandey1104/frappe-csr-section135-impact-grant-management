"""Companies Act 2013 Section 135 Mandatory 2% CSR & Grant Management Engine."""
from dataclasses import dataclass, field
from datetime import datetime, date
from typing import List, Dict, Any, Optional

@dataclass
class CSRGrantTranche:
    tranche_id: str
    ngo_partner_name: str
    mca_csr1_reg_no: str
    schedule_vii_activity: str  # EDUCATION, HEALTHCARE, RURAL_DEV, ENVIRONMENT
    committed_amount_inr: float
    disbursed_amount_inr: float = 0.0
    utilization_cert_verified: bool = False

class CSRMandatoryComplianceEngine:
    def __init__(self, net_profit_year_1: float, net_profit_year_2: float, net_profit_year_3: float):
        # 2% of average net profits of preceding 3 financial years
        avg_profit = (net_profit_year_1 + net_profit_year_2 + net_profit_year_3) / 3.0
        self.mandatory_csr_budget_inr = round(max(0.0, avg_profit * 0.02), 2)
        self.disbursed_total_inr = 0.0
        self.grants: Dict[str, CSRGrantTranche] = {}

    def allocate_grant_tranche(self, grant: CSRGrantTranche) -> Dict[str, Any]:
        if not grant.mca_csr1_reg_no:
            raise ValueError("NGO must have a valid MCA CSR-1 registration number to receive statutory CSR grants.")
        self.grants[grant.tranche_id] = grant
        return {"tranche_id": grant.tranche_id, "committed": grant.committed_amount_inr}

    def disburse_tranche_with_uc(self, tranche_id: str, disbursement_amount: float, uc_verified: bool) -> Dict[str, Any]:
        if tranche_id not in self.grants:
            raise ValueError(f"Grant {tranche_id} not found.")
        g = self.grants[tranche_id]
        
        g.disbursed_amount_inr += disbursement_amount
        g.utilization_cert_verified = uc_verified
        self.disbursed_total_inr += disbursement_amount

        remaining_statutory_csr = max(0.0, round(self.mandatory_csr_budget_inr - self.disbursed_total_inr, 2))
        return {
            "tranche_id": tranche_id,
            "ngo_partner": g.ngo_partner_name,
            "disbursed_inr": disbursement_amount,
            "remaining_unspent_csr_budget": remaining_statutory_csr,
            "is_statutory_quota_satisfied": remaining_statutory_csr == 0.0
        }
