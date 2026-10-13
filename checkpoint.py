import os

checkpoint_filename = "last_processed.txt"


class CheckPoint:
    def __init__(self, filename: str = "last_processed.txt") -> None:
        self.filename = filename

    def get_last_processed_row(self):
        """Reads the last processed row index from the checkpoint file."""
        if os.path.exists(checkpoint_filename):
            with open(checkpoint_filename, "r") as f:
                content = f.read().strip()
                return int(content) if content.isdigit() else 0
        return 0

    def update_checkpoint(self, row_index: int):
        """Saves the current row index to the checkpoint file."""
        # Using 'w' overwrites the file, keeping it small and fast
        with open(checkpoint_filename, "w") as f:
            f.write(str(row_index))
