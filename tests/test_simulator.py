"""Module contains test cases for simulator module in trafficsim package."""
import pytest

import trafficsim


def test_simulator_constructor_illegal_objects():
    """Verify constructor raises exception when non-Simulator class objects are passed in."""
    with pytest.raises(trafficsim.IllegalSimulation):
        trafficsim.Simulator(simulated_objects=[
            trafficsim.TrafficSignal(trafficsim.SimplePattern(100, 200, 300)),
            'wrong type']
        )


def test_simulator_simple_traffic_signal():
    """Verify simulator correctly steps through simulation of a simple pattern traffic signal."""
    traffic_signal = trafficsim.TrafficSignal(trafficsim.SimplePattern(500, 1000, 750))
    simulator = trafficsim.Simulator([traffic_signal])

    assert simulator.display() == trafficsim.display.GREEN_LIGHT

    step_time = simulator.step()
    assert step_time == 750  # transition from green -> yellow
    assert simulator.display() == trafficsim.display.YELLOW_LIGHT

    step_time = simulator.step(999)  # explicitly step 999ms
    assert step_time == 999  # 999ms will not have transitioned yet from yellow -> red
    assert simulator.display() == trafficsim.display.YELLOW_LIGHT

    step_time = simulator.step(2)
    assert step_time == 2 # transition yellow -> red
    assert simulator.display() == trafficsim.display.RED_LIGHT

    step_time = simulator.step()
    assert step_time == 499  # remainder of red light duration - transition red - green
    assert simulator.display() == trafficsim.display.GREEN_LIGHT
