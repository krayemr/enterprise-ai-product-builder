def determine_workflow(request_type: str) -> str:
    if request_type == "security":
        return "security_review_required"

    if request_type == "compliance":
        return "compliance_review_required"

    return "standard_processing"