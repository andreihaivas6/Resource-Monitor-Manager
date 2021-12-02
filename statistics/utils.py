import matplotlib.axes

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

    @staticmethod
    def get_front_padding(resources: list) -> list:
        return [0.] * (CanvasConfig.MAX_SECONDS_ON_PLOTS - len(resources))

    @staticmethod
    def draw_plot(
            axes: matplotlib.axes.Axes, x_list: list, y_list: list, color: str, label: str, alpha: int = 0.4) -> None:
        axes.fill_between(
            x_list,
            y_list,
            color=color,
            alpha=alpha,
        )

        axes.plot(
            x_list,
            y_list,
            color=color,
            label=label,
        )
        axes.legend()
