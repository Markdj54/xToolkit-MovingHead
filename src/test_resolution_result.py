from core.domain.standard_functions import PAN
from core.services.resolution_result import ResolutionResult

result = ResolutionResult(
    matched=True,
    function=PAN,
    confidence=100,
    method="exact"
)

print(result)

print()

print("Matched:", result.matched)
print("Unknown:", result.is_unknown)
print("Function:", result.function.display_name)
print("Confidence:", result.confidence)
print("Method:", result.method)