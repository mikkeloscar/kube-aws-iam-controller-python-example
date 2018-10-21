# kube-aws-iam-controller Python SDK (boto3) Example

This is an example to demo/verify that the [AWS Python
SDK (boto)](https://github.com/boto/botocore) works with the
[kube-aws-iam-controller](https://github.com/mikkeloscar/kube-aws-iam-controller).

It works by using
[credential_process](https://docs.aws.amazon.com/cli/latest/topic/config-vars.html#sourcing-credentials-from-external-processes)
feature of the SDK where it can refresh credentials from an external process.

The external process is simply `cat /meta/aws-iam/credentials.json` injected by
[kube-aws-iam-controller](https://github.com/mikkeloscar/kube-aws-iam-controller)
which is assumed to be [running in your
cluster](https://github.com/mikkeloscar/kube-aws-iam-controller#setup).

The example just goes to EC2 every 5 min. and lists the current instances:

```
2018-10-21 10:34:06,437 - __main__ - INFO - Getting instances
2018-10-21 10:34:06,641 - __main__ - INFO - i-abcd1234 - t2.medium
2018-10-21 10:34:06,641 - __main__ - INFO - i-abcd1234 - t2.medium
2018-10-21 10:34:06,641 - __main__ - INFO - i-abcd1234 - t2.medium
```

## Build

```bash
$ docker build --rm -t mikkeloscar/kube-aws-iam-controller-python-example:latest .
$ docker push mikkeloscar/kube-aws-iam-controller-python-example:latest
```

## Create IAM Role

```bash
# $ASSUME_ROLE_ARN is the arn of the role used by the kube-aws-iam-controller deployment
$ aws cloudformation create-stack --stack-name aws-iam-example \
  --parameters "ParameterKey=AssumeRoleARN,ParameterValue=$ASSUME_ROLE_ARN" \
  --template-body=file://iam-role.yaml --capabilities CAPABILITY_NAMED_IAM
```

## Deploy exmaple

```bash
$ kubectl apply -f deployment.yaml
```
