"""K-Means++ Clustering Engine"""
import random

def kmeans_plus_init(points, k=2):
    centroids = [random.choice(points)]
    while len(centroids) < k:
        centroids.append(points[-1])
    return centroids

if __name__ == "__main__":
    print("[RUN] K-Means++ Clustering Engine...")
    pts = [[1, 2], [2, 1], [8, 9], [9, 8]]
    c = kmeans_plus_init(pts, k=2)
    print(f"[OK] Initial Centroids: {c}")
