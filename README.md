# DevOps Lab Exercises Repository

This repository contains hands-on DevOps lab exercises covering containerization, container orchestration, CI/CD pipelines, security profiling, and monitoring/alerting systems.

**Author / Maintainer:** [JANKITHKUMAR](https://github.com/JANKITHKUMAR)  
**Repository:** [DevOps-Lab](https://github.com/JANKITHKUMAR/DevOps-Lab)

---

## Exercise Catalog

| # | Exercise Folder | Key Technologies | Description |
|---|---|---|---|
| **01** | [`Exercise-01-Kubernetes-Getting-Started`](./Exercise-01-Kubernetes-Getting-Started) | Kubernetes, Minikube, Nginx | Deploy first containerized Pod (`hello-k8s`) and expose it as a NodePort Service. |
| **02** | [`Exercise-02-Minikube-Kubectl-Flask`](./Exercise-02-Minikube-Kubectl-Flask) | Kubernetes, Minikube, Docker, Python Flask | Build and deploy a Python Flask app on Minikube using Deployments and NodePort Services. |
| **03** | [`Exercise-03-Minikube-Scaling-Flask-App-with-Replicasets`](./Exercise-03-Minikube-Scaling-Flask-App-with-Replicasets) | Kubernetes, ReplicaSets, Gunicorn, Flask | Implement horizontal scaling and high availability with ReplicaSets, health checks, and probes. |
| **04** | [`Exercise-04-Docker-Networking`](./Exercise-04-Docker-Networking) | Docker, Bridge Networks, Flask, MySQL, Redis | Multi-container application networking with custom bridge network, inter-container DNS and ping tests. |
| **05** | [`Exercise-05-Docker-Security-AppArmor`](./Exercise-05-Docker-Security-AppArmor) | Docker Security, AppArmor, Python Docker SDK | Enforce Linux AppArmor security profiles on Docker containers to restrict file and binary execution. |
| **06** | [`Exercise-06-Grafana-Realtime-Monitoring-of-Quick-Commerce-App`](./Exercise-06-Grafana-Realtime-Monitoring-of-Quick-Commerce-App) | Prometheus, Grafana, Jenkins, Python | Real-time operations monitoring with custom Prometheus metrics, alerting rules, and Grafana dashboards. |
| **07** | [`Exercise-07-Jenkins-CI-Automation`](./Exercise-07-Jenkins-CI-Automation) | Jenkins LTS, Docker, CI/CD | Comprehensive introduction to Continuous Integration (CI), Jenkins container deployment, and admin setup. |
| **08** | [`Exercise-08-Jenkins-Hello-World-Job`](./Exercise-08-Jenkins-Hello-World-Job) | Jenkins, GitHub, Bash, Freestyle Job | Create and execute your first Jenkins Freestyle Job linked to a GitHub repository. |
| **09** | [`Exercise-09-Jenkins-Multi-Stage-Pipeline`](./Exercise-09-Jenkins-Multi-Stage-Pipeline) | Jenkins Pipeline (Groovy), Flask, Unittest | Automate a 5-stage CI/CD pipeline (Build, Test, Deploy, Run, Verify) for a Python web application. |
| **10** | [`Exercise-10-Minikube-Multi-Node-Deployment`](./Exercise-10-Minikube-Multi-Node-Deployment) | Minikube Multi-Node, Pod Anti-Affinity, Flask | Multi-node cluster deployment of Product Catalog & Shopping Cart microservices with Pod Anti-Affinity rules. |

---

## Prerequisites & Tooling
- **Docker Engine / Docker Desktop** (v20+): Container virtualization.
- **Minikube** (v1.30+): Local Kubernetes cluster development.
- **Kubectl** (v1.28+): Kubernetes command-line interface.
- **Python** (v3.9+): Application development and test runners (`flask`, `prometheus-client`, `docker`).
- **Jenkins** (LTS): Automation server.
- **Prometheus & Grafana**: Time-series metrics collection and visualization.

---

## Running Verification Tests
Each Python-based exercise includes automated unit tests. To run all tests across the repository:

```bash
# Run unit tests across all exercises
python -m unittest discover -s . -p "test_*.py"
```

---

## License & Attribution
Developed and maintained for DevOps Engineering practice and learning.
