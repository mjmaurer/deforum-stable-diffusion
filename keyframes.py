from decimal import Decimal
from typing import Literal


class InterpolationMode:
    def __init__(self) -> None:
        pass


KeyframeTimeUnit = Literal["beat", "second", "frame"]


class Keyframe:
    def __init__(
        self,
        val: float,
        interpolation_mode: InterpolationMode,
        time_measure: KeyframeTimeUnit,
        beat: Decimal,
        second: Decimal,
        frame: int,
    ) -> None:
        """
        Args:
            val (float): _description_
            interpolation_mode (InterpolationMode): Describes the mode *after* this keyframe
        """
        if time_measure == "frame" and not frame:
            raise Exception("No frame specified")
        if time_measure == "beat" and not beat:
            raise Exception("No beat specified")
        if time_measure == "second" and not second:
            raise Exception("No second specified")
        self.beat = beat
        self.frame = frame
        self.second = second


class KeyframeFactory:
    def __init__(self) -> None:
        pass


class Timeline:
    """
    Represents the animation timeline of a single parameter
    """

    def __init__(self, scene) -> None:
        self.keyframes: list[Keyframe] = []
        self.scene: Scene = scene

    def add_keyframe(self, keyframe: Keyframe) -> None:
        self.keyframes.append(keyframe)

    def get_val_at_frame(self, frame: int) -> float:
        return 0


class Scene:
    def __init__(self, bpm, fps) -> None:
        self.bpm = bpm
        self.fps = fps
        self.timelines: list[Timeline] = []

    def new_timeline(self) -> Timeline:
        timeline = Timeline(self)
        self.timelines.append(timeline)
        return timeline
