import pytest
from pydantic import ValidationError
from mission import Member


class TestMemberDefaults:
    """기본값이 올바르게 설정되는지 테스트"""

    def test_default_point(self):
        m = Member(username="alice", age=20)
        assert m.point == 0

    def test_default_is_premium(self):
        m = Member(username="alice", age=20)
        assert m.is_premium is False

    def test_explicit_values(self):
        m = Member(username="alice", age=25, point=100, is_premium=True)
        assert m.username == "alice"
        assert m.age == 25
        assert m.point == 100
        assert m.is_premium is True


class TestUsernameValidation:
    """username 필드 검증 테스트"""

    def test_valid_username(self):
        m = Member(username="alice", age=20)
        assert m.username == "alice"

    def test_username_too_short(self):
        with pytest.raises(ValidationError):
            Member(username="ab", age=20)

    def test_username_min_boundary(self):
        m = Member(username="abc", age=20)
        assert m.username == "abc"

    def test_username_too_long(self):
        with pytest.raises(ValidationError):
            Member(username="a" * 21, age=20)

    def test_username_max_boundary(self):
        m = Member(username="a" * 20, age=20)
        assert m.username == "a" * 20


class TestAgeValidation:
    """age 필드 검증 테스트"""

    def test_valid_age(self):
        m = Member(username="alice", age=20)
        assert m.age == 20

    def test_age_too_young(self):
        with pytest.raises(ValidationError):
            Member(username="alice", age=13)

    def test_age_min_boundary(self):
        m = Member(username="alice", age=14)
        assert m.age == 14


class TestRequiredFields:
    """필수 필드 누락 시 에러 테스트"""

    def test_missing_username(self):
        with pytest.raises(ValidationError):
            Member(age=20)

    def test_missing_age(self):
        with pytest.raises(ValidationError):
            Member(username="alice")


class TestTypeValidation:
    """타입 검증 테스트"""

    def test_age_not_string(self):
        with pytest.raises(ValidationError):
            Member(username="alice", age="not_a_number")

    def test_is_premium_type(self):
        m = Member(username="alice", age=20, is_premium=True)
        assert isinstance(m.is_premium, bool)