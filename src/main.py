#!/usr/bin/env python
import warnings

from src.crew import FlightFinderCrewai

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the crew.
    """
    inputs = {
        "origin": "HKG",
        "destination": "LAX",
        "departure_date": "2024-12-25",
        "return_date": "2025-01-25",
    }
    FlightFinderCrewai().crew().kickoff(inputs=inputs)
