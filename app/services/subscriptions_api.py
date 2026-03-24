import requests

from app.config import (
    PAUSE_SUBSCRIPTION_URL,
    RENEW_SUBSCRIPTION_URL,
    UPGRADE_SUBSCRIPTION_URL,
    CANCEL_SUBSCRIPTION_URL
)

def pause_subscription(user_id: str, reason: str = "requested_by_user") -> str:
    payload = {
        "userId": user_id,
        "reason": reason
    }
    
    response = requests.post(PAUSE_SUBSCRIPTION_URL, json=payload, timeout=10)
    response.raise_for_status()

    return response.text

def renew_subscription(user_id: str) -> str:
    payload = {
        "userId": user_id
    }

    response = requests.post(RENEW_SUBSCRIPTION_URL, json=payload, timeout=10)
    response.raise_for_status()

    return response.text

def upgrade_subscription(user_id: str, new_plan: str) -> str:
    payload = {
        "userId": user_id,
        "newPlan": new_plan
    }

    response = requests.post(UPGRADE_SUBSCRIPTION_URL, json=payload, timeout=10)
    response.raise_for_status()

    return response.text

def cancel_subscription(user_id: str, reason: str) -> str:
    payload = {
        "userId": user_id,
        "reason": reason
    }

    response = requests.post(CANCEL_SUBSCRIPTION_URL, json=payload, timeout=10)
    response.raise_for_status()

    return response.text
