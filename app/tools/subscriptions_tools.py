import json
from langchain.tools import Tool
from app.services.subscriptions_api import (
    pause_subscription,
    renew_subscription,
    upgrade_subscription,
    cancel_subscription
)

def pause_susbscription_tool(input_str: str) -> str:
    """
    Expected input JSON:
    {"userId": "12345", "reason": "temporary financial issue"}
    """
    data = json.loads(input_str)
    user_id = data["userId"]
    reason = data.get("reason", "requested_by_user")
    return pause_subscription(user_id, reason)

def renew_susbscription_tool(input_str: str) -> str:
    """
    Expected input JSON:
    {"userId": "12345"}
    """

    data = json.loads(input_str)
    user_id = data["userId"]
    return renew_subscription(user_id)

def upgrade_subscription_tool(input_str: str) -> str:
    """
    Expected input JSON:
    {"userId": "12345", "newPlan": "premium"}
    """

    data = json.loads(input_str)
    user_id = data["userId"]
    plan = data["plan"]
    return upgrade_subscription(user_id, plan)

def cancel_subscription_tool(input_str: str) -> str:
    """
    Expected input JSON:
    {"userId": "12345", "reason": "found better alternative"}
    """

    data = json.loads(input_str)
    user_id = data["userId"]
    reason = data["reason"]
    return cancel_subscription(user_id, reason)

def get_tools():
    return [
        Tool(
            name="PausEsubscription",
            func=pause_susbscription_tool,
            description=("Use this when the user wants to pause or temporarily stop their subscription. "
                "Input must be JSON with userId and optional reason. "
                'Example: {"userId":"12345","reason":"vacation"}'),
        ),
        Tool(
            name="RenewSubscription",
            func=renew_susbscription_tool,
            description=("Use this when the user wants to renew their subscription. "
                "Input must be JSON with userId. "
                'Example: {"userId":"12345"}'),
        ),
        Tool(
            name="UpgradeSubscription",
            func=upgrade_subscription_tool,
            description=("Use this when the user wants to upgrade their subscription plan. "
                "Input must be JSON with userId and plan. "
                'Example: {"userId":"12345","plan":"premium"}'),
        ),
        Tool(
            name="CancelSubscription",
            func=cancel_subscription_tool,
            description=("Use this when the user wants to cancel their subscription. "
                "Input must be JSON with userId and reason. "
                'Example: {"userId":"12345","reason":"found better alternative"}'),
        )
    ]