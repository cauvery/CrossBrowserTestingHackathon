#!/usr/bin/env python
from core_utils import log
import yaml

logger = log.getLogger(__name__)

default_config_dir = "./conf/"

def getConfig(env="", config=None):
    logger.info("load system config")
    if config:   
        return yaml.load(open(config).read(), Loader=yaml.FullLoader)
    else:
        return yaml.load(open(default_config_dir+"config_"+env+".yaml").read(), Loader=yaml.FullLoader)