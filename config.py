from oslo_config import cfg

CONF = cfg.CONF

opts = [
	cfg.StrOpt('test',
               default='test',
               help='Test'),
	]

CONF.register_opts(opts)

CONF(['--config-file', '~/agent/config.conf'])