import sys
import traceback
from my.plugins_comp import SomeReader, SomeFilter, SomeWriter
from seppl import check_compatibility


def check(pipeline):
    try:
        check_compatibility(pipeline)
    except:
        print("\n\nCompatibility check failed:", file=sys.stderr)
        print(pipeline, file=sys.stderr)
        traceback.print_exc()


check([SomeReader(), SomeWriter()])
check([SomeReader(), SomeFilter(), SomeWriter()])
check([SomeWriter(), SomeReader()])
check([SomeFilter(), SomeReader()])
