from datetime import datetime

class AuditMixin:
    def __init__(self, description=None):
        self._history = []
        if description:
            time = datetime.now().strftime("%H:%M:%S")
            self._history.append(f"{time} {description}")

    @property
    def history(self):
        return self._history
    
    def generate_audit_report(self):
        for c in self._history:
            yield c
