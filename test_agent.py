# tests/test_agent.py

import pytest

from agent.agent import Agent
from agent.router import AgentRouter
from agent.context_builder import ContextBuilder
from agent.prompt_engine import PromptEngine


# -------------------------------
# 🔹 TEST INTENT DETECTION
# -------------------------------
def test_intent_detection():
    router = AgentRouter()

    assert router.detect_intent("Who is the best user?") == "top_users"
    assert router.detect_intent("Show risk analysis") == "risk_analysis"
    assert router.detect_intent("Give summary") == "summary"


# -------------------------------
# 🔹 TEST CONTEXT BUILDER
# -------------------------------
def test_context_builder():
    cb = ContextBuilder()

    data = {
        "all_users": [
            {"user_id": "U1", "mean": 1500},
            {"user_id": "U2", "mean": 1200}
        ],
        "top_users": [
            {"user_id": "U1"}
        ]
    }

    context = cb.build("Who is best?", data, "top_users")

    assert "query" in context
    assert "data_summary" in context
    assert "key_insights" in context


# -------------------------------
# 🔹 TEST PROMPT ENGINE
# -------------------------------
def test_prompt_engine():
    pe = PromptEngine()

    context = {
        "data_summary": {"total_users": 2},
        "key_insights": {"top_users": ["U1"]}
    }

    prompt = pe.create_prompt("Who is best?", context, "top_users")

    assert "Context:" in prompt
    assert "User Query:" in prompt


# -------------------------------
# 🔹 TEST AGENT RUN
# -------------------------------
def test_agent_run():
    agent = Agent()

    data = {
        "all_users": [
            {"user_id": "U1", "mean": 1500, "risk": 100},
            {"user_id": "U2", "mean": 1000, "risk": 200}
        ],
        "top_users": [
            {"user_id": "U1"}
        ]
    }

    result = agent.run("Who is best?", data)

    assert "intent" in result
    assert "response" in result


# -------------------------------
# 🔹 EDGE CASE TEST
# -------------------------------
def test_empty_query():
    agent = Agent()

    result = agent.run("", data={})

    assert "intent" in result
    assert "response" in result