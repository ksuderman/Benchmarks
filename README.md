# Cloud Costs Benchmarks

This repository collects the RNA-Seq, Variant calling, and Single Cell benchmarks that are scattered amongst several other repositories including, but not limited to:

1. [Resource Prediction Experiments](https://github.com/ksuderman/resource-prediction-experiments)
2. Biology of Genomes
3. [Experiments](https://github.com/ksuderman/Experiments)

## Experiments

Each of the `rnaseq`, `variant`, and `single-cell` directories contain the benchmark, experiment, and TPV configuration files required to run the benchmark experiments.

## Results Tables

1. [RNA-Seq](rnaseq/RNA-Seq-Defaults.md)
2. [Ice Lake](results/IceLake.md)


## Files

**costs.sh**<br/>Environment variable definitions used when creating a GKE cluster. See [Variables](#variables) below for a description of the variables used.<br/>
**cascade-lake.sh**<br/>Variable definitions used for the clusters using Intel Cascade Lake cpus.<br/>
**ice-lake.sh**<br/>Variable definitions used for the clusters using Intel Ice Lake cpus.<br/>
**anvil**<br/> is a Bash script used to manage the GKE clusters used to run the experiments. Run `anvil --help` for full usage information.

## Ensuring the CPU Type

Google supports specifying a `--min-cpu-platform`, but that is a *minimum* and we may get a later CPU family if the minium requested family is not available.  Therefore we need to ensure the CPUs used in the cluster are actually the type requested.

```bash
# SSH into the node
gcloud compute ssh --zone <ZONE> <instance name>

# Install GCC
sudo apt update
sudo apt install build-essential

# Get the CPU family name
gcc -march=native -Q --help=target | grep -march
```
### Create a cluster
```bash
anvil --settings settings.sh cluster disks galaxy
```

### Destroying a cluster
```bash
anvil --settings settings.sh cleanup delete-disks
```

If you do not delete the persistent disks they can be re-attached to a new cluster as long as the same cluster `--prefix` is used.  The easiest way to achieve this is to use a `settings` file that contains definitions for the common variable definitions.

```bash
anvil --settings settings.sh cluster disks galaxy
anvil --settings settings.sh cleanup 
anvil --settings settings.sh cluster galaxy # Will re-use the persistent disks created in step 1
```

## Variables

The following environment variables can be set that will be used by the `anvil` Bash script.

**MACHINE**<br/>Machine type for cluster nodes, e.g. `n2-standard-32`.

**PREFIX**<br/>A prefix string used to when creating resources.

**NAMESPACE**<br/>Kubernetes/Helm namespace used when installing Galaxy.  Defaults to `galaxy`. 

**IMAGE**<br/>Docker image used to install Galaxy. Defaults to `quay.io/galaxyproject/galaxy-anvil`. 

**TAG**<br/>Image tag of the Docker image used to install Galaxy. Defaults to `23.1`.

**CHART**<br/>Helm chart used to install Galaxy. Defaults to `anvil/galaxykubeman`. 

**DISK**<br/>Size of the persistent disk created. In GB. Defaults to `768`.

