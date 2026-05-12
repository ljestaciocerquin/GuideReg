from pathlib import Path


REQUIRED_TOP_LEVEL_KEYS = [
    "dataset",
    "columns",
    "output",
    "registration"
]


def validate_config(config: dict):
    # ==========================================
    # CHECK REQUIRED SECTIONS
    # ==========================================
    for key in REQUIRED_TOP_LEVEL_KEYS:
        if key not in config:
            raise ValueError(
                f"Missing required configuration section: '{key}'"
            )

    # ==========================================
    # CHECK INPUT CSV
    # ==========================================
    input_csv = Path(config["dataset"]["input_csv"])
    if not input_csv.exists():
        raise FileNotFoundError(
            f"Input CSV not found: {input_csv}"
        )

    # ==========================================
    # CHECK REGISTRATION STAGES
    # ==========================================
    valid_stages = [
        "initial",
        "rigid"
    ]
    stages = config["registration"]["stages"]
    for stage in stages:
        if stage not in valid_stages:
            raise ValueError(
                f"Invalid registration stage: '{stage}'"
            )