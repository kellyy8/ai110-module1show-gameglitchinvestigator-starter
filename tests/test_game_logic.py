from logic_utils import check_guess, parse_guess

# ================================================================
# Test check_guess() logic
# ================================================================

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

def test_check_guess_regression_high_low_not_inverted():
    # Regression guard: this used to incorrectly report "Too Low".
    result = check_guess(51, 50)
    assert result == "Too High"
    assert result != "Too Low"

# ================================================================
# Test parse_guess() logic 
# ================================================================

def test_parse_guess_non_numeric_input():
    ok, value, err = parse_guess("abc", 1, 100)
    assert ok is False
    assert value is None
    assert err == "That is not a number."

def test_parse_guess_out_of_bounds_input_upper():
    ok, value, err = parse_guess("101", 1, 100)
    assert ok is False
    assert value is None
    assert err == "Guess must be between 1 and 100."

def test_parse_guess_out_of_bounds_input_lower():
    ok, value, err = parse_guess("0", 1, 100)
    assert ok is False
    assert value is None
    assert err == "Guess must be between 1 and 100."

def test_parse_guess_valid_at_lower_bound():
    ok, value, err = parse_guess("1", 1, 100)
    assert ok is True
    assert value == 1
    assert err is None

def test_parse_guess_valid_at_upper_bound():
    ok, value, err = parse_guess("100", 1, 100)
    assert ok is True
    assert value == 100
    assert err is None

def test_parse_guess_valid_inside_bounds():
    ok, value, err = parse_guess("42", 1, 100)
    assert ok is True
    assert value == 42
    assert err is None
