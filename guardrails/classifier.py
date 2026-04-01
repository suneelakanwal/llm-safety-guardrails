# guardrails/classifier.py

from enum import Enum
import re


class RiskLevel(Enum):
    SAFE = "safe"
    REQUIRES_REVIEW = "requires_review"
    ESCALATE = "escalate"


class InputClassifier:
    """
    Rule-based classifier for detecting risk level in user input.
    Designed to simulate lightweight LLM safety filtering.
    """

    def __init__(self):
        self.high_risk_patterns = [
            r"suicide",
            r"kill myself",
            r"end my life",
            r"self harm",
            r"hurt myself"
        ]

        self.medium_risk_patterns = [
            r"depressed",
            r"hopeless",
            r"anxious",
            r"panic",
            r"overwhelmed"
        ]

    def classify(self, text: str) -> RiskLevel:
        text = text.lower()

        for pattern in self.high_risk_patterns:
            if re.search(pattern, text):
                return RiskLevel.ESCALATE

        for pattern in self.medium_risk_patterns:
            if re.search(pattern, text):
                return RiskLevel.REQUIRES_REVIEW

        return RiskLevel.SAFE
