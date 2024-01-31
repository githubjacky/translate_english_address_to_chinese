import orjson
import pandas as pd
from pathlib import Path
from typing import Optional


def csv2jsonl(input_path: str, output_path: Optional[str] = None, *, write=False):
    df = pd.read_csv(input_path)
    output_list = []
    for i in range(len(df)):
        output_list.append({
            "owner_id": int(df.at[i, 'owner_id']),
            "owner_address": df.at[i, 'owner_address']
        })

    if write and output_path is not None:
        with Path(output_path).open('w') as f:
            for item in output_list:
                f.write(
                    orjson.dumps(
                        item,
                        option=orjson.OPT_APPEND_NEWLINE
                    )
                    .decode()
                )

    return output_list