import sys
from pathlib import Path

sys.path.append(Path('~', '.zipline').expanduser().as_posix())
from zipline.data.bundles import register
from stooq_us_stocks import stooq_jp_to_bundle
from datetime import time
from pytz import timezone


register('stooq',
         stooq_jp_to_bundle(),
         calendar_name='XNYS',
         )


