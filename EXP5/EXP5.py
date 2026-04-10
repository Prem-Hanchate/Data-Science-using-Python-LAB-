import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def save_kmeans_visualizations(X_scaled, cluster_labels, kmeans, output_dir):
    # Elbow curve helps validate why k=3 is a reasonable choice.
    k_values = range(1, 11)
    inertias = []
    for k in k_values:
        model = KMeans(n_clusters=k, random_state=42, n_init=10)
        model.fit(X_scaled)
        inertias.append(model.inertia_)

    plt.figure(figsize=(8, 5))
    plt.plot(k_values, inertias, marker="o")
    plt.title("Elbow Method for K-Means")
    plt.xlabel("Number of Clusters (k)")
    plt.ylabel("Inertia")
    plt.grid(alpha=0.3)
    elbow_path = output_dir / "kmeans_elbow_curve.png"
    plt.tight_layout()
    plt.savefig(elbow_path, dpi=150)
    plt.close()

    # PCA projects high-dimensional features to 2D for easy cluster visualization.
    pca = PCA(n_components=2, random_state=42)
    X_pca = pca.fit_transform(X_scaled)
    centers_pca = pca.transform(kmeans.cluster_centers_)

    plt.figure(figsize=(8, 6))
    scatter = plt.scatter(
        X_pca[:, 0],
        X_pca[:, 1],
        c=cluster_labels,
        cmap="viridis",
        alpha=0.75,
        edgecolors="k",
        s=45,
    )
    plt.scatter(
        centers_pca[:, 0],
        centers_pca[:, 1],
        c="red",
        marker="X",
        s=220,
        label="Centroids",
    )
    plt.title("K-Means Clusters Visualized with PCA (2D)")
    plt.xlabel("Principal Component 1")
    plt.ylabel("Principal Component 2")
    plt.legend(loc="best")
    plt.colorbar(scatter, label="Cluster ID (0-based)")
    plt.grid(alpha=0.2)
    cluster_plot_path = output_dir / "kmeans_clusters_pca.png"
    plt.tight_layout()
    plt.savefig(cluster_plot_path, dpi=150)
    plt.close()

    return elbow_path, cluster_plot_path


def main():
    # 1) Load data (unsupervised: no class label column)
    base_dir = Path(__file__).resolve().parent
    file_path = base_dir / "wine-clustering.csv"
    df = pd.read_csv(file_path)

    # 2) Prepare features
    feature_columns = df.columns.tolist()
    X = df[feature_columns].copy()

    # 3) Scale features before clustering and supervised learning
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # 4) Discover 3 wine types using clustering
    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    cluster_labels = kmeans.fit_predict(X_scaled)

    # Convert cluster IDs to 1, 2, 3 for readability
    df["Wine_Type"] = cluster_labels + 1

    # 5) Build supervised dataset using discovered labels
    X_supervised = X_scaled
    y_supervised = df["Wine_Type"]

    X_train, X_test, y_train, y_test = train_test_split(
        X_supervised,
        y_supervised,
        test_size=0.25,
        random_state=42,
        stratify=y_supervised,
    )

    # 6) Train classifier on generated labels
    clf = RandomForestClassifier(n_estimators=300, random_state=42)
    clf.fit(X_train, y_train)

    # 7) Evaluate
    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    print("=== Supervised Learning on Generated Wine Types ===")
    print(f"Accuracy: {acc:.4f}\n")
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred), "\n")
    print("Classification Report:")
    print(classification_report(y_test, y_pred, digits=4))

    # 8) Show profile of the 3 discovered wine types
    print("\n=== Mean Feature Values Per Discovered Wine Type ===")
    cluster_profile = df.groupby("Wine_Type")[feature_columns].mean()
    print(cluster_profile)

    # 9) Save visualizations for report/presentation use
    elbow_path, cluster_plot_path = save_kmeans_visualizations(
        X_scaled, cluster_labels, kmeans, base_dir
    )
    print("\nSaved visualizations:")
    print(f"- Elbow Curve: {elbow_path}")
    print(f"- PCA Cluster Plot: {cluster_plot_path}")

    # 10) Save supervised dataset
    output_path = base_dir / "wine-supervised.csv"
    df.to_csv(output_path, index=False)
    print(f"\nSaved supervised dataset with labels to: {output_path}")


if __name__ == "__main__":
    main()
