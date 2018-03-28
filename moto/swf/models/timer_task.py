from moto.core import BaseModel
from moto.core.utils import unix_time

from threading import Timer

class TimerTask(BaseModel):
    def __init__(self, timer_id, start_to_fire_timeout, control, callback):
        self.timer_id = timer_id
        self.start_to_fire_timeout = start_to_fire_timeout
        self.control = control
        self.callback = callback
        self.timer = Timer(start_to_fire_timeout, self._on_timer_fired)

    def start(self, decision_task_completed_event_id):
        self.state = "STARTED"
        self.decision_task_completed_event_id = decision_task_completed_event_id

    def _on_timer_fired(self):
        self.callback(self)