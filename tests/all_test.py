

import numpy as np
import pytest
import quaternion


@pytest.fixture(scope="module")
def q():
    angle = np.pi * 0.5
    axsis = np.array([0, 0, 1])
    return quaternion.rotation(angle, axsis)


def test_real(q):
    desired = np.cos(np.pi * 0.25)
    np.testing.assert_almost_equal(q[0], desired)


def test_img(q):
    desired = np.array([0, 0, 1]) * np.cos(np.pi * 0.25)
    np.testing.assert_almost_equal(q[1:], desired)
