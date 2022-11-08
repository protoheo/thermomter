from thermometer import Thermometer
import yaml


def load_yaml(cfg_path='configs/config.yaml'):
    return yaml.full_load(open(cfg_path, 'r', encoding='utf-8-sig'))


if __name__ == '__main__':
    cfg = load_yaml()
    target_site = cfg['TARGET_SITE']
    tm = Thermometer(target_site, cfg)
    tm.login()
    tm.get_rest_time()

