
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding="utf-8").read()


setup(
    name="gptq_for_llama",
    version="0.1.1",
    url="https://github.com/paolorechia/gptq-for-llama-old",
    src=".",
    python_requires=">=3.9",
)