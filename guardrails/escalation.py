# guardrails/escalation.py

from datetime import datetime


class EscalationManager:
    """
    Handles escalation events for high-risk inputs.
    Stores logs for audit or human review.
    """

    def __init__(self):
        self.log = []

    def trigger_escalation(self, user_input: str):
        event = {
            "timestamp": datetime.utcnow().isoformat(),
            "input": user_input,
            "action": "ESCALATED_TO_HUMAN"
        }
        self.log.append(event)
        return event

    def get_logs(self):
        return self.log
