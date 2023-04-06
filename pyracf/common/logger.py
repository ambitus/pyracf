"""Logging for pyRACF."""


class Logger:
    """Logging for pyRACF."""

    debug_color = "\033[1;35m"
    reset_color = "\033[0m"
    debug_label = "[ Debug ]"

    def log_debug(self, message: str) -> None:
        """Log function to use for debug logging."""
        print(f"{self.debug_color}{self.debug_label}{self.reset_color} {message}")
