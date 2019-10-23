from gym.envs.registration import register

register(id='Pendulum-v0', 
    entry_point='Pendulum.envs:PendulumEnv', 
)