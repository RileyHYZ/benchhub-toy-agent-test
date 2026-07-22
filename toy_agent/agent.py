import json
import os
import sys

class ToyAgent:
    """A minimal Harbor-compatible mock agent."""
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        print(f"ToyAgent initialized with kwargs: {kwargs}", file=sys.stderr)

    def run(self, task_prompt: str, **kwargs):
        print(f"Executing task: {task_prompt}", file=sys.stderr)
        # Write a dummy telemetry file so the parser succeeds
        os.makedirs("output", exist_ok=True)
        telemetry_data = {
            "status": "completed",
            "score": 1.0,
            "metrics": {
                "steps": 1,
                "tokens": 42
            }
        }
        with open("output/run.telemetry.json", "w") as f:
            json.dump(telemetry_data, f)
        print("Task execution completed. Telemetry written to output/run.telemetry.json", file=sys.stderr)
        return "Task completed"
