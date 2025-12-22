

First, we are using workload identity federation. We can exchange the kubernetes projected SA token for an access token on the blueprint. But to do that, the blueprint we pick $BLUEPRINT_ID must have its federated workload credentials set up. From our helper tool, we can run:

```bash
./run.sh add-federated-credential --blueprint-id $BLUEPRINT_ID --issuer https://oidc7de4f053.blob.core.windows.net/oidc --subject "system:serviceaccount:entra-demo:ai-agent-cli-sa" --name "ai-agent-cli-sa-mapping"
```

Things to note:
* `issuer` is the public facing OIDC issuer for our workload identity federation setup
* `subject` is the full service account from kubernetes, this is the mapping
* `name` is just how it's named on the Entra side

Now when the sidecar sends the projected token to exchange for blueprint access token, entra will trust it. 

Since in this app we do a lot of OBO stuff, we need to make sure all of the `access_as_user` stuff is set up. When you create a new blueprint with `create-new-blueprint` in the `entra-agent-cli` this gets set upu automatically. 

You set up the `sidecar` configuration in .env:

TOKEN_PROVIDER_MODE=sidecar

You will need agent gateway running:

```bash
agentgateway -f agentgateway_config.yaml
```
At the moment we are using agw `v0.10.5` but we should upgrade shortly.

This config is for azure openai access as well as mcp access. The mcp server is at:

* `http://localhost:3000/mcp` and it expects the entra agent ID obo token (for the MCP app `MCP_SERVER_APP_ID` in .env)

You will need to deploy the workload (sleep/sidecar) into kubernetes:

```bash
./kubernetes/deploy.sh
```

And then port forward the pod on `5000`

Then when you `./run.sh` it will try to acquire all the right tokens and be ready for running. 

Make sure that the CLIENT_ID from the `$ROOT/.env` matches what's in `$ROOT/ai-agent-cli/.env`


To actually run in k8s, you need to build and load the ai-agent-cli into kind/kubernetes cluster:

```bash
make k8s-load-kind KIND_CLUSTER=entra-workload-federation
```

