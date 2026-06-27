import json
from datetime import datetime

class AuditEngine:

    def log(self, event):

        log = {

            "timestamp": str(datetime.now()),

            "event": event

        }

        print(log)