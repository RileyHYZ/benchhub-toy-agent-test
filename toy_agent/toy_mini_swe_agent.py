"""A BYO wrapper around Harbor's built-in mini-swe-agent.

Unlike the other agents here, this one is not derived from harbor-custom-agents:
mini-swe-agent ships with Harbor itself, so the wrapper is deliberately empty.
Everything that makes it run under BenchHub is declared in manifest.json.

That is the point of this agent. mini-swe-agent passes `--model` straight to
litellm, which recognises `gemini/...` and `vertex_ai/...` but not the plain
`google/...` name BenchHub submits. Harbor then resolves the API key variable
from that provider (`gemini` -> GEMINI_API_KEY). Without a correct prefix the
run fails before the model is ever called, with "Unable to determine API key for
model google/gemini-3.5-flash".

`model_prefix_map` in the manifest fixes that, so there is no prefix handling in
this file. If you find yourself adding some, the manifest is not being applied.
"""

from harbor.agents.installed.mini_swe_agent import MiniSweAgent


class ToyMiniSweAgent(MiniSweAgent):
    """Harbor's mini-swe-agent, selectable as a BYO agent."""

    @staticmethod
    def name() -> str:
        return "toy-mini-swe-agent"
