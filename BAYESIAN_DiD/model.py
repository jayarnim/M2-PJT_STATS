import pymc as pm


class BayesianDiD:
    def __init__(self, df, target):
        self.model = pm.Model()
        self.DATA(df, target)

    def build(self):
        with self.model:
            # PRIORS
            FIXED_EFFECT = self.FIXED()
            COVID_EFFECT = self.ATT()
            PI = self.TREATED()
            sigma = pm.HalfNormal('sigma', 1)

            # LIKELIHOOD
            D = pm.Bernoulli("D", p=PI)
            mu = (
                FIXED_EFFECT
                + COVID_EFFECT * (D*self.post_idx)
            )
            y = pm.Normal('y', mu, sigma, observed=self.y_obs)

    def fit(
        self, 
        draws=5000, 
        tune=5000,  
        target_accept=0.95, 
        chains=4, 
        cores=4,
        random_seed=42,
    ):
        with self.model:
            trace = pm.sample(
                draws=draws, 
                tune=tune, 
                target_accept=target_accept, 
                chains=chains, 
                cores=cores,
                random_seed=random_seed,
                progressbar=True,
            )
        return trace

    def DATA(self, df, target):
        self.N_AREA = df['AREA'].nunique()
        self.N_IND  = df['INDUSTRY'].nunique()
        self.N_TIME = df['TIME'].nunique()

        self.y_obs = df[target].values
        self.area_idx = df['AREA'].values
        self.ind_idx  = df['INDUSTRY'].values
        self.time_idx = df['TIME'].values
        self.post_idx = df['POST'].values

    def FIXED(self):
        # LEVEL 3:
        alpha_tau = pm.HalfNormal('alpha_tau', 1)
        beta_tau = pm.HalfNormal('beta_tau', 1)
        gamma_tau = pm.HalfNormal('gamma_tau', 1)

        # LEVEL 2:
        alpha_raw = pm.Normal('alpha_raw', 0, 1, shape=self.N_AREA)
        beta_raw = pm.Normal('beta_raw', 0, 1, shape=self.N_IND)
        gamma_raw = pm.Normal('gamma_raw', 0, 1, shape=self.N_TIME)

        omega = pm.Normal('omega', 0, 1)
        alpha = pm.Deterministic('alpha', alpha_raw*alpha_tau)
        beta  = pm.Deterministic('beta',  beta_raw*beta_tau)
        gamma = pm.Deterministic('gamma', gamma_raw*gamma_tau)

        # CONCAT:
        FIXED_EFFECT = (
            omega                       # INTERCEPT
            + alpha[self.area_idx]      # AREA
            + beta[self.ind_idx]        # INDUSTRY
            + gamma[self.time_idx]      # TIME
        )

        return FIXED_EFFECT

    def ATT(self):
        # LEVEL 3:
        p_tau = pm.HalfNormal('p_tau', 1)
        q_tau = pm.HalfNormal('q_tau', 1)

        # LEVEL 2:
        p_raw = pm.Normal('p_raw', 0, 1, shape=self.N_AREA)
        q_raw = pm.Normal('q_raw', 0, 1, shape=self.N_IND)

        delta = pm.Normal('delta', 0, 1)
        p = pm.Deterministic('p', p_raw*p_tau)
        q  = pm.Deterministic('q', q_raw*q_tau)

        # CONCAT:
        COVID_EFFECT = (
            delta                     # INTERCEPT
            + p[self.area_idx]        # AREA
            + q[self.ind_idx]         # INDUSTRY
        )

        return COVID_EFFECT

    def TREATED(self):
        # LEVEL 3:
        u_tau = pm.HalfNormal('u_tau', 1)
        v_tau = pm.HalfNormal('v_tau', 1)
        
        # LEVEL 2:
        u_raw = pm.Normal('u_raw', 0, 1, shape=self.N_AREA)
        v_raw = pm.Normal('v_raw', 0, 1, shape=self.N_IND)
        
        eta = pm.Normal('eta', 0, 1)
        u = pm.Deterministic('u', u_raw*u_tau)
        v = pm.Deterministic('v', v_raw*v_tau)

        # CONCAT:
        PI = pm.math.sigmoid(
            eta                         # INTERCEPT
            + u[self.area_idx]          # AREA
            + v[self.ind_idx]           # INDUSTRY
        )

        return PI