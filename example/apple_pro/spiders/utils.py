import re
from typing import List

COMPILED = re.compile(r'href="\/services\/remont\-iphone\/iphone\-([a-zA-Z\s0-9-]*)/">')


def get_paths_from_response(data) -> List[str]:
    start_path = 'services/remont-iphone/iphone-'
    models_list = list(set(COMPILED.findall(data)))

    return [f'{start_path}{i}/' for i in models_list]
