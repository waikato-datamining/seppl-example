from seppl import ClassListerRegistry

# the default class lister
MY_DEFAULT_CLASS_LISTERS = "my.class_lister"

# the environment variable to use for overriding the default modules
# (comma-separated list)
MY_ENV_CLASS_LISTERS = "MY_CLASS_LISTERS"

# singleton of the Registry
REGISTRY = ClassListerRegistry(default_class_listers=MY_DEFAULT_CLASS_LISTERS,
                               env_class_listers=MY_ENV_CLASS_LISTERS)
