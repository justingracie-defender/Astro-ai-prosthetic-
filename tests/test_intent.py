from astro.intent import estimate_intent


def test_estimate_intent_defaults_to_safe_zero_low_confidence():
    intent = estimate_intent({})
    assert intent.target_position_deg == 0.0
    assert intent.target_velocity_deg_s == 0.0
    assert intent.estimated_torque_nm == 0.0
    assert intent.confidence == 0.0
