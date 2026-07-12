"""
profile_builder.py

Builds a FixtureProfile from a CanonicalFixture.
"""

from core.domain.fixture_profile import FixtureProfile


class ProfileBuilder:

    def build(self, fixture):

        profile = FixtureProfile(
            name=fixture.name,
            manufacturer=fixture.manufacturer,
            model=fixture.model,
            mode=fixture.mode,
        )

        for capability in fixture.capabilities:
            profile.add(capability.function)

        return profile