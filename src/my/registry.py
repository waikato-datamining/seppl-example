from seppl import Registry

# the default modules to look for plugins
MY_DEFAULT_MODULES = ",".join(
    [
        "my.plugins",
    ])

# the environment variable to use for overriding the default modules
# (comma-separated list)
MY_ENV_MODULES = "MY_MODULES"

# singleton of the Registry
REGISTRY = Registry(default_modules=MY_DEFAULT_MODULES,
                    env_modules=MY_ENV_MODULES,
                    enforce_uniqueness=True)

