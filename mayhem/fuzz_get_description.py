#!/usr/bin/python3
import sys
import atheris

with atheris.instrument_imports():
    from cron_descriptor import get_description, MissingFieldException, FormatException

def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)

    str_len = fdp.ConsumeIntInRange(0, 100)
    str = fdp.ConsumeUnicodeNoSurrogates(str_len)

    try:
        get_description(str)
    except(MissingFieldException):
        pass
    except(FormatException):
        pass

atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()
