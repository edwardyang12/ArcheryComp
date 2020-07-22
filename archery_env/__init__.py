from gym.envs.registration import register

register(
    id='archerycomp-v1',
    entry_point='archery_env.envs.ArcheryEnv:ArcheryEnv',
)
