from scipy.io import loadmat
from ..coare35 import xcoare35

# rev = loadmat("/home/deepak/work/coare3_6/Revelle10minutesLeg3_r3.mat", squeeze_me=True)
# mat = loadmat("/home/deepak/work/coare3_6/revelle_35.mat", squeeze_me=True)['A35']
# expected = output_to_xr(mat.T, xr.DataArray(data=mat[:, 0], dims=("yday", )))
# expected["yday"] = revds.yday
# expected.to_netcdf("tests/expected_revelle_35.nc")

# revds = xr.Dataset()
# for var in rev:
#     if "__" in var:
#         continue
#     revds[var] = (("yday",), rev[var])


def test_35():
    revds = xr.open_dataset("tests/Revelle10minutesLeg3_r3.nc")
    expected = xr.open_dataset("tests/expected_revelle_35.nc")

    actual = xcoare35(
        revds["U10"],
        10,
        revds["T10"],
        10,
        revds["RH10"],
        10,
        revds["Pair10"],
        revds["Tsea5"],
        -revds["Solardn"],
        -revds["IRdn"],
        revds["Lat"],
        600,
        revds["P"],
    )

    # import matplotlib.pyplot as plt
    # # %matplotlib qt
    # # revds.stress.plot()
    # expected.tau.plot()
    # calc.tau.plot()

    xr.testing.assert_allclose(expected, actual)
