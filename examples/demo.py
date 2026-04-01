# examples/demo.py

from guardrails import InputClassifier, SafeResponder, EscalationManager


def run_demo(user_input: str):
    classifier = InputClassifier()
    responder = SafeResponder()
    escalation = EscalationManager()

    risk = classifier.classify(user_input)

    if risk.value == "escalate":
        escalation.trigger_escalation(user_input)

    response = responder.format_response(user_input, risk.value)

    print("=" * 50)
    print(f"User Input: {user_input}")
    print(f"Risk Level: {risk.value}")
    print("Response:")
    print(response)


if __name__ == "__main__":
    run_demo("How does machine learning work?")
    run_demo("I feel very anxious and overwhelmed")
    run_demo("I want to end my life")
