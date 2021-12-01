from statistics.canvas_config import CanvasConfig


class Utils:
    @staticmethod
    def get_seconds(resources: list) -> list:
        return [
            second
            for second in range(CanvasConfig.MAX_SECONDS_ON_PLOTS - len(resources))
        ] + [
            second + CanvasConfig.MAX_SECONDS_ON_PLOTS - len(resources)
            for second in range(len(resources))
        ]
