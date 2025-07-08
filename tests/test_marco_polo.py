"""Unit tests for marco_polo function."""

from juancobo6_marco_polo import marco_polo


class TestMarcoPolo:
    """Test cases for the marco_polo function."""

    def test_marco_returns_polo(self) -> None:
        """Test that 'Marco' returns 'Polo'."""
        result = marco_polo("Marco")
        assert result == "Polo"

    def test_marco_case_sensitive(self) -> None:
        """Test that the function is case sensitive."""
        result = marco_polo("marco")
        assert result is None

    def test_marco_uppercase(self) -> None:
        """Test that 'MARCO' returns None."""
        result = marco_polo("MARCO")
        assert result is None

    def test_empty_string(self) -> None:
        """Test that empty string returns None."""
        result = marco_polo("")
        assert result is None

    def test_other_names(self) -> None:
        """Test that other names return None."""
        test_cases = ["Juan", "Pedro", "Ana", "Carlos", "Maria"]
        for name in test_cases:
            result = marco_polo(name)
            assert result is None, f"Expected None for {name}, got {result}"

    def test_marco_with_spaces(self) -> None:
        """Test that 'Marco' with spaces returns None."""
        result = marco_polo(" Marco ")
        assert result is None

    def test_marco_with_numbers(self) -> None:
        """Test that 'Marco123' returns None."""
        result = marco_polo("Marco123")
        assert result is None

    def test_partial_marco(self) -> None:
        """Test that partial 'Marco' returns None."""
        result = marco_polo("Mar")
        assert result is None

    def test_marco_with_special_chars(self) -> None:
        """Test that 'Marco!' returns None."""
        result = marco_polo("Marco!")
        assert result is None

    def test_function_type_hints(self) -> None:
        """Test that the function accepts str and returns str or None."""
        result = marco_polo("Marco")
        assert isinstance(result, str)
        assert result == "Polo"

        result = marco_polo("NotMarco")
        assert result is None
