import pystan
import pandas as pd


trend2 = pd.read_csv('trend2.csv')

trend2 = trend2.dropna(axis = 0, how = 'any', thresh = None )

trend2.country = trend2.country.str.strip()
unqcountries = trend2.country.unique()
lencountry = len(unqcountries)

lookup_countries = dict(zip(unqcountries, range(len(unqcountries))))
countries = trend2['country_code'] = trend2.country.replace(lookup_countries).values

degree_inequality = trend2.gini_net.values
degree_religion = trend2.church2.values
realgdp = trend2.rgdpl.values

varying_intercept = """
data {
  int<lower=0> J; 
  int<lower=0> N; 
  int<lower=1,upper=J> countries[N];
  vector[N] x1;
  vector[N] x2;
  vector[N] y;
}
parameters {
  vector[J] a;
  real b1;
  real b2;
  real mu_a;
  real<lower=0,upper=100> sigma_a;
  real<lower=0,upper=100> sigma_y;
}
transformed parameters {
  vector[N] y_hat;
  for (i in 1:N)
    y_hat[i] = a[countries[i]] + x1[i] * b1 + x2[i] * b2;
}
model {
  sigma_a ~ uniform(0, 100);
  a ~ normal (mu_a, sigma_a);
  b1 ~ normal (0, 1);
  b2 ~ normal (0, 1);
  sigma_y ~ uniform(0, 100);
  y ~ normal(y_hat, sigma_y);
}
"""

varying_intercept_data = {'N': len(degree_religion),
                          'J': len(unqcountries),
                          'countries': countries+1,
                          'x1': degree_inequality,
                          'x2': realgdp,
                          'y': degree_religion}
varying_intercept_fit = pystan.stan(model_code=varying_intercept, data=varying_intercept_data, iter=1000, chains=2)
varying_intercept_fit

print(varying_intercept_fit)