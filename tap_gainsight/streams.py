"""Stream type classes for tap-gainsight."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_gainsight.client import GainsightStream

# TODO: Delete this is if not using json files for schema definition
# SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class ClientsStream(GainsightStream):
    """Stream to retrieve client info"""

    name = "clients"
    path = "v1/data/objects/query/Company"
    primary_keys = ["Gsid"]

    # Optionally, you may also use `schema_filepath` in place of `schema`:
    # schema_filepath = SCHEMAS_DIR / "users.json"
    schema = th.PropertiesList(
        th.Property("Gsid", th.StringType, description="The client's system ID"),
    ).to_dict()
