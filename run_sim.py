#!/usr/bin/env python

"""
Simple command line wrapper for running simulation
using simulator package.
"""
import argparse
import curses
import signal
import time

import trafficsim


MS_PER_STEP = 100
MS_PER_SEC = 1000.0


def force_quit(signum, frame):
    """Method is called whenever SIGINT or SIGTERM is sent to the running
    application. Set raise exception to terminate simulation in a controlled
    manner"""
    raise trafficsim.SimulationTerminated('Force Quit')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run Simple Traffic Signal Simulator.\n\
        To safely exit the simulation press \'q\'.')
    parser.add_argument('red_ms', type=int, help='Duration in ms for red light')
    parser.add_argument('yellow_ms', type=int, help='Duration in ms for yellow light')
    parser.add_argument('green_ms', type=int, help='Duration in ms for green light')
    parser.add_argument('step', type=int, default=MS_PER_STEP, nargs='?',
                        help='Duration in ms for simulation step. Defaults to 100ms')
    params = parser.parse_args()

    # Register
    signal.signal(signal.SIGINT, force_quit)
    signal.signal(signal.SIGTERM, force_quit)

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

        try:
            while True:
                # Poll on keyboard input - required until simulator can run
                # and print in separate thread context from display
                if stdscr.getch() == ord('q'):
                    raise trafficsim.SimulationTerminated('User Quit')

                # Perform simulator step of fixed time
                step_time = simulator.step(params.step)
                display_str = simulator.display()

                # Update Display w/ Simulator image and sleep for step time
                update_display(display_str)
                time.sleep(step_time/MS_PER_SEC)

        except trafficsim.SimulationTerminated:
            # Traffic Simulation terminated. Gracefully exit...
            update_display('Exiting Traffic Light Simulator')
            time.sleep(1)

        except Exception as err:
            raise err # Raise any other excpetions that may occur during simulation

    # Run simulation within curses display context
    curses.wrapper(run_sim)

