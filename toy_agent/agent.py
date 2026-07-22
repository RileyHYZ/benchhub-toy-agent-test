import json
from pathlib import Path
from harbor.agents.base import BaseAgent  # Import base agent class

class ToyAgent(BaseAgent):
    @staticmethod
    def name() -> str:
        return "toy-agent"

    def version(self) -> str | None:
        return "1.0"

    def __init__(self, model_name: str | None = None, *args, **kwargs):
        super().__init__()
        self.model_name = model_name

    async def setup(self, environment):
        pass

    async def run(self, instruction, environment, context):
        print("Toy Agent starting...")
        trajectory_path = Path("/logs/agent/toy-agent.trajectory.json")
        trajectory_path.parent.mkdir(parents=True, exist_ok=True)
        trajectory_path.write_text(json.dumps({
            "schema_version": "ATIF-v1.2",
            "session_id": "toy-session",
            "agent": {
                "name": "toy-agent",
                "version": "1.0",
                "model_name": self.model_name or "toy-model"
            },
            "steps": [],
            "final_metrics": {
                "total_steps": 1,
                "mean_reward": 1.0
            }
        }))
