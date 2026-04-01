# guardrails/responder.py

class SafeResponder:
    """
    Generates safe and structured responses based on risk level.
    Implements a Structured Support Response (SSR) format.
    """

    def format_response(self, user_input: str, risk_level: str) -> str:
        if risk_level == "safe":
            return self._normal_response(user_input)

        elif risk_level == "requires_review":
            return self._supportive_response(user_input)

        elif risk_level == "escalate":
            return self._critical_response()

        return "Unable to process request."

    def _normal_response(self, text: str) -> str:
        return f"I understand your question about '{text}'. Here's a helpful response."

    def _supportive_response(self, text: str) -> str:
        return (
            "Acknowledgement: I understand what you're sharing.\n"
            "Context: Situations like this can feel difficult.\n"
            "Guidance: It may help to talk to someone you trust.\n"
            "Support: You are not alone in feeling this way.\n"
            "Closing: I'm here to help if you'd like to continue."
        )

    def _critical_response(self) -> str:
        return (
            "I'm really sorry that you're going through this.\n"
            "It might help to reach out to someone who can support you directly.\n"
            "Consider contacting a trusted person or a professional.\n"
            "If you're in immediate danger, please contact emergency services."
        )
