void P_BBPS(double *P_out, const double *r, unsigned Nr, double M_delta, double z, double omega_b, double omega_m, double P_0, double x_c, double beta, double alpha, double gamma, double delta);
int projected_P_BBPS(double *P_out, double *P_err_out, const double *r, unsigned Nr, double M_delta, double z, double omega_b, double omega_m, double P_0, double x_c, double beta, double alpha, double gamma, double delta, unsigned limit, double epsabs, double epsrel);
int fourier_P_BBPS(double *up_out, double *up_err_out, const double *ks, unsigned Nk, double M_delta, double z, double omega_b, double omega_m, double P_0, double x_c, double beta, double alpha, double gamma, double delta, unsigned limit, double epsabs);
