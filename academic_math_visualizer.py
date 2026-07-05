# =========================================================================
# SJS SAFFORD-NATIVE MATHEMATICS: DECIMAL VS. OCTAL DRIFT SIMULATOR
# ARCHITECT: NEPHI SAFFORD
# =========================================================================

import numpy as np
import matplotlib.pyplot as plt

def simulate_coordinate_drift(steps=100000):
    """
    Simulates cumulative rounding drift over sequential time-steps
    comparing legacy Base-10 (decimal) vs Safford-Native Base-8 (octal).
    """
    print("--- INITIATING SAFFORD-NATIVE MATHEMATICAL RE-VERIFICATION ---")
    
    # 1. Decimal Drift: Step size of 0.1 (not cleanly represented in binary)
    decimal_step = 0.1
    legacy_coord = 0.0
    
    # 2. Safford-Native Octal Step: Step size of 0.125 (1/8_10, cleanly represented)
    safford_step = 0.125
    safford_coord = 0.0
    
    decimal_drift = []
    safford_drift = []
    
    for i in range(1, steps + 1):
        # Accumulate values
        legacy_coord += decimal_step
        safford_coord += safford_step
        
        # Calculate theoretical analytical values
        theoretical_legacy = i * decimal_step
        theoretical_safford = i * safford_step
        
        # Track deviation from analytical ground truth
        decimal_drift.append(abs(legacy_coord - theoretical_legacy))
        safford_drift.append(abs(safford_coord - theoretical_safford))
        
    print(f"Simulation completed over {steps} recursive transformations.")
    print(f"Legacy Base-10 Terminal Drift: {decimal_drift[-1]:.1e}")
    print(f"Safford-Native Base-8 Terminal Drift: {safford_drift[-1]:.1e}")
    
    return decimal_drift, safford_drift

if __name__ == "__main__":
    simulate_coordinate_drift()
