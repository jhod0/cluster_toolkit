import pytest
from cluster_toolkit import bias
from os.path import dirname, join
import numpy as np
import numpy.testing as npt

#Halo properties that are inputs
rhomconst = 2.775808e+11 #units are SM h^2/Mpc^3
Mass = 1e14 #Msun/h
Omega_m = 0.3 #arbitrary
datapath = "./data_for_testing/"
klin = np.loadtxt(join(dirname(__file__),datapath+"klin.txt")) #h/Mpc; wavenumber
plin = np.loadtxt(join(dirname(__file__),datapath+"plin.txt")) #[Mpc/h]^3 linear power spectrum
Ma = np.array([1e13, 1e14, 1e15]) #Msun/h

def test_exceptions_bias_at_M():
    with pytest.raises(TypeError):
        bias.bias_at_M()
        bias.bias_at_M(Mass, klin, plin)
        bias.bias_at_M(Mass, klin, plin, Omega_m, Omega_m)
        bias.bias_at_M("a string", klin, plin, Omega_m)

def test_outputs_bias_at_M():
    #List vs. numpy.array
    npt.assert_array_equal(bias.bias_at_M(Ma, klin, plin, Omega_m), bias.bias_at_M(Ma.tolist(), klin, plin, Omega_m))
    #Single value vs numpy.array
    arrout = bias.bias_at_M(Ma, klin, plin, Omega_m)
    for i in range(len(Ma)):
        npt.assert_equal(bias.bias_at_M(Ma[i], klin, plin, Omega_m), arrout[i])

def test_s2_and_nu_functions():
    #Test the mass calls
    s2 = bias.sigma2_at_M(Mass, klin, plin, Omega_m)
    nu = bias.nu_at_M(Mass, klin, plin, Omega_m)
    npt.assert_equal(1.686/np.sqrt(s2), nu)
    s2 = bias.sigma2_at_M(Ma, klin, plin, Omega_m)
    nu = bias.nu_at_M(Ma, klin, plin, Omega_m)
    npt.assert_array_equal(1.686/np.sqrt(s2), nu)
    out = bias.bias_at_M(Ma, klin, plin, Omega_m)
    out2 = bias.bias_at_nu(nu)
    npt.assert_array_equal(out, out2)
    #Now test the R calls
    R = 1.0 #Mpc/h; arbitrary
    s2 = bias.sigma2_at_R(R, klin, plin)
    nu = bias.nu_at_R(R, klin, plin)
    npt.assert_equal(1.686/np.sqrt(s2), nu)
    out = bias.bias_at_R(R, klin, plin)
    out2 = bias.bias_at_nu(nu)
    npt.assert_array_equal(out, out2)

def test_R_vs_M():
    R = 1.0 #Mpc/h
    M = 4.*np.pi/3. * Omega_m * rhomconst * R**3
    npt.assert_almost_equal(bias.bias_at_R(R, klin, plin), bias.bias_at_M(M, klin, plin, Omega_m))
    R = np.array([1.2, 1.4, 1.5])
    M = 4.*np.pi/3. * Omega_m * rhomconst * R**3
    npt.assert_array_almost_equal(bias.bias_at_R(R, klin, plin), bias.bias_at_M(M, klin, plin, Omega_m))

def test_mass_dependence():
    masses = np.logspace(13, 15, num=100)
    arrout = bias.bias_at_M(masses, klin, plin, Omega_m)
    for i in range(len(masses)-1):
        assert arrout[i] < arrout[i+1]
    Rs = (masses/(4./3.*np.pi*Omega_m*rhomconst))**(1./3.)
    arrout = bias.bias_at_R(Rs, klin, plin)
    for i in range(len(masses)-1):
        assert arrout[i] < arrout[i+1]
    nus = bias.nu_at_M(masses, klin, plin, Omega_m)
    arrout = bias.bias_at_nu(nus)
    for i in range(len(masses)-1):
        assert arrout[i] < arrout[i+1]
