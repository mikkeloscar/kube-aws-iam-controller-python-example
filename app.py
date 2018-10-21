#!/usr/bin/python

import boto3
import time
import logging

log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO,format=log_format)
logger = logging.getLogger(__name__)


def main():
    ec2 = boto3.resource('ec2')

    while True:
        logger.info("Getting instances")
        instances = ec2.instances.filter(
            Filters=[{'Name': 'instance-state-name', 'Values': ['running']}],
        )
        for instance in instances:
            logger.info("{} - {}".format(instance.id, instance.instance_type))
        # sleep for 5 min.
        time.sleep(60 * 5)
    return


if __name__ == '__main__':
    main()
