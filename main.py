def amt(wages, cap_gains_base, tax_paid_ytd, n_shares):
    standard_deduction = 12_950

    fmv = 17.26
    strike_price = 3.56

    bargain_element = (fmv - strike_price) * n_shares

    total_income = cap_gains_base + wages + bargain_element
    taxable_income = total_income - standard_deduction

    amt_exempt = 75_900
    p28_limit = 206_100
    rate1 = 0.26
    rate2 = 0.28
    phase_out = 539_900

    amt_taxable = total_income - amt_exempt

    amt_tax = min(amt_taxable, p28_limit) * rate1
    amt_tax += max(0, amt_taxable - p28_limit) * rate2

    remainder = amt_tax - tax_paid_ytd
    return remainder


if __name__ == "__main__":
    low = 5000
    high = 20000
    mid = 0
    price = 0
    cash = 80000
    tax_paid = 41782 + 30627
    cap_gains_base = 77_110
    salary = 100_000

    for _ in range(100):
        mid = int((low + high) / 2)
        price = mid * 3.56 + amt(salary, cap_gains_base, tax_paid, mid)
        if price > cash:
            high = mid
        else:
            low = mid
    print(f"exercising {mid} options will cost {price}")
