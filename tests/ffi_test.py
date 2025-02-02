# Copyright 2024 The JAX Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations

import os
import unittest

from absl.testing import absltest

import jax
import jax.extend as jex

from jax._src import test_util as jtu
from jax._src.lib import xla_extension_version

jax.config.parse_flags_with_absl()


class FfiTest(jtu.JaxTestCase):

  @unittest.skipIf(xla_extension_version < 265, "Requires jaxlib 0.4.29")
  def testHeadersExist(self):
    base_dir = os.path.join(jex.ffi.include_dir(), "xla", "ffi", "api")
    for header in ["c_api.h", "api.h", "ffi.h"]:
      self.assertTrue(os.path.exists(os.path.join(base_dir, header)))


if __name__ == "__main__":
  absltest.main(testLoader=jtu.JaxTestLoader())
