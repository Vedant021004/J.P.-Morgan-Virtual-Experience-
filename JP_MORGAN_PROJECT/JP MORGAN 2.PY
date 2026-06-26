
from datetime import datetime

def price_gas_storage_contract(
    injection_dates,
    withdrawal_dates,
    purchase_prices,
    sale_prices,
    volumes,
    max_storage_volume,
    storage_cost_per_month
):
    """
    Prices a gas storage contract.

    Parameters:
    -----------
    injection_dates : list of strings (YYYY-MM-DD)
    withdrawal_dates : list of strings (YYYY-MM-DD)
    purchase_prices : list of floats
    sale_prices : list of floats
    volumes : list of floats
    max_storage_volume : float
    storage_cost_per_month : float

    Returns:
    --------
    contract_value : float
    """

    total_purchase_cost = 0
    total_sale_revenue = 0
    total_storage_cost = 0

    current_storage = 0

    for i in range(len(volumes)):

        volume = volumes[i]

        if current_storage + volume > max_storage_volume:
            raise ValueError(
                "Storage capacity exceeded."
            )

        current_storage += volume

        total_purchase_cost += (
            volume * purchase_prices[i]
        )

        total_sale_revenue += (
            volume * sale_prices[i]
        )

        injection_date = datetime.strptime(
            injection_dates[i],
            "%Y-%m-%d"
        )

        withdrawal_date = datetime.strptime(
            withdrawal_dates[i],
            "%Y-%m-%d"
        )

        storage_months = (
            withdrawal_date - injection_date
        ).days / 30

        total_storage_cost += (
            storage_months
            * storage_cost_per_month
            * volume
        )

    contract_value = (
        total_sale_revenue
        - total_purchase_cost
        - total_storage_cost
    )

    return contract_value


# Example test case

contract_value = price_gas_storage_contract(
    injection_dates=[
        "2024-01-01",
        "2024-03-01"
    ],
    withdrawal_dates=[
        "2024-06-01",
        "2024-09-01"
    ],
    purchase_prices=[
        2.50,
        2.70
    ],
    sale_prices=[
        3.20,
        3.60
    ],
    volumes=[
        100000,
        50000
    ],
    max_storage_volume=200000,
    storage_cost_per_month=0.02
)

print(
    f"Contract Value: ${contract_value:,.2f}"
)
