import tkinter as tk  # Import the Tkinter library for GUI

class ProgressBar:
    def __init__(self):
        # Create the main window
        self.window = tk.Tk()
        self.window.title("Progress Bar")    # Set window title
        self.window.geometry("100x250")      # Set window size

        self.labels = []    # List to store label blocks (progress segments)
        self.color = "red"  # Initial block color
        self.progress = 0   # Current progress percentage

        # Create 10 vertical blocks for the progress bar
        for i in range(10):
            label = tk.Label(
                self.window,
                text="",
                width=2,
                height=1,
                bg=self.color,
                relief="solid",
                borderwidth=0
            )
            label.grid(row=i, column=0)  # Place label in grid
            self.labels.append(label)    # Add label to the list

        # Label to show the percentage below the blocks
        self.remaining_label = tk.Label(
            self.window,
            text=f"{self.progress}%",
            font=("Arial", 12)
        )
        self.remaining_label.grid(row=11, column=0, columnspan=1)

        # Bind the Enter key to the progress function
        self.window.bind("<Return>", self.simulate_progress)

    def simulate_progress(self, event=None):
        # If progress is less than 100%, update bar
        if self.progress < 100:
            self.progress += 10  # Increase progress by 10%
            self.remaining_label.config(text=f"{self.progress}%")  # Update label text

            self.labels[0].config(bg="green")  # Color top block green
            self.labels.pop(0)  # Remove colored block from list

            if self.progress > 90:
                self.color = "green"  # Change color to green near the end

            # Add a new block at the bottom with current color
            self.labels.append(
                tk.Label(
                    self.window,
                    text="",
                    width=2,
                    height=1,
                    bg=self.color,
                    relief="solid",
                    borderwidth=0
                )
            )
            # Place the new block in the grid
            self.labels[-1].grid(row=len(self.labels)-1, column=0)

        elif self.progress == 100:
            # If progress reaches 100%, ensure last block is green
            self.labels[-1].config(bg="green")

        else:
            # Unbind Enter key if done
            self.remaining_label.config(text="100%")
            self.window.unbind("<Return>")

    def run(self):
        # Start the Tkinter event loop
        self.window.mainloop()

# Create and run the progress bar app
progress_bar = ProgressBar()
progress_bar.run()
