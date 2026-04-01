# tests/test_guardrails.py

from guardrails.classifier import InputClassifier, RiskLevel


def test_safe_input():
    clf = InputClassifier()
    assert clf.classify("What is AI?") == RiskLevel.SAFE


def test_medium_risk():
    clf = InputClassifier()
    assert clf.classify("I feel anxious") == RiskLevel.REQUIRES_REVIEW


def test_high_risk():
    clf = InputClassifier()
    assert clf.classify("I want to kill myself") == RiskLevel.ESCALATE
