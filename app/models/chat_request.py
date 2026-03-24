from dataclasses import dataclass

@dataclass
class ChatRequest:
    user_id: str
    message: str
    timestamp: str

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'message': self.message,
            'timestamp': self.timestamp
        }

