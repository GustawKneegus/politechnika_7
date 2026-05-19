import pytest

tenant_1 = {
    "id": "tenant-1",
    "rent": 1000
}
tenant_2 = {
    "id": "tenant-2",
    "rent": 1500
}

class PaymentChecker:
    def __init__(self, tenants):
        self.tenants = tenants
    def check_payment(self, payment):
        tenant = self.tenants.get(payment["tenant_id"])
        if tenant is None:
            return ["Wrong tenant"]
        if payment["amount"] != tenant["rent"]:
            return ["Wrong amount"]
        return []


def test_payment_ok():
    checker = PaymentChecker({
        "tenant-1": tenant_1,
        "tenant-2": tenant_2
    })
    payment = {
        "tenant_id": "tenant-1",
        "amount": 1000
    }
    assert checker.check_payment(payment) == []

def test_wrong_tenant():
    checker = PaymentChecker({
        "tenant-1": tenant_1,
        "tenant-2": tenant_2
    })
    payment = {
        "tenant_id": "tenant-999",
        "amount": 1000
    }
    assert checker.check_payment(payment) == ["Wrong tenant"]


def test_wrong_amount():
    checker = PaymentChecker({
        "tenant-1": tenant_1,
        "tenant-2": tenant_2
    })
    payment = {
        "tenant_id": "tenant-2",
        "amount": 2000
    }
    assert checker.check_payment(payment) == ["Wrong amount"]