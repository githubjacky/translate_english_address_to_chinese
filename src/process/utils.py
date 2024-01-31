import orjson
from pathlib import Path
from typing import Dict, List, Optional


def read_jsonl(
    path: str | Path,
    n: int = -1,
    return_str: bool = False
) -> List[Dict] | List[str]:
    return (
        [orjson.loads(i) for i in Path(path).read_text().split("\n")[:n]]
        if not return_str
        else
        [i for i in Path(path).read_text().split("\n")[:n]]
    )


def split_jsonl(input_path: str, n: int = 100) -> None:
    data = read_jsonl(input_path)
    with Path(f'data/processed/test_{n}.jsonl').open('w') as f:
        for i in range(n):
                f.write(
                    orjson.dumps(
                        data[i],
                        option=orjson.OPT_APPEND_NEWLINE
                    )
                    .decode()
                )
    with Path(f'data/processed/test_{n}_remained.jsonl').open('w') as f:
        for i in range(len(data)-n):
                f.write(
                    orjson.dumps(
                        data[n+i],
                        option=orjson.OPT_APPEND_NEWLINE
                    )
                    .decode()
                )

def merge_jsonl(exper_name: str,
                run_name_1: str,
                run_name_2: str,
                output_path: Optional[str] = None,
                *,
                write=False
               ):
    data = (
        read_jsonl(f'data/model_results/{exper_name}/{run_name_1}.jsonl')
        +
        read_jsonl(f'data/model_results/{exper_name}/{run_name_2}.jsonl')
    )
    if write and output_path is not None:
        with Path(otuput_path).open('w'):
            for item in data:
                f.write(
                    orjson.dumps(
                        item,
                        option=orjson.OPT_APPEND_NEWLINE
                    )
                    .decode()
                )
    return data