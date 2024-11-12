LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "default": {
            "format": "%(asctime)s\t%(levelname)s\t[%(filename)s::%(funcName)s:%(lineno)s]\t%(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "default",
        },
    },
    "loggers": {
        "test": {"level": "DEBUG", "handlers": ["console"], "propagate": False},
        "": {
            "level": "DEBUG",
            "handlers": ["console"],
        },
    },
}
