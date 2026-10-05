import pytest

from policy import determine_workflow


@pytest.mark.parametrize(
    "request_type, expected_workflow",
    [
        ("feature", "standard_processing"),
        ("bug", "standard_processing"),
        ("security", "security_review_required"),
        ("compliance", "compliance_review_required"),
    ],
)
def test_determine_workflow(request_type, expected_workflow):
    result = determine_workflow(request_type)

    assert result == expected_workflow