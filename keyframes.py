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
        time: float,
    ) -> None:
        """
        Args:
            val (float): _description_
            interpolation_mode (InterpolationMode): Describes the mode *after* this keyframe
            beat (_type_, optional): _description_. Defaults to None.
            second (_type_, optional): _description_. Defaults to None.
            frame (_type_, optional): _description_. Defaults to None.
        """
        pass


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

    def add_keyframe(self, beat) -> Keyframe:
        keyframe = Keyframe()
        self.keyframes.append(keyframe)
        return keyframe

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
