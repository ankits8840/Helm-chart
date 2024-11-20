import yaml
import csv
import os

hosts_file = os.path.join("config", "hosts.yaml")
paths_file = os.path.join("config", "paths.yaml")
output_csv = "output.csv"

def load_yaml(file_path):
    with open(file_path, "r") as file:
        return yaml.safe_load(file)

def generate_combinations(hosts, paths):
    combinations = []
    for host in hosts["hosts"]:
        for path in paths["paths"]:
            sample_cta = f"{host}{path['sample_url']}"
            cta_url = f"{host}{path['dynamic_url']}"
            combinations.append((cta_url, sample_cta))
    return combinations

def save_to_csv(combinations, output_file):
    with open(output_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["cta", "sample_cta"])
        for cta, sample_cta in combinations:
            writer.writerow([cta, sample_cta])
    print(f"CSV file generated: {output_file}")

if __name__ == "__main__":
    hosts = load_yaml(hosts_file)
    paths = load_yaml(paths_file)

    combinations = generate_combinations(hosts, paths)

    save_to_csv(combinations, output_csv)
