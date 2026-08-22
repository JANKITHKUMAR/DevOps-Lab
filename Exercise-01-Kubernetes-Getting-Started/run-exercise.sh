#!/bin/bash
# Exercise 1: Kubernetes Getting Started
echo "Starting Minikube..."
minikube start

echo "Deploying Nginx Pod..."
kubectl apply -f pod.yaml

echo "Verifying Pod status..."
kubectl get pods

echo "Exposing Pod via NodePort Service..."
kubectl apply -f service.yaml

echo "Verifying Service..."
kubectl get services

echo "To access the service in browser:"
echo "minikube service hello-k8s"
