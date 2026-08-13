"""A BYO wrapper around Harbor's built-in goose agent.

Like toy_mini_swe_agent, this is not derived from harbor-custom-agents: goose
ships with Harbor, so the wrapper is an empty subclass.

It is the control case for manifest handling. Goose parses the provider out of
the model name itself and already understands the plain `google/...` name that
BenchHub submits (`case "google" | "gemini":` in Harbor's adapter), setting
GOOSE_PROVIDER and reading GOOGLE_API_KEY / GEMINI_API_KEY from the
environment. So its manifest entry declares no `model_prefix_map` and no `env`
-- a BYO agent that needs nothing beyond `import_path`.

Contrast with toy-mini-swe-agent, which hands the model straight to litellm and
therefore cannot run without the prefix map. Between them the two cover both
sides of manifest-driven model naming.
"""

from harbor.agents.installed.goose import Goose


class ToyGoose(Goose):
    """Harbor's goose agent, selectable as a BYO agent."""

    @staticmethod
    def name() -> str:
        return "toy-goose"
