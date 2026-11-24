import unittest
from csr_section135_grant.engine import CSRGrantTranche, CSRMandatoryComplianceEngine

class TestCSRMandatoryComplianceEngine(unittest.TestCase):
    def setUp(self):
        # Average profit: (100Cr + 120Cr + 110Cr)/3 = 110Cr -> 2% CSR = 2.2Cr (22,000,000 INR)
        self.engine = CSRMandatoryComplianceEngine(1000000000.0, 1200000000.0, 1100000000.0)

    def test_budget_calculation_and_tranche(self):
        self.assertEqual(self.engine.mandatory_csr_budget_inr, 22000000.0)
        grant = CSRGrantTranche(
            tranche_id="GRANT-EDU-2026-01", ngo_partner_name="Pratham Education Foundation",
            mca_csr1_reg_no="CSR00012441", schedule_vii_activity="EDUCATION",
            committed_amount_inr=22000000.0
        )
        self.engine.allocate_grant_tranche(grant)
        res = self.engine.disburse_tranche_with_uc("GRANT-EDU-2026-01", 22000000.0, uc_verified=True)
        self.assertTrue(res["is_statutory_quota_satisfied"])
        self.assertEqual(res["remaining_unspent_csr_budget"], 0.0)

if __name__ == "__main__":
    unittest.main()
