from app.invoice import calculate_subtotal, calculate_tax, calculate_invoice_total

def test_calculate_subtotal():
    # Arrange
    unit_price = 25000
    quantity = 4
    expected_subtotal = 100000

    # Act
    result = calculate_subtotal(unit_price, quantity)

    # Assert
    assert result == expected_subtotal

def test_calculate_tax():
    # Arrange
    subtotal = 100000
    tax_rate = 19
    expected_tax = 19000.0

    # Act
    result = calculate_tax(subtotal, tax_rate)

    # Assert
    assert result == expected_tax

def test_calculate_invoice_total():
    # Arrange
    unit_price = 50000
    quantity = 2
    tax_rate = 19
    expected_total = 119000

    # Act
    result = calculate_invoice_total(unit_price, quantity, tax_rate)

    # Assert
    assert result == expected_total
