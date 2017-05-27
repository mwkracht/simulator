#!/usr/bin/env python

"""
Simple command line wrapper for running simulation
using simulator package.
"""
import argparse
import curses
import time

import trafficsim


MS_PER_STEP = 100
MS_PER_SEC = 1000.0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run Simple Traffic Signal Simulator.\n\
        To safely exit the simulation press \'q\'.')
    parser.add_argument('red_ms', type=int, help='Duration in ms for red light')
    parser.add_argument('yellow_ms', type=int, help='Duration in ms for yellow light')
    parser.add_argument('green_ms', type=int, help='Duration in ms for green light')
    parser.add_argument('step', type=int, default=MS_PER_STEP, nargs='?',
                        help='Duration in ms for simulation step. Defaults to 100ms')
    params = parser.parse_args()

    # Construct pattern from provided arguments
    pattern = trafficsim.SimplePattern(params.red_ms, params.yellow_ms, params.green_ms)

    # Construct traffic signals for simulation
    traffic_signals = [
        trafficsim.TrafficSignal(pattern)
    ]

    # Construct Simulator
    simulator = trafficsim.Simulator(traffic_signals)

    def run_sim(stdscr):
        """Simple wrapper to pass into curses to run simulator"""
        stdscr.nodelay(True) # Force curses to not block on getch()

        def update_display(display_str):
            """Update display and sleep for the given milliseconds"""
            stdscr.clear() # clear curses display
            stdscr.addstr(0, 0, display_str)
            stdscr.refresh()

        while True:
            # Poll on keyboard input - required until simulator can run
            # and print in separate thread context from display
            c = stdscr.getch()
            if c == ord('q'):
                # If 'q' is pressed exit simulation
                update_display('Exiting Traffic Light Simulator')
                time.sleep(1)
                break

            # Perform simulator step of fixed time
            step_time = simulator.step(params.step)
            display_str = simulator.display()

            # Update Display w/ Simulator image and sleep for step time
            update_display(display_str)
            time.sleep(step_time/MS_PER_SEC)

    # Run simulation within curses display context
    curses.wrapper(run_sim)

