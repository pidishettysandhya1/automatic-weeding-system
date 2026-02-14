import time
import random
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter
from matplotlib.colors import ListedColormap


def paddy_weeding_system():

    GRID_SIZE = 10

    # ---- Create Field ----
    field = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)

    # AI-based probability heatmap
    probability_map = np.random.rand(GRID_SIZE, GRID_SIZE)
    threshold = 0.75

    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if probability_map[i][j] > threshold:
                field[i][j] = 1   # Weed

    # Add obstacles
    for _ in range(8):
        x = random.randint(0, GRID_SIZE - 1)
        y = random.randint(0, GRID_SIZE - 1)
        if field[x][y] == 0:
            field[x][y] = -1   # Obstacle

    # ---- Counters ----
    weed_removed = 0
    cells_covered = 0
    total_weeds = np.count_nonzero(field == 1)

    # ---- Zig-Zag Path ----
    path = []
    for i in range(GRID_SIZE):
        if i % 2 == 0:
            col_range = range(GRID_SIZE)
        else:
            col_range = range(GRID_SIZE - 1, -1, -1)

        for j in col_range:
            path.append((i, j))

    start_time = time.time()

    # ---- Animation Setup ----
    fig, ax = plt.subplots()

    # Background heatmap
    ax.imshow(probability_map, cmap='YlOrRd', alpha=0.4)

    cmap = ListedColormap(["black", "white", "red", "green"])
    img = ax.imshow(field, cmap=cmap, vmin=-1, vmax=2)

    robot_dot, = ax.plot([], [], 'bo', markersize=8)

    ax.set_xticks(range(GRID_SIZE))
    ax.set_yticks(range(GRID_SIZE))
    ax.grid(True)

    def update(frame):
        nonlocal weed_removed, cells_covered

        x, y = path[frame]
        cells_covered += 1

        # Skip obstacle
        if field[x][y] == -1:
            robot_dot.set_data(y, x)
            return img, robot_dot

        # Remove weed
        if field[x][y] == 1:
            field[x][y] = 2
            weed_removed += 1

        img.set_data(field)
        robot_dot.set_data(y, x)

        efficiency = weed_removed / cells_covered if cells_covered else 0
        elapsed_time = round(time.time() - start_time, 2)

        ax.set_title(
            f"Smart Weeding Robot Simulation\n"
            f"Weeds Removed: {weed_removed}/{total_weeds} | "
            f"Cells Covered: {cells_covered} | "
            f"Efficiency: {efficiency:.2f} | "
            f"Time: {elapsed_time}s"
        )

        return img, robot_dot

    ani = FuncAnimation(
        fig,
        update,
        frames=len(path),
        interval=300,
        repeat=False
    )

    # ---- Save Video in Same Project Folder ----
    output_path = os.path.join(os.path.dirname(__file__), "smart_weeding_robot.mp4")
    writer = FFMpegWriter(fps=3)
    ani.save(output_path, writer=writer)

    plt.show()


if __name__ == "__main__":
    paddy_weeding_system()
