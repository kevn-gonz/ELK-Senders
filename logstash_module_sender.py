import logging
import logstash
lshost = '<LOGSTASH_HOST>'
lsport = '5069'
logger = logging.getLogger('python-logstash-logger')
logger.setLevel(logging.INFO)
logger.addHandler(logstash.TCPLogstashHandler(lshost, lsport, version=1))
extra = {
'test_string': 'PINEAPPLE',
'test_boolean': True,
'test_dict': {'a': 1, 'b': 'c'},
'test_float': 1.23,
'test_integer': 123,
'test_list': [1, 2, 3],
'test_field': "asdf"
}
logger.info('python-logstash: test logstash info message.', extra=extra)

#logger.debug('DEBUG', extra=extra)
#logger.warning('WARNING', extra=extra)
#logger.critical('CRITICAL', extra=extra)
#logger.error('ERROR', extra=extra)



