from dataclasses import dataclass
from decimal import Decimal
from typing import Literal, Optional, Tuple


class InterpolationMode:
    def __init__(self) -> None:
        pass


TimeUnit = Literal["beat", "second", "frame"]


@dataclass
class Keyframe:
    val: float
    time: Decimal


class Timeline:
    """
    Represents the animation timeline of a single parameter
    """

    def __init__(
        self, keyframes: list[Keyframe], time_unit: TimeUnit = "frame", repeat_after: int = 0
    ) -> None:
        self.keyframes: list[Keyframe] = keyframes
        self.time_unit = time_unit
        self.repeat_after = repeat_after

    def _get_first_keyframe(self):
        return self.keyframes[0]

    def _get_last_keyframe(self):
        return self.keyframes[len(self.keyframes) - 1]


    def _get_keyframes_for_frame(self, frame: int) -> Tuple[Keyframe, Keyframe]:
        start = self._get_last_keyframe() 
        end = self._get_first_keyframe() 

    def set_scene(self, scene) -> None:
        self.scene = scene

    def get_val_at_frame(self, frame: int) -> float:
        return 0


class Scene:
    def __init__(self, bpm=120, fps=24) -> None:
        self.bpm = bpm
        self.fps = fps
        self.timelines: list[Timeline] = []

    def add_timeline(self, timeline: Timeline):
        timeline.set_scene(self)
        self.timelines.append(timeline)
