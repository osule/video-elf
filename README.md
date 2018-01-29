# Video Elf #
This function extracts media info from a Youtube URL allowing you to download them directly.


## Dependencies ##
- youtube_dl


## Deploying to Minikube ##
In order to deploy ensure you have a cluster running on kubernetes by following [these steps](https://github.com/nuclio/nuclio/blob/0.2.4/docs/setup/k8s/getting-started-k8s.md).


Then, deploy:
```bash
./bin/deploy
```


## Testing ##

Run this following line in your terminal to run the tests.

```bash
PYTHONPATH=$(pwd) pytest .
```
